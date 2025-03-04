import asyncio
import json
import os

import click
from dotenv import load_dotenv
from httpx import Response
from twikit.client.client import Client as TwiKit
from twikit.tweet import Tweet
from twscrape.api import API

load_dotenv()


def get_env_var(name: str) -> str:
    """Retrieve an environment variable and raise an error if missing."""
    value = os.getenv(name)
    if value is None:
        raise ValueError(f"❌ Missing required environment variable: {name}")
    return value


async def fetch_latest_tweet_details(api: API, tweet: Tweet) -> Response:
    return await api.tweet_details_raw(tweet.id) or Response(  # type: ignore
        status_code=200, content=b"{}"
    )


async def fetch_latest_tweet():
    """Fetches the latest tweet from Elon Musk and returns it as a dictionary."""
    tk = TwiKit()
    api = API()
    username = get_env_var("TWITTER_USERNAME")
    email = get_env_var("TWITTER_EMAIL")
    password = get_env_var("TWITTER_PASSWORD")
    cookies_file = get_env_var("TWITTER_COOKIES_FILE")

    await tk.login(  # type: ignore
        auth_info_1=username,
        auth_info_2=password,
        password=password,
        cookies_file=cookies_file,
    )

    with open(cookies_file, "r") as file:
        cookies = json.dumps(json.load(file))

    await api.pool.add_account(  # type: ignore
        username=username,
        password=password,
        email=email,
        email_password=password,
        cookies=cookies,
    )

    await api.pool.login_all()  # type: ignore

    latest_tweet = await tk.get_user_tweets("44196397", "Tweets", count=1)
    if latest_tweet:
        tweet = latest_tweet[0]
        summary = {
            attr: getattr(tweet, attr)
            for attr in dir(tweet)
            if not attr.startswith("_") and not callable(getattr(tweet, attr))
        }

        summary["details"] = fetch_latest_tweet_details(api, tweet)

        return summary
    else:
        raise ValueError("❌ No tweets found.")


@click.command()
@click.option(
    "--output", "-o", type=click.Path(), help="Path to save output JSON file."
)
def main(output: str):
    try:
        tweet_data = asyncio.run(fetch_latest_tweet())

        if output:
            # Save JSON to file (convert datetime objects to string)
            with open(output, "w", encoding="utf-8") as file:
                json.dump(tweet_data, file, ensure_ascii=False, indent=4, default=str)
            print(f"✅ Tweet saved to: {output}")
        else:
            # Print JSON to console (convert datetime objects to string)
            print(json.dumps(tweet_data, ensure_ascii=False, indent=4, default=str))

    except Exception as e:
        click.echo(f"❌ Error: {e}", err=True)


if __name__ == "__main__":
    main()
