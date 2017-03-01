# -*- coding: utf-8 -*-

import shutil

from lektor.publisher import Publisher
from lektor.pluginsystem import Plugin


class CpPlugin(Plugin):
    name = u'cp'
    description = u'Adds cp as a deploy target. Use cp://<path> to deploy to a path.'

    def on_setup_env(self, **extra):
        # Modern Lektor stores publishers in env
        if hasattr(self.env, 'publishers'):
            self.env.publishers['cp'] = CpPublisher
        # Older versions stored publishers in a global
        else:
            from lektor.publisher import publishers
            publishers['cp'] = CpPublisher


class CpPublisher(Publisher):
    def publish(self, target_url, credentials=None, server_info=None, **extra):
        shutil.copytree(self.output_path, target_url.path)
        yield "success"
