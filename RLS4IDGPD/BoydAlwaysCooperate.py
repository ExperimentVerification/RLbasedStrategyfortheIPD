#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Strategy import *

class BoydAlwaysCooperate(Strategy):
    def __init__(self, game):
        Strategy.__init__(self)
        self._lambda = Lambda(1.0) # only play the social game

    def respond(self, game):
        self._lambda.nochange()
        return 'C'

    def name(self):
        return "Always Cooperate from Boyd's Tournament"

    def author(self):
        return "In-house (Theodore Boyd)"