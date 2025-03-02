import asyncio
import json
import os

import click
from dotenv import load_dotenv
from twikit.client.client import Client as TwiKit

# Load environment variables
load_dotenv()


def get_env_var(name: str) -> str:
    """Retrieve an environment variable and raise an error if missing."""
    value = os.getenv(name)
    if value is None:
        raise ValueError(f"❌ Missing required environment variable: {name}")
    return value


async def fetch_latest_tweet():
    """Fetches the latest tweet from Elon Musk and returns it as a dictionary."""
    tk = TwiKit()

    await tk.login(  # type: ignore
        auth_info_1=get_env_var("TWITTER_USERNAME"),
        auth_info_2=get_env_var("TWITTER_EMAIL"),
        password=get_env_var("TWITTER_PASSWORD"),
        cookies_file=get_env_var("TWITTER_COOKIES_FILE"),
    )

    latest_tweet = await tk.get_user_tweets("44196397", "Tweets", count=1)

    if latest_tweet:
        tweet = latest_tweet[0]

        # Convert tweet object to dictionary (extracting all attributes)
        tweet_data = {
            attr: getattr(tweet, attr)
            for attr in dir(tweet)
            if not attr.startswith("_") and not callable(getattr(tweet, attr))
        }

        return tweet_data
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
