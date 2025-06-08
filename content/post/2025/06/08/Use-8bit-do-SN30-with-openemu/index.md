---
author: Centurio
title: "Use 8bitDo SN30 Pro With OpenEmu"
date: 2025-06-08T20:53:25+02:00
categories:
- macOS
tags:
- openEmu
---
# Introduction
I've bought two [8bitDo SN30 Pro](https://www.8bitdo.com/sn30-pro-g-classic-or-sn30-pro-sn/) Gamepads. They look and feel like the original SNES gamepads and are considered to be good quality. I already used them on my AppleTV as well as on my Macbook in combination with OpenEmu, but recently they stopped working. Bluetooth connectivity was given and the controllers were paired and could be identified.

# The problem
While the system showed them as connected, OpenEmu showed them as well but was unable to properly map controller buttons. This seems to be a known issue for [many years](https://www.reddit.com/r/OpenEmu/comments/ighvwu/8bitdo_controller_not_working_with_openemu_2091/).

# The solution
It is possible to pair the Gamepads in different modes. The one I've used seem to be the Nintendo Switch compatible mode, since they appeared as Nintendo Switch controllers. But when they are turned of and are powered on by using START and X, they can be paired and are recognized correctly. Also the battery levels are now properly reported and OpenEmu was able to map buttons.

# Conclusion
These controllers are good. You just have to know about all their possible supported options and modes. In this case I'm using now the Windows mode, while I was using Switch mode before. The possible combinations are also documented [here](https://manuals.plus/8bitdo/8bitdo-sn30-pro-sf30-pro-user-manual#bluetooth_connection). 