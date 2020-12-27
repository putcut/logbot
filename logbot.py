import asyncio
from pathlib import Path

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from discord.ext import commands

import config

class MyHandler(FileSystemEventHandler):
  def __init__(self):
    self.loop = loop

  def on_modified(self, event):
    path = Path(event.src_path)
    if path.name == config.FILE_NAME:
      asyncio.run_coroutine_threadsafe(send_message("Log modified."), self.loop)

bot = commands.Bot(command_prefix="!")
loop = bot.loop
event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, config.DIR_PATH, recursive=True)

@bot.command()
async def start(ctx):
  observer.start()
  ctx.send("Start log observer.")

@bot.command()
async def stop(ctx):
  observer.stop()
  ctx.send("Stop log observer.")

async def send_message(text):
  await bot.guilds[0].text_channels[0].send(text)

if __name__ == "__main__":
  bot.run(config.TOKEN)