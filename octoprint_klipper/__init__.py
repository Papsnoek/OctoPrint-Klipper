# coding=utf-8
from __future__ import absolute_import

### (Don't forget to remove me)
# This is a basic skeleton for your plugin's __init__.py. You probably want to adjust the class name of your plugin
# as well as the plugin mixins it's subclassing from. This is really just a basic skeleton to get you started,
# defining your plugin as a template plugin, settings and asset plugin. Feel free to add or remove mixins
# as necessary.
#
# Take a look at the documentation on what other plugin mixins are available.

import octoprint.plugin

class KlipperPlugin(octoprint.plugin.SettingsPlugin,
                    octoprint.plugin.AssetPlugin,
                    octoprint.plugin.TemplatePlugin):

    def handle_endstop(self, comm, line, *args, **kwargs):
        self._logger.info(line)
        if "x:" not in line:
            return line

        if "TRIGGER" not in line or "open" not in line:
            return line

        self._plugin_manager.send_plugin_message(self._identifier, dict(type="popup", msg=line))
        return line

	##~~ SettingsPlugin mixin
	def get_settings_defaults(self):
		return dict(
			# put your plugin's default settings here
		)

	##~~ AssetPlugin mixin
	def get_assets(self):
		# Define your plugin's asset files to automatically include in the
		# core UI here.
		return dict(
			js=["js/klipper.js"],
			css=["css/klipper.css"],
			less=["less/klipper.less"]
		)


# If you want your plugin to be registered within OctoPrint under a different name than what you defined in setup.py
# ("OctoPrint-PluginSkeleton"), you may define that here. Same goes for the other metadata derived from setup.py that
# can be overwritten via __plugin_xyz__ control properties. See the documentation for that.
__plugin_name__ = "Klipper Plugin"

def __plugin_load__():
	global __plugin_implementation__
	__plugin_implementation__ = KlipperPlugin()

	global __plugin_hooks__
	__plugin_hooks__ = {
        "octoprint.comm.protocol.gcode.received": __plugin_implementation__.handle_endstop
	}
