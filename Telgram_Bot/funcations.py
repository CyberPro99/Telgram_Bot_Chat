from typing import Text
from telegram import update
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
import Constance as keys
from telegram import *
from telegram.ext import Updater
import Respons as R
from pytube import YouTube
import pafy
import os


def start_command(update, context):
    update.message.reply_text("Hey Welcom to Mr.Bot this is Our Service" + "\n 1) ❤ Youtub Download Mp4 "+
    " \n 2) ❤ Youtub Download Mp3")
    print(start_command)
    
def help_command(update, context):
    update.message.reply_text('Type somthing to show help list!')
    print(help_command)

def handel_message(update, context):
    text = str(update.message.text).lower()
    response = R.sample_responses(text)
    update.message.reply_text(response)

def error(update, context):
    print(f"Update {update} caused error{context.error}")

def main():
    updater = Updater(keys.API_KET, use_context = True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start",start_command))
    dp.add_handler(CommandHandler("help",help_command))
    dp.add_handler(MessageHandler(filter.__text_signature__,handel_message))
    dp.add_error_handler(error)
    updater.start_polling(5)
    updater.idle()

def YouTub(Url):
  my_video = YouTube(Url)
  print(my_video.title)
  print(my_video.thumbnail_url)
  my_video = my_video.streams.get_highest_resolution()
  my_video.download()