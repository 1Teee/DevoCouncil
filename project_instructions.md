## P00: ~~Half-Quick~~ Move Slowly and Fix Things
### Due: TBD

~~_Imagine:_~~

~~_Your team advertises proficiency with Flask, Python, and SQLite.~~
~~Your team has been contracted to design and implement a newfangled webapp called a "wiki."_~~


_Imagine one of these scenarios:_

__Scenario One:__ Your team has been contracted to create a collaborative storytelling game/website, with the following features:
- Users will have to register to use the site.
- Logged-in users can either start a new story or add to an existing story.
- When adding to a story,
  - Users are shown only the latest update to the story, not the whole thing.
  - A user can then add some amount of text to the story.
- Once a user has added to a story, they cannot add to it again.
- When creating a new story,
  - Users get to start with any amount of text and give the story a title.
  - Logged in users will be able to read any story they have contributed to on their homepage (the landing page after login).

__Scenario Two:__ Your team has been contracted to create a we<b>b log</b> hosting site, with the following features:
- Users will have to register to use the site.
- A logged-in user will be able to
  - Create a new blog
  - Update their blog by adding a new entry
  - View and edit their own past entries
  - View the blogs of other users

----- 

Your "software solution," to use the parlance of our times, will incorporate a few distinct components, so it is imperative that your team develop a design before taking any further steps.
<br>
<br>
Your team's first order of business is reaching agreement as to how your project will be organized and how you will divide work. It will be imperative that each teammate a) shares the same organizational model of your target, and b) <br>
understands how they and their work will fit into it.
<br>
<br>
Enter the _design document_. Design by next class session.
<br>
<br>
(___Nota bene:___ _This is your only deliverable for next class. All your efforts should be directed to doing this job well._)

### Design Document Specifications:
- A *list* of program components with role of each specified. (e.g., a car engine is comprised of various components: carburetor, alternator, radiator, spark plugs, etc. Each must perform its role for the engine to do its overall job.)
- Explanation of how each component relates to the others.
  - Component map visualizing relationships between components.
- Database Organization (tables? Relationships b/t tables? etc.)
- Site map for front end
  - Represent each page you envision for your site.
  - Show linkages conveying all possilbe pathways for a user traversing site.
- A breakdown of the different tasks required to complete this project
  - Include assignments of each task to each group member
- Append this line to your heading: **`TARGET SHIP DATE: {yyyy-mm-dd}`**
- Amalgamate these components into a single PDF, store in designated location.

### Project Guidelines:
* Flask will serve as your web server/delivery framework.
* SQLite3 will serve as your backend data storage system.
  - As you grown your "sql-fu", always start with Devo Knowledge Base (QAF, n&c) and primary documentation. (...and if none of these have the answer you seek, and you find a SO post that is actually useful, or any other diamond in the rough of the Intertrash, add it to Devo KB)
  - Get creative, think boldly, get your hands dirty as you experiment via the sqlite3 shell and see what works/sticks...
* Multiple Python files should be used, as necessary, for application layer. (_a.k.a._ "middleware" modules, etc.)
* CSS: You may provide your own IFF...
  - your site is fully functional with CSS is stripped away.
  - you store it in the appropriate location for flask to use it.
  - it is all written by you
* Use Q&A forum liberally. *"A rising tide lifts all boats."*
* _Reminder:_ include heading as comment in all source files.
* Platinum Rule: __THOUST APP SHALT NOT FAIL.__

Your website will incorporate a few distinct components, so it is imperative that your team develop a design and agree upon roles ___before___ you move to implementation.

----- 

You will need a DEVLOG for this project.
* Devlog allows any group member at any time to see the current state of the project.
* PM will make sure devlog is being maintained, but will not make all entries.
* The devlog should be a plain text file, stored in the specified location.
* When any team member stops working and pushes changes to github, they should update the devlog explaining what changes have been made. Include errors/bugs discovered (or created).
* Separate devlog entries with a newline.
* Most recent entry at the bottom.
* Each entry should begin with the following format: `firstL -- TIMESTAMP\n` ( _e.g._: `topherM -- 1999-12-31 23:59` )

----- 

### FINAL DELIVERABLES (watch this section for updates):

* hardcopy:
  * final version of design doc (x1)
  * staple because it indicates "you have it together"
* repo structure:
```
app/
    __init__.py
    static/
        css/          ( O P T I O N A L )
    templates/
design.pdf
devlog.txt
flag.jpg
README.md
requirements.txt
```
* `README.md`
  * Clearly visible at top: __\<Project Name\> by \<Team Name\>__
  * Roster with roles
  * Description of website/app (a la abstract of a scientific paper... NOT your entire design doc!)
  * Launch codes:
    * How to clone/install.
    * How to run.
* `design.pdf`
  * Latest/current version of your design document.
  * Revisions since v0 noted/explained in devlog.
* `requirements.txt`
  * It will list flask as well as any other pip installs your app requires.
  * Latest version of all packages.
  * Clearance must be sought and granted for any modules/libraries not explicitly covered in class.

----- 

### Subgoals / Checkpoint Deliverables:

1. `R 2024-10-24 08:00`
  * submodule linked
  * team registered
  * deposit hardcopy of design doc (3x) on lisadesk at beginning of pd
  * writing utensils of multiple non-blue/black hues
1. `F 2024-10-25 08:00`
  * revised design document
  * summary of design doc changes in devlog
  * readme heading

----- 

related:
<br>
[dumpster fires are best avoided](https://www.ftc.gov/system/files/documents/public_statements/1536911/chopra_dissenting_statement_on_facebook_7-24-19.pdf)
<br>
[tk](https://)

