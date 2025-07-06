# Changelog of Reactive Factions Retribution

## Backlog

- TODO: RepHits for more events like e.g. destroying assets //vary on community feedback, or as new mod e.g. credits and rewards for activities or dynamic events/missions (if is it possible). - Rewards system, accumulating CR & Rep per faction for these activities and pay if randomized threshold CR+Rep is accumulated with fancy/gift message. New Mod Menu for this. Enemies should be excluded (enemy should not send gifts of CR+Rep to the player) like in the main functionality.
- TODO: Political lobbying e.g. change relation X and Y, Player and X etc. for credits/rep/assets/law etc. Send envoy delegation or via new black market NPC ?  //vary on community feedback
- TODO: More RPG tiers //vary on community feedback
- TODO: KD Menu API integration adding new features and moving existing there. // or some new system provided by Egosoft from 7.0 to 8.0? https://wiki.egosoft.com:1337/X4%20Foundations%20Wiki/Modding%20Support/Breaking%20Changes/
- TODO: Adding enum for `tag.reactivefaction` property manually via injection - if possible + Feature to toggle different tags via mod menu so user can decide which actions impact the bonuses/penalties.
- TODO: Changeable evaluation cooldown values in the mod menu + **stacking rep bonuses/penalties and applying them to the evaluation event instead of instantly.**
- TODO: Button to trigger evaluation manually.

<<<<<<< HEAD
## 2.4.0 - 2.4.2 - Support Update & Fixes
- **Fixed** expection from math log function.
=======
## 2.4.0 - 2.4.1 - Support Update & Fixes
>>>>>>> b0d9068 (2.4.1 fix for 2.4.0)
- **Fixed** wrongly set relation reason in set_faction_relation. Changed to reason="relationchangereason.smalltalkreward" instead of "tag.smalltalkreward" which wasn't working correctly.
- **Fixed** event sometimes failed to trigger correctly on relation changes.
- **Fixed** missing tags — now fully excludes the smalltalkreward tag from the relation‐changed event.
- **Improved** checkinterval cue now uses a separate cooldown variable ($NextPossibleCheckTime) to decouple polling frequency (6 min) from the 25 min cooldown.
- **Tested** compatibility with X4: Foundations 7.6.0
- **Changed** Experimental and Relative amplitudes are now ON by default. Those provide changes being more smooth and less arcady. User may turn them off in Extension Options menu provided by [Mod Support APIs](https://www.nexusmods.com/x4foundations/mods/1699).

## 2.2.8 - 2.3.4 Localization & Fixes

- **Added** specific localizations for the mod. [You can contribute to improving the translation if you are an advanced or native speaker of any language](https://github.com/iomatix/Reactive-Factions-Retribution-X4Foundations/tree/main/t).
- **Improved** exception handling for the `tag.reactivefaction` property. The tag feature may still not work as intended if the issue was not addressed by Ego.
- **Fixed** an issue within the FactionFilter library that caused a null pointer exception.
- **Added** a missing bracket that caused another exception.
- **(2.2.9) Hot-fix**, Fixed another issue connected to the typo within the codebase.
- **(2.3.0) Mandatory-fix**, Reworked FactionFilter library to avoid iterating on removed values.
- **(2.3.1) Mandatory-fix**, Applied fix for the lock options.
- **(2.3.1) Minor-fix**, Fixed exceptions from the mod menu implementation.
- **(2.3.2) Minor-fix**, Attempt to handle the non-critical exception related to the ListofCooldowns variable. If the issue persists, it should not impact performance or functionality but will only log a warning: `Property lookup failed`.
- **(2.3.3) Patch**, `tag.reactivefaction` has been changed `tag.smalltalkreward` to make it working as intended. According to the tag lookup documentation, "Tag of the given name (tag is created if it doesn't exist)," the tag should be created automatically but is not currently in 7.50. This means that tag.smalltalkreward will not impact reputation changes made by the mod while this patch is applied.
- **(2.3.4) Patch**, Improved Cr formatting of info display within mod menu.

## 2.2.6 & 2.2.7 Yaki Lock and the faction filter

- (2.2.6) Added Yaki lock option to the mod's menu UI. You may want to turn it on during the Yaki storyline to prevent losing reputation with the Yaki faction.
- (2.2.6) Changed the check interval of the main method from debug 90 seconds back to immersive 25 minutes.
- (2.2.6) Added Yaki to the faction filter.
- (2.2.6) SCA and Yaki are removed from the faction filter if their lock is turned off within the mod menu.
- (2.2.7) Hot-fix, connected language entries to the mod's menu for Yaki Lock to provide correct localization support.

## 2.2.5 User Info

- Added information display to the mod menu.

## 2.2.4 Log Writes

- Added missing in-game logging functionality. Note that the logs are not displayed using the UI game values currently but raw values instead.

## 2.2.3 Fix

- Fixed an issue which stopped applying bonuses and penalties for the rep change event.

## 2.2.2 Update

- Patched an issue where the mod was not automatically refreshing players' asset calculations.

## 2.2.1 Your X Game - Your Rules

- Further improvements to the mod menus, and other related features that are not yet implemented in the mod menu for this update.
- API Menu and its elements have the possibility to be dynamic. Implemented this for most settings improving settings customization and accessibility.
- Most of the mod settings may be change dynamically without further limitations, bending the experience provided by Reactive Factions Retribution to individual players needs.

## 2.2.0 for X4 7.0

- SCA Reputation Lock is now enabled by default.
- Optimized memory usage for cues.
- Set all default cooldown values to 0 seconds.
- Added more customizable approximate values for CR at each power level in the mod menu.
- Increased Asset Modifiers mod menu slider cap from 100% to 350%.
- Excluded visitor factions from the mod.
- Changed default cooldown values to 0 seconds.
- Improved logic, added a cue cancel event, and allowed cooldowns to be set to a true 0 seconds without triggering avalanche syndrome.
- Implemented custom tag name relationchangereason.reactivefaction and added functionality to cancel cues for instances of cues. Note: The X4 mechanism for creating new enums is currently malfunctioning so it will be null instead at the moment.
- Mod Menu has been reworked on the backend.
- The bug with missing event faction check against the ignore list, which could potentially cause issues has been fixed.
- From now player's enemy faction can not take part in the mod's main event. Helping the enemy is assumed as accidental by default, so if you are e.g. helping Xenons by killing your foes next to their stations, it is assumed as accidental and will no longer destroy the reputation of every faction.
- Full support for custom factions is provided with this update.

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
