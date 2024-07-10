# Changelog of Reactive Factions Retribution 


## Backlog
- TODO: Rep changes for more events like e.g. destroying assets
- TODO: Political lobbing e.g. change relation X and Y, Player and X etc. for credits/rep/assets/law etc.  //vary on community feedback
- TODO: More RPG tiers //vary on community feedback

## 2.2.0 for X4 7.0

- SCA Reputation Lock is now set back to true by default.
- Optimized memory usage for cues.
- Default MainFactionCooldown changed to 5 seconds.
- Customizable approximate values for CR at each power level in the mod menu.
- Unlocked DefaultAssetModifier the mod menu slider's cap from 100% up to 350%.
- (Experimental) Cooldowns can now be set to a real value of 0 seconds.
- TODO: Bugfix (to be confirmed in tests) for missing event faction check against ignore list, potentially causing issues.
- TODO: Fixes to the event logics, custom trigger name e.g. repchange_reactivefactions and canceling cues for instances of repchange_reactivefactions (avalanche syndrome to be avoided if cooldown may eq 0).

## 2.1.0 for X4 6.0

- Corrected language file typos.
- SCA Reputation Lock is now set to false by default.
- Added SCA to FactionFilter.
- Notifications will now appear only for significant relation changes by default.
- Fixed Suspend Notifications functionality.
- Added Detailed Notifications checkbox to enable all notifications.
- Default UIRelationDivisor set to 3.
- Reimplemented Maximum Amplitude algorithm.
- Implemented Experimental Amplitude.
- Implemented Relative Amplitude.
