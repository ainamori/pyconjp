#!/usr/bin/env python3
#  -*- coding: utf-8 -*
import json


class DemoClass:

    @classmethod
    def demo_get(cls, demo_path):
        messages = {
            "your_path": demo_path,
            "messages": "Static Message"
        }
        json_body = json.dumps(messages)
        status_code = 200
        return json_body, status_code

    @classmethod
    def demo_post(cls, demo_path, body):
        messages = {
            "your_path": demo_path,
            "messages": body
        }
        json_body = json.dumps(messages)
        status_code = 200
        return json_body, status_code

    # @classmethod
    def none_class_get(self, demo_path):
        messages = {
            "your_path": demo_path,
            "messages": "Static Message"
        }
        json_body = json.dumps(messages)
        status_code = 200
        return json_body, status_code
