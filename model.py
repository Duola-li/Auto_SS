#coding:utf-8
'''
莫名其妙秒，configs要配置两个才能用，否则就失效
'''
model = '''{
  "configs": [
    {
      "server": "%s",
      "server_port": %s,
      "password": "%s",
      "method": "%s",
      "plugin": "",
      "plugin_opts": "",
      "plugin_args": "",
      "remarks": "",
      "timeout": 5
    },
    {
      "server": "%s",
      "server_port": %s,
      "password": "%s",
      "method": "%s",
      "plugin": "",
      "plugin_opts": "",
      "plugin_args": "",
      "remarks": "",
      "timeout": 5
    }
  ],
  "strategy": null,
  "index": 1,
  "global": false,
  "enabled": true,
  "shareOverLan": false,
  "isDefault": false,
  "localPort": 1080,
  "pacUrl": null,
  "useOnlinePac": false,
  "secureLocalPac": true,
  "availabilityStatistics": false,
  "autoCheckUpdate": true,
  "checkPreRelease": false,
  "isVerboseLogging": false,
  "logViewer": {
    "topMost": false,
    "wrapText": false,
    "toolbarShown": false,
    "Font": "Consolas, 8pt",
    "BackgroundColor": "Black",
    "TextColor": "White"
  },
  "proxy": {
    "useProxy": false,
    "proxyType": 0,
    "proxyServer": "",
    "proxyPort": 0,
    "proxyTimeout": 3
  },
  "hotkey": {
    "SwitchSystemProxy": "",
    "SwitchSystemProxyMode": "",
    "SwitchAllowLan": "",
    "ShowLogs": "",
    "ServerMoveUp": "",
    "ServerMoveDown": ""
  }
}
'''
