sors workshop today i want to discuss with you
0:11
the single most important element or factor in programming
0:17
programmable logic controllers no matter what the brand is almost no matter what the application is
0:24
and if you don't agree with this then um i'm not saying bad to you i'm just
0:30
saying you shouldn't waste your time watching the rest of this video the number one factor is
0:37
the maximum number of good parts components products
0:42
out the door from the manufacturer's facility remember that the plc was created
0:50
to facilitate faster upgrades in the process to manufacture
0:57
parts it was also created to facilitate quicker troubleshooting
1:04
for the technicians and electricians so if you don't agree that good parts out the door
1:11
is not the most important factor of programmable logic controllers
1:16
uh really got no business being in this business i know that sounds like i'm being high and mighty or self-righteous
1:23
but i'm not the goal is products out the door and that means less downtime
1:31
less downtime means that the systems can be trouble shot
1:36
quicker and put back into production as quick as possible
1:42
and it's not just a matter of the people that are available to troubleshoot which most of them the the good ones are
1:50
really electricians who have picked up the skill of troubleshooting the processes with
1:58
online monitoring of the plc so it's not about how well you wrote the code necessarily
2:05
what code you use what language you use it all has to do is with how quickly
2:11
can you determine what's wrong with the system and get it fixed and 99 times out of 100
2:17
or 999 times out of a thousand it's a sensor that's broken a sensor
2:23
that's been come loose it's a cylinder that's sticking and not making it to the end of
2:29
stroke quick enough all these things are found by monitoring the program in the plc so all boils down
2:38
to how easy is it to monitor the program
2:44
so let's jump in and start looking at some of this
2:49
how did the plc happen general motors around 1968 actually
2:55
started before then but 1968 is the date that they throw down in history
3:01
and that was when dick morley and a group of engineers working at general motors were
3:06
dealing with the changeover that they had to go through every model
3:12
year so general motors back then they tended to change the sheet metal
3:17
and the features on vehicles more quickly in other words every year
3:23
they try to come out with something that look different look cooler look better than all the rest these changes in the manufacturing
3:29
because the parts changed the sheet metal changed everything changed they had to completely reprogram the
3:34
control systems and back then they were all relays and without laboring into that
3:41
and talking about that we'll just keep this simple so before the plc control logic for
3:46
manufacturing was mainly composed of relays cam timers and drum sequencers
3:52
and some dedicated closed loop controllers that might have been controlling temperature or speeds or
3:57
something and the hardwired nature of it made it difficult for design engineers to alter
4:03
the automation process changes would require rewiring and careful updating of the documentation insane all by itself
4:11
often the technicians at general motors would spend hours troubleshooting by examining schematics and comparing them
4:17
to existing wiring now you've got to put yourself in that mindset back then it's very difficult to do where you're
4:23
looking at a set of prints you don't even know if the panel is wired that way someone could have come in and moved a
4:28
few wires around to correct the problem and not updated the print is bad news when general purpose computers became
4:35
available they were soon applied to control logics and industrial processes
4:40
however these early computers were unreliable not industrially hardened and required very special programmers now
4:48
morley's genius when he came up with a plc was to incorporate ladder logic into
4:53
his system ladder logic is essentially a graphic representation of boolean logic
4:59
this was the game changer the engineers would find it easier to understand and use than they would boolean logic and so
5:07
the first plc's provided several advantages over earlier automation systems
5:13
the plc would tolerate the industrial environment better than computers and was more reliable
5:19
compact and required less maintenance than the relay systems it was also
5:25
extensible with additional i o modules you didn't have to put in more relays you just added more i o modules so this
5:32
allowed for easier iteration over manufacturing process design with simple
5:37
programming language focused on logic and switching operations it was
5:42
more user friendly than computers using general purpose programming languages
5:48
it also permitted its operation to be monitored they could go in and monitor the logic early plc's
5:55
were programmed in ladder logic which strongly resembled a schematic diagram
6:00
of relay logic this program notation was chosen to reduce training demands for
6:06
existing technicians it turned out to be a lot more than that you're probably some of you are thinking that i'm an old
6:13
geezer and i just kind of passed my the pinnacle of my career and understanding
6:19
of what's going on before structured text became available to program a plc
6:25
with well let me straighten you out on that right away i learned fortran which
6:30
was a general purpose compiled imperative programming language before plc's even existed my first language was
6:38
fortran and fortran if you look at an example here and it's hard to find any examples for industrial
6:45
control but if you see it is a structured text now a lot of people want to argue what
6:51
structure text is is or not but saying that this is not structured checks would
6:56
be like somebody who says who drives a a say a camaro says that if you're driving an impala
7:03
that's not really a chevrolet you got to be driving a corvette or a camaro otherwise you're not driving to
7:09
chevrolet well folks this is structured text and after fortran
7:15
then i started using basic and basic went through quite a number of
7:20
improvements in his toolbox and everything else and then moved to c
7:26
now this language c looks more like modern structured text
7:32
than basic or fortran nonetheless these are structure text languages
7:39
okay so i don't have a dog in this fight so to
7:45
speak i learned structured text long before i ever heard of a plc
7:52
my i was writing programs in text-based language and um i never even saw ladder logic
8:00
for a plc until long after i was doing lots of control engineering i wasn't
8:05
really programming pocs i was doing the uh the electrical design you know which
8:10
used a lot of relays and timers and drum sequencers what have you so i kind
8:16
of went through the full iteration of you know what's led up to now
8:21
and let me ask you a question real simple question you've heard it said
8:27
that a picture tells a thousand words okay so let's say i took a photograph
8:35
didn't show it to you and in that photograph there were a number of objects that you would quickly
8:42
recognize including the colors and the brands and the gender
8:49
one story two story woods in the back beach in the back etc so let's say i took a photograph and
8:55
wrote a thousand words and i put those thousand words in front of you
9:01
sat it down in front of you and nicely written and laid out not trying to trick you
9:06
and then said what color is the car in the image
9:12
how long do you think you would have to read before you found the color of the car and you
9:18
couldn't just look for the word car you would have to see the word the noun car
9:24
with adjectives after it or before it to see that it's a red car but if i showed you the photograph
9:31
how quickly could you tell me what color the car was unless there's something wrong with you
9:37
probably in less than one second you look at say oh it's a red car and then if i went back to the text and said
9:45
now now that you've seen the photograph you've taken in that image my point is a picture tells a thousand
9:51
words and any graphic language beats text based language hands down for
9:57
how quickly you can analyze it and read it but there's more to that let's look
10:03
what i have here in front of me is i've opened a project in connected
10:08
components workbench i picked this software package to do the demonstration with because it has a simulator so i
10:15
don't need any hardware now i own all but one of the
10:21
family of micro 800 controllers it's not my favorite but it's becoming
10:26
more popular so i decided to use it typically i write most of my projects in
10:32
rslogix studio 5000 logic designer for compact logics with panel views variable
10:38
frequencies drive servo control and everything so what i have here are some program files where i have the same
10:46
logic in both structure text and in ladder logic diagrams so let's look at
10:51
the most obvious one and that would be the if then else i'm really addressing this more to people who
10:58
program in structured text then i am people who program a ladder logic diagram
11:03
and are considering learning structured text and i certainly encourage everyone to learn everything
11:10
you can but this is something you need to strongly think about the most important thing in manufacturing regarding plc
11:17
programming is how quickly it can be trouble shot and put back into production making money there are a lot
11:23
of machines showing up now out in the industry that have structured text for
11:28
the main sequential functions of the machine and the machine breaks down say
11:34
three four months after it was delivered it's commissioned uh the company has paid the machine builder
11:40
and they're long gone and then something happens at three o'clock the morning maintenance guy goes out there and he
11:45
opens up ccw or whatever program he's got and he opens up the program and he sees structured text well
11:52
even if he can read structured text there's there's some other issues of whether or not you
11:58
can monitor it while it's running if you're a structured text guy i'm encouraging you to learn lander
12:04
logic diagram as fast and quickly as you can because once the manufacturers the
12:10
people who purchase these machines start realizing that machines that show up with structured texts are going to
12:16
cause them a problem because the maintenance guys can't troubleshoot it or even if they can't it's slower to
12:22
troubleshoot they're going to start telling companies not to send machines
12:28
with structured text now using structured checks for little routines for math
12:33
and maybe some loop control or something that's great but for the main sequence of the program no so they're going to
12:40
start refusing machine builders now i realize what's going on with machine builders there's not enough controls
12:46
engineers to go around so they're taking people right out of school that have no
12:51
electrical background no industrial control background but can write structured text because you can write
12:57
this structure text in ide right in a arduino or a pie raspberry pi and then
13:05
pour it over that doesn't address the fact that it's harder to troubleshoot and there aren't many
13:12
people to troubleshoot it so the machine builders are between a rock and a hard place they can't deliver the equipment because
13:18
they can't find controls engineers that can write ladder logic because that's what the
13:24
companies want that are buying the machine because that's what's going to get them back up into production the
13:29
fastest fastest when something breaks down the field okay enough we look at the strain and so y'all are the writing
13:36
structure text and not ladder logic diagrams your paycheck is going to suffer the
13:42
the folks male and female that can do both specifically write ladder logic diagrams
13:48
are going to be able to call for higher paychecks for higher hourly rates higher
13:54
salaries because they can deliver what the customers want so here's a simple piece
14:00
of structured text you got a couple if then statements and i picked these on purpose because i'm going to compare it
14:06
to ladder logic diagrams so it says if input 1 then output 9
14:11
true so basically it's saying if input 1 is on then turn on output nine
14:17
otherwise or else turn off output nine so this is if input one is
14:24
on turn on nine output nine if it's off turn off output nine this one says
14:30
if input 0 then turn on 8 that's the end of it this one says if
14:36
not input 0 then turn off 8. so this if then else up here does the
14:44
same basic thing as these two down here this turns it on and this turns it off
14:49
so let's look at the lander logic this says if i'm trying to use different addresses to make this easier to compare
14:55
when we actually run this on a plc so here we had if input 1 then turn on 9 otherwise turn
15:03
it off then here we have if input 0 then turn on 8 if not input 0 turn off 8. if
15:10
we go over here if input 1 then turn on output 11. this
15:15
particular instruction right here it's called a coil or an output energize it has a true
15:22
and a false execution so if this is true if input 1 is on or
15:29
turn on output 11. if it's off then turn off see it's a real simple statement
15:34
these two down here this has a true and a false execution if the rungs true if the statement's true turns it on the
15:41
statement's false turns it off these if the wrong is true or this this statement is true it turns it on but if
15:48
the statement goes false it does nothing there's no else whereas this one if the wrong is true
15:56
then it turns it off and if it's false it doesn't do anything these two sets of code right here this and this
16:03
are identical they have the exact same function i pick different outputs simply
16:08
so we could see them operate when we open up the simulator now i have another example here and it's uh called case and
16:17
we have three cases over here i see i'm missing one so i'm gonna double click on that and
16:23
bring that in i have to open this up a little bit this is the one i wanted to look at first though
16:29
because if you're a structured text person then you immediately recognize it so this is saying and i'm
16:37
elucidating or elaborating on the text the case of
16:44
state is a variable it's an integer so in the case of state equaling one
16:50
then you see four statements there turn on output zero turn off one two and
16:56
three however if the state is two then turn off zero and on one and off
17:02
two and three now the reason you have to do this is because whatever you tell that output to do it'll stay in that
17:08
state until you tell it otherwise so in each state you have to tell what output is on and which ones
17:15
are off so you and i put 0 part way down just to show you now logically i would
17:21
put 0 at the top then 1 2 3 4 just because it makes it you know more it makes it easier to read now the same
17:28
thing in lander logic would look like this now remember that i'm using
17:34
a type of instruction that says it's on but there's no else so it's
17:39
just saying turn on zero turn off one two and three so each case
17:45
is turning on one thing and turning off everything else and then for zero i have if the state is zero then just turn them
17:52
all off okay so now we go back to the ladder logic it takes a little up a
17:58
little bit more space on the page i mean i can geezer it down you know to get more of it on the page
18:04
to make it more readable but i wanted to show it specifically like this so this is an equal
18:11
instruction so it says if the state is equal to 1 then turn on 4 turn off 5 6
18:18
and 7. and all of these statements are all the same if the state is equal to a particular value then do this in this
18:25
case it's turn off four turn on five and turn off six and seven
18:32
all the way down the bottom if you're in state four then turn off four five and six and turn
18:38
on seven now there's an easier way to do this because remember these instructions don't have a true and a false execution
18:44
it's true only so if we go to another example which is actually simpler
18:50
if the value of state the integer if it's 1 equal to 1 then
18:55
turn on output 12. if it's not equal to 1 then it turns it off so this replaces
19:04
a little bit more beefy looking thing and they both accomplish the exact same
19:10
thing you know there are people that look this just say it's a complicated mess and i'm looking at and
19:15
thinking how's that possible this is like an electrical diagram and over here this vertical bar
19:21
that's plus 24 volts and this is zero volts these are individual circuits between plus 24 and zero
19:28
now we're not really doing voltage and current switching and load but it's
19:33
symbolic so it has linear logical conductivity whereas if you look
19:40
at this you don't see any logical conductivity a matter of fact you have to read it a bit
19:46
to picture that but let's let's keep this simple so i downloaded this to
19:52
the plc so i'm going to connect so now we're ready to download this to the controller and remember i told you i'm
19:59
not using the controller i'm using the simulator so i go up here to this button start micro 800 simulator it brings it
20:05
up on the screen a simulator i'll just move it over a little bit
20:10
maybe i can scrunch this up a little bit so i've got it all on the screen everything i need
20:16
for what we want to do that a plc has memory it has firmware etc your laptop
20:22
your desktop it has memory it has firmware etc so a simulator takes a section of the
20:29
memory in your computer your laptop or desktop and mimics the memory
20:36
structure and everything in a particular micro800 now in this case there's only one model
20:43
that you can use for the simulators of micro850 what separates this is these
20:49
input terminals right here if you want to operate and you you can just click here and turn on input 0 and then any
20:56
outputs are turned on these will light up down here so let's do that now i'm going to connect and it just so happens
21:03
well i try to connect but you know what i forgot to turn this on so i'm going to turn it on first even though i
21:08
started the simulator i didn't actually power it up so right now it's powered up and you can see it said connection
21:15
failed that's because i tried to connect before i powered it up i have to do connection path i needed to get it right
21:21
here and we're not going through how to set up the simulator this could be a real piece
21:27
of hardware okay so now we want to connect now that we have a path see up here i didn't have a
21:34
path in there i do now so i've started the process of connecting and we're going to go online
21:39
let's go back to the if then else structured text okay so you recognize this and then right
21:46
next to it we had the ladder logic diagram now notice right away that you see red
21:51
and blue blue from here over means false
21:57
here it means on and whenever you see the text
22:03
that text will be read if that bit memory is on and if the wrong is true like this one
22:11
you know the instruction is true because input 0 is off the wrong is true
22:16
and this turns off output 10. so if i turn on input 0 and i
22:21
watch here and put 0 is on now look
22:28
now there's eight and ten both came on because i have other code in here that's also
22:34
using input zero which happens to be your structure text
22:41
so see if input 0 then turn on 8 so you see 8 is
22:48
on here okay now when you look at that structure text you see any hint whatsoever
22:56
of what's true or false forget to forget this guy over here because you're not going to have this
23:02
to look at you can open up the doors of the panel electrical panel and you can go look at
23:08
the plc the controller and you can see leds lit up here so you could see the
23:13
same thing but what you're not going to see is this you're not going to have this to look at
23:20
you don't have a clue of what's true or false on or off here and you're online right now this is not
23:26
offline i'm online okay so let's turn off input 0 and you
23:32
can see that the logic changes if i went here and said why isn't what's on and
23:38
what's off you don't have a clue but if you go here you can see that nothing's
23:43
on go back here you have no clue now let's take something a little bit more complicated let's do a case okay we
23:50
looked at this a little bit early and i'm online now this is running okay so if i were to turn on input 0 and i'm
23:57
going to go do that right now no i'm going to change the state okay now to do that
24:03
i would have to right click on state here variable monitoring and i'd have to go in there and change this to a one hit
24:10
enter do you see anything change here look close let's go over to
24:15
the same logic but in ladder logic well yes you see right away
24:20
i'll put four is on and when you look down through these equal statements these are all blue right
24:27
and only one of these is red that means the statement is true and it's turning on output four
24:35
now if we change the state remember how we did it in this structured text
24:40
we kind of right clicked on it and picked variable monitoring now in ladder logic diagram
24:45
you would simply click right there any place that you saw any place where it says state
24:51
and we'll pick zero that'll put it back kind of where it was and now you see
24:56
this is true and it turns them all off so if you go here you can't tell what's true or false you
25:02
don't have a clue go here you look and say oh i got a true rung and it's turning all those off
25:09
now there's another way to do this logic that's more straightforward and that's this one
25:15
and again remember i'm using different outputs so when you look at the simulator you're
25:21
going to see different outputs come on based on what inputs i turn on
25:26
now for the state logic it's going to be if i put this in state 1 logical value
25:32
1 enter notice what came on
25:38
0 4 and 12. so here's 12. remember we've got
25:44
two different examples of this logic this one which uses the set reset or
25:52
these instructions have a true execution no false execution so i can use this instruction to turn
26:00
the bit on but i can't turn it off if i want to turn it off i have to use a reset set and reset latch and unlatch
26:08
so in this case i'm using the state i'm using that integer variable
26:14
in all three of these examples here now on this one if i pick
26:20
a different state and i'm going to show you something interesting here i'm going to go
26:25
to zero
26:31
and you notice that they go off let's do something slightly different let's
26:37
make this four and you can see the fourth one turns on
26:43
remember i have three different examples here i've got 12 13 14 15. i've got four
26:48
five six seven i've got zero one two three but let's change it to
26:54
something that's not accounted for like five
26:59
notice that this one turned off because there is no statement that says
27:06
if the state equals five then do something these other two
27:13
this one doesn't have it can't do a zero see right here notes
27:20
you would have to have a zero to turn them all off but in this case if you don't have a
27:25
state that matches any of these then they're all off because this is a
27:30
would be like a then else in other words it has a true to false execution the point here is
27:36
that when you're looking at this you don't have a clue what's true false on or off now you can
27:43
you can right click and go to variable monitoring and you can go and look say
27:48
well that one's off you can go down here say well three's on and now you're trying to relate that to
27:54
something up here it just doesn't work so the bottom line is there's no way in the world you can
28:00
troubleshoot structure text as quickly and easily as ladder logic diagram now there was a time when i think rockwell
28:07
had animated structure text so the variables change color
28:12
but that still did not define a true and false continuity in the structure
28:18
of the code if you're writing ladder line or if you're writing structure text programs for machine control
28:25
just be warned that there will come a time if you continue to do it where it's going to
28:30
come back on the company you're working for from their customers saying we don't want any more now they're going to be looking for
28:36
somebody that could program ladder logic diagram or even more important and this is where it could be your advantage
28:43
if you learn lander logic diagram programming right now get at it then you can be someone that can convert
28:50
structure text to ladder logic diagram for the sake of reducing downtime bottom
28:55
line you need to learn ladder logic diagram if you're going to do machine control and if you don't understand the
29:01
electrical nature you know this is your power bar over here on the right and this is your neutral bar on the left if
29:08
this electrical nature doesn't you don't understand it then you don't
29:13
know enough about electricity industrial electrical controls to be fooling around writing programs for industrial control
29:20
that sounds harsh but i'm trying to do you a favor here if you're doing structure text programs
29:26
right now i'm not telling you to stop i'm just telling you to learn ladder logic diagrams and start switching over because the
29:33
day's going to come where the people who can do ladder logic diagrams are available to work for machine builders are going to
29:40
get paid more money than structured text now here's a case where it's a little bit more complicated i
29:47
showed you real simple examples but this is a more complex example of structured text real easy to read it
29:54
says if this is the first program scan then set these variables to these values in
30:00
other words step set i step to zero and this variable is zero and then turn
30:07
off these three bits they're they're binary booleans and if
30:12
now case of i step equaling zero see up here it says i step equals zero so you start
30:20
here it initializes the value of all these variables and then
30:25
it sets i step to 10 immediately so you go to 10 here and you've got
30:32
these they're they're not difficult to read but if you're trying to troubleshoot and
30:37
you can't see the value if you can't see what's true or false you're going to end up
30:43
wandering around in here because it's really spaghetti code now it starts out pretty straightforward sets it this state to 10 10
30:51
blah blah blah set it to 15. however if this wasn't true then you got else if
30:59
this then this else so they're nested and if then
31:06
inside of an if then that's spaghetti code very difficult to follow so you're not
31:11
going to be able to follow this period then you've got here you go to 15. look
31:17
let's say that this is an else you go to step 700 and that's way down here
31:24
so you're jumping across a bunch of code i never do jump to labels in my code
31:30
it's just too much spaghetti code so if you look down through here imagine all this
31:36
you're trying to read through this and find out what is and what isn't what's on what's off what's true what's false
31:42
and there's not a clue here okay i'm go all the way down to the bottom
31:48
that's a lot of stuff to scroll through trying to figure out what's going on this is not an iphone app
31:54
where you've got thousands or you know a million people using it so you got a big
31:59
user base to get the thing debugged this is an industrial machine the reason i sound a little harsh in
32:06
this discussion is because i'm in the process of converting this over to ladder logic diagram
32:13
because the customer that bought the machine is out in the boondocks
32:18
something happened it got locked up couldn't find anybody to troubleshoot
32:23
the program primarily because it was structured text and then since they couldn't find
32:29
anybody to troubleshoot it then they called me and i took one look at i said well
32:35
i'll be honest with you i'm going to convert this over to ladder logic diagram otherwise you're going to be back in the
32:41
same situation again next time it doesn't function you're going to be looking for
32:46
somebody to work on it if i sound a little rough i'm still dealing with the frustration of this project and i don't
32:52
see any into it i see more and more of this showing up out on the factory floor
32:58
have a great day