# Import the necessary modules from the Telethon and PyTgCalls libraries
from telethon.sync import TelegramClient
from pytgcalls import PyTgCalls
from pytgcalls.types import MediaStream
import os

from dotenv import load_dotenv
load_dotenv()


# Define the main function
def main() -> None:
    """
    Start the PyTgCalls client and play a media stream.
    This function is the entry point of the program. It starts the PyTgCalls client and plays a media stream.
    """

    # Create a Telegram client instance
    client = TelegramClient('SusiMusicBot', int(os.getenv('APP_ID')), os.getenv('API_HASH'))
    
    # Create a PyTgCalls client instance using the Telegram client
    call_py = PyTgCalls(client)
    
    # Start the PyTgCalls client
    call_py.start()
    
    # Play the media stream on the specified entity (Example)
    play_media(call_py, int(os.getenv('CHAT_ID')), 'http://docs.evostream.com/sample_content/assets/sintel1m720p.mp4')
    
    # Keep the PyTgCalls client running
    call_py.idle()


# Define the play_media function
def play_media(call_py: PyTgCalls, entity_id: int, stream_url: str) -> None:
    """
    Play a media stream on a specified entity.

    This function plays a media stream on the specified entity.
    """
    # Play the media stream using the PyTgCalls client
    call_py.play(entity_id, MediaStream(stream_url))


# Check if the script is being run directly
if __name__ == '__main__':
    # Call the main function
    main()

