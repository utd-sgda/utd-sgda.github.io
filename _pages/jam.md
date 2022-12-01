---
permalink: /jams/
title: Jams
Description: Here are the winners of our previous game jam!
---

{% for jam in site.data.jams %}
<div id="{{ jam.title | slugify }}" class="text-center mt-8">
    <a class="mx-auto display-block w-full lg:w-3/5" href="{{ jam.link }}" target="#">
       <img class="card-{{ jam.color }} border-radius-md overflow-hidden" src="/assets/images/posters/{{ jam.poster }}" alt="This is a poster of the jam's winners. Please look below for that information typed out!">
    </a>
</div>

<h1 class="mb-0"> {{ jam.title }} </h1>

<h2 class="mt-0 font-normal" style="text-transform: none;"> {{ jam.date }} </h2>

<div class="mt-8 mb-12 grid has-1-columns lg:has-2-columns justify-items-center row-gap-45">
{% for game in jam.games %}
    <a id="{{ game.name | slugify }}" class="h-color card p-4 lg:p-8 text-center" href="{{ game.link }}" target="#" style="width: 90%;">
        <h1 class="mt-0" style="text-transform: none; line-height: 1;"> {{ game.name }} </h1>
        <h2 class="mt-0 c-white font-normal" style="text-transform: none; line-height: 1;"> {{ game.categories }} </h2>
    {% if game.members.size > 1 %}
        <div class="mt-4 grid has-1-columns lg:has-2-columns justify-items-center row-gap-5">
    {% else %}
        <div class="mt-4 grid has-1-columns justify-items-center row-gap-5">
    {% endif %}
        {% for member in game.members %}
            <p class="c-white my-0"> {{ member.name }} </p>
        {% endfor%}
        </div>
    </a>
{% endfor %}
</div>
<hr>
{% endfor %}