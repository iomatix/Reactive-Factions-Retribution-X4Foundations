# Changelog of Reactive Factions Retribution

## Backlog

- TODO: RepHits for more events like e.g. destroying assets //vary on community feedback, or as new mod e.g. credits and rewards for activities or dynamic events/missions (if is it possible). - Rewards system, accumulating CR & Rep per faction for these activities and pay if randomized threshold CR+Rep is accumulated with fancy/gift message. New Mod Menu for this. Enemies should be excluded (enemy should not send gifts of CR+Rep to the player) like in main functionality.
- TODO: Political lobbing e.g. change relation X and Y, Player and X etc. for credits/rep/assets/law etc. Send envoy delegation or via new black market NPC ?  //vary on community feedback
- TODO: More RPG tiers //vary on community feedback
- TODO: KD Menu API integration adding new features and moving existing there.

## 2.2.0 for X4 7.0

- SCA Reputation Lock is now enabled by default.
- Optimized memory usage for cues.
- Set all default cooldown values to 0 seconds.
- Added customizable approximate values for CR at each power level in the mod menu.
- Increased Asset Modifiers mod menu slider cap from 100% to 350%.
- Excluded visitor factions from the mod.
- Changed default cooldown values to 0 seconds.
- Improved logic, added a cue cancel event, and allowed cooldowns to be set to a true 0 seconds without triggering avalanche syndrome.
- Implemented custom tag name relationchangereason.reactivefaction and added functionality to cancel cues for instances of cues. Note: The X4 mechanism for creating new enums is currently malfunctioning so it will be null instead at the moment.
- TODO: Confirm bug and fix it. Bug regards probably missing event faction check against the ignore list, which could potentially cause issues. Fix which should prevent this sus situation: Optional setting "ExcludeEnemies" to exclude all enemy factions to the player faction from being possible MainFactions. Disables helping enemies logic assuming these accidental until Enemy status between factions is hold.

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
