# Copyright 2016 Mycroft AI, Inc.
#
# This file is part of Mycroft Core.
#
# Mycroft Core is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Mycroft Core is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Mycroft Core.  If not, see <http://www.gnu.org/licenses/>.

from os.path import dirname

from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill
from mycroft.util.log import getLogger

from urllib2 import urlopen

__author__ = 'Dark5ide'

LOGGER = getLogger(__name__)

class Esp8266Skill(MycroftSkill):

    def __init__(self):
        super(Esp8266Skill, self).__init__(name="Esp8266Skill")
    
    def initialize(self):
        self.load_data_files(dirname(__file__))
        self.__build_turn_on_lights()
        self.__build_turn_off_lights()
        
    def __build_turn_on_lights(self):
        intent = IntentBuilder("TurnOnAllLightsIntent").require("TurnOnLightsKeyword").build()
        self.register_intent(intent, self.handle_turn_on_lights)
        
    def __build_turn_off_lights(self):
        intent = IntentBuilder("TurnOffAllLightsIntent").require("TurnOffLightsKeyword").build()
        self.register_intent(intent, self.handle_turn_off_lights)
        
    def handle_turn_on_lights(self, message):
        urlopen("http://esp8266.local/led0?state=on")
        urlopen("http://esp8266.local/led1?state=on")
        self.speak_dialog("lights.on")
        
    def handle_turn_off_lights(self, message):
        urlopen("http://esp8266.local/led0?state=off")
        urlopen("http://esp8266.local/led1?state=off")
        self.speak_dialog("lights.off")
        
    def stop(self):
        pass
        
def create_skill():
    return Esp8266Skill()
