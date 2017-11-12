/*
 * View model for OctoPrint-Klipper
 *
 * Author: Bradley Muller
 * License: AGPLv3
 */
$(function() {
    function KlipperViewModel(parameters) {
        var self = this;
        console.log("Klipper Created")
        // assign the injected parameters, e.g.:
        self.loginState = parameters[0];
        // self.settingsViewModel = parameters[1];

        // TODO: Implement your plugin's view model here.
        self.onDataUpdaterPluginMessage = function(plugin, data) {
          if (plugin != "klipper") {
  				 console.log('Ignoring '+plugin);
              return;
          }

    			if(data.type == "popup") {
    				 console.log(data.msg);
    				$("#klipper").text(data.msg);
    			}
    		}
    }

    // view model class, parameters for constructor, container to bind to
    OCTOPRINT_VIEWMODELS.push([
        KlipperViewModel,

        // e.g. loginStateViewModel, settingsViewModel, ...
        [ "loginStateViewModel"/*, "settingsViewModel" */ ],

        // e.g. #settings_plugin_klipper, #tab_plugin_klipper, ...
        [ #klipperMenu ]
    ]);
});
