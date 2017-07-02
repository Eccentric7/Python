#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  1 18:52:15 2017

@author: eccentric7
"""
import fresh_tomatoes 
import media 

fight_club = media.Movie("Fight Club","A story about a soap salesman and his friend","http://images.moviepostershop.com/fight-club-movie-poster-1999-1020215604.jpg","https://youtu.be/SUXWAEX2jlg")
#print(fight_club.poster_image_url)


ex_machina = media.Movie("Ex Machina","A story about AI","http://www.joblo.com/posters/images/full/ex-machina-large.jpg", "https://www.youtube.com/watch?v=XYGzRB4Pnq8")
#print(ex_machina.title)
#ex_machina.show_trailer()

i_robot = media.Movie("I Robot", "Story of robots and human interaction", "http://image.tmdb.org/t/p/original/laggUPDhOh8mbeFsk50p72ddcpn.jpg","https://www.youtube.com/watch?v=s0f3JeDVeEo")

lord_of_war = media.Movie("Lord of Ward", "Story of an armsdealer","http://oi53.tinypic.com/2n66fcg.jpg", "https://www.youtube.com/watch?v=ke79K4bO4P8")

movies = (fight_club, ex_machina, i_robot, lord_of_war)
fresh_tomatoes.open_movies_page(movies)