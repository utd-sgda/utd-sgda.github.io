---
permalink: /events/
title: Events
Description: Here is information about our next event!
---

{% include title-animated.html text="Next Event" %}

{% unless site.data.events.show-next-event %}
# To Be Announced

Throughout the Fall and Spring semesters, we generally have meetings every *Wednesday* at *7pm*. Check back here for information once our next event has been announced, or get notifications from the `#announcement` channel on our discord.

<p class="p-1"></p>

<div class="text-center"><a class="button" href="/discord"> <i class="icon-discord" aria-hidden="true"></i> Join our Discord </a></div>

<p class="p-1 lg:p-4"></p>

{% else %}
{% include poster.html image=site.data.events.poster color=site.data.events.color %}

<p class="p-1 lg:p-4"></p>

<div class="text-center"><a class="button" href="/discord"> <i class="icon-discord" aria-hidden="true"></i> Join our Discord </a></div>

<p class="p-1 lg:p-4"></p>

---

# {{ site.data.events.title }}

## When

{{ site.data.events.when }}

## Where

{{ site.data.events.where }}

## What

{{ site.data.events.what }}

<div class="pt-12"></div>
{% endunless %}

{% comment %}
<!-- # When

Kick Off: **03/09/2022**  
Due Date: **03/20/2022**  
Wrap Up: **03/23/2022**

# Where

SPN 2.220 2nd Floor (**Makerspace**)

[Room Locator](https://map.concept3d.com/?id=1772#!m/550572)

[Google Maps](https://www.google.com/maps/place/UTDesign+Makerspace/@32.9935207,-96.7521344,17z/data=!3m1!4b1!4m5!3m4!1s0x864c2206dfe20ddb:0x1906acd349077109!8m2!3d32.9935207!4d-96.7521344)

---

# Rules

1. To participate one must be:
   1. A current college student (exceptions may occur if first approved by an SGDA officer)
   2. A member of the SGDA Discord server (utdsgda.club/discord)
   3. Registered for the jam here. 

2. Games must be submitted by 11:59 pm on Mar 20, 2022 to our itch.io page to be judged and in the running for prize consideration. Exceptions may occur to the 11:59 pm deadline on a case by case basis if actively communicated with an SGDA officer.

3. Game submission rules
   1. No NSFW content
   2. Games must have been made during the period of the jam.
   3. Games must be developed only by those on a registered team.
   
4. Premade assets
   1. Free assets that are publicly available to everyone at the time of the jam can be used. No assets may be used that, at the time of the jam, cost money to obtain.
   2. The use of assets previously made by participants is discouraged. 
   3. Any assets used that are not developed by the team, must be credited on the team’s itch.io submission page. Additionally, crediting assets within the game submission itself is encouraged.
   4. Definition of an asset may include but not limited to: 3D models, animations, music, sound effects, code, art, Unity or Unreal asset packs, etc.

5. Any game engine is allowed to develop a jam submission. These may include Unity, Unreal, Gamemaker, RPG Maker, etc. Additional software to aid with development is allowed as well, such as Maya, Blender, Wwise, Reaper, Photoshop, etc.

6. Final submissions must be either a zipped folder that includes a game build for Windows or a WebGL build that runs directly in itch.io. Other builds for other platforms may also be uploaded to a team’s itch page if they so choose.

7. Teams
   1. Max size of a team is 5 participants
   2. All members of the team must be valid participants, each of which has officially registered for the jam.
   3. If at any time there are conflicts between team members, an SGDA officer may be contacted to help resolve the matter. The SGDA officer then has the right to split teams, remove members from the team, or even remove participants from the jam if they deem fit.
   4. If someone joins the jam late and a team is willing to accept a new member that would not exceed the 5 person limit, the team can add the new participant to their team if they communicate with an SGDA Officer first.

<div class="pt-12"> -->
{% endcomment %}