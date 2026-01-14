from django.shortcuts import render
from django.http import HttpResponse

def guess_number (request, number=-1):
    """ Handles the magic number guessing game"""
    if number == -1:
        return HttpResponse ("You didn't guess a number!")
    
    elif number < 42:
        return HttpResponse (f"You're number {number} is smaller than my secret number!")
    
    elif number > 42:
        return HttpResponse (f"You're number {number} is bigger than my secret number!")
    
    elif number == 42:
        return HttpResponse (f"Bravo! The secret number is {number}!")


def error_url (request):
    """ Handles url errors"""
    return HttpResponse ("To play this game use magicnumber/guess/'you're number' URL pattern.")