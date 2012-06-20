#!/usr/bin/env python
"""
raspberry_pi_farm.py
contains a some singing/dancing animals on the Raspberry Pi!

author: Thomas Preston
date  : 18/06/2012
"""

import subprocess
import pfio


VERBOSE_MODE = True


class Chicken(object):
	"""The wobbling/talking chicken"""
	def __init__(self):
		self.relay_pin = 1
		self.voice_pitch = 50 # 0-99
		self.voice_speed = 160 # words per min

		pfio.init()
	
	def __del__(self):
		pfio.deinit()

	def start_wobble(self):
		"""Starts wobbling the chicken"""
		pfio.digital_write(self.relay_pin, 1)
		if VERBOSE_MODE:
			print "Chicken has started wobbling."

	def stop_wobble(self):
		"""Stops wobbling the chicken"""
		pfio.digital_write(self.relay_pin, 0)
		if VERBOSE_MODE:
			print "Chicken has stopped wobbling."

	def say(self, text_to_say):
		"""Makes the chicken say something"""
		if VERBOSE_MODE:
			print "Chicken says: %s" % text_to_say

		# using 'espeak' to make the chicken talk
		subprocess.call(["espeak",
			"-v", "en-rp",
			"-p", str(self.voice_pitch),
			"-s", str(self.voice_speed),
			text_to_say])
