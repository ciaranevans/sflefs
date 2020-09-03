#!/usr/bin/env python3
import os

from aws_cdk import core

from stack import SflefsStack

tags = {
    "APPLICATION": "sflefs",
    "ENV": os.environ.get("ENV", "dev"),
    "SOURCE": "https://github.com/ciaranevans/sflefs",
    "ORG": "Development Seed",
}

app = core.App()
SflefsStack(app, f"sflefs-{os.environ.get('ENV', 'dev')}")
_ = [core.Tag.add(app, key, val) for key, val in tags.items()]
app.synth()
