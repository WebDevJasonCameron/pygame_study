# Log

## 2022 11 26 | Sprite Problems

I was having the worst time with the graphic portion of the tut. Amazingly, I wasn't alone. I found a comment by Antoine THERY > > Hey !
So im a mac user and i got stuck during the graphic part of the video (around 1:50:00), the probleme was that i was getting the worng sprites for the objects (getting statues instead of trees, etc.).
After a bit of testing i undestood that the Mac os walk function doesnt "walk" throught the directory in the correct order so the list we're creating(image_surf) is unsorted.
If u're struggling with the same issue, define a new list to get every images from the walk function, then sort it and iterate angain throught the sorted list.

def import_folder(path):
surface_list = []
sorted_list = []

    for _, __, img_files in walk(path):
        for image in img_files:
            sorted_list.append(image)
        sorted_list.sort()
        for img in sorted_list:
            full_path = path + "/" + img
            image_surf = pygame.image.load(full_path).convert_alpha()
            surface_list.append(image_surf)

It works now, i can keep enjoying your tutorial :) < <

## 2022 11 24 | Happy Thanksgiving

Hey all, Happy Thanksgiving. I am thankful that I can get so much done on this day. I asked work to let me do nine hours every day for two weeks so I could take every other Friday to study code and build cool stuff. That's 81 hours in two weeks, plus another 12 hours of study time on those Fridays. I thought that would be a great deal cause everyone wins (I work as a Jr. Software Engineer). The offer wasn't accepted so I am loving this time to learn more Python, build fun stuff, and really flex those creative programming skills. Hopefully I can get through a lot of the courses before Monday! I already have plans to get out of tutorial purgatory and challenge myself with the things I am learning. Until then, have a wonderful holiday and don't eat too much!!! ~Cheers

## 2022 11 21 | Near Complete

I'm at the stage that I can add sound to this first "game" intro tut. Afterwards, I need to provide examples to the readme. Then I want to mod it with some different graphics to make it feel like it is my own. Not that I can pass the code as my own... or really the artwork. I just want to go through the follow-along-code to see if I can understand it. Next, I will try to go through the long Zelda-like pygame tut. That will probably take me a really long time. Still... it is fun and I don't get to do much fun stuff at work. However, that is a different story for another place. ~Cheers

## 2022 11 13 | Update

Continuing the tutorial between work and life. I am currently stuck on a bug where anim fails. I added the movement anim to the player. This includes the walk and jump. These are suppose to trigger as the start of the game begins. If the character is above the y axis of 300, then the single frame jump triggers. Gravity does the rest. The problem I get is that the "tuple doesn't have a 'y' instance." (something like that) If I comment out line 149, it goes on the cause more problems. What I need to do is watch the tut again and see if I missed something. Right now, I'm trying to look at the logic to understand why the error is saying what it says. Finally, the code the instructor gives is based on the final product. This means, things do not look like they would at part 3hours and 21 minutes into the video. Instead I have a fully working product or a working product with commented out code representing different point in tut time. Both are great and I'm not complaining. I'm just pointing out that one needs to still dig into their own broken code... that makes you stronger as a programmer!

---

## 2022 11 08 | Fleshed

Revised the repo format. Changed this doc to "log" and created a "RM" for visitors. I hope they like the extra love I put into the presentation! Despite that, I'm nearing the completion of the the first tut. It has been very rewarding... even though I am dead tired when I get home. As with all repos, I really hope this isn't a waist of time. I know I've already learned so much. I just haven't recorded that within the logs.

---

## 2022 10 28 | Init

Following some tuts in YT. Let's see how much time I can give this side side side project!
