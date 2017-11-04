"""Repository for all journal entries in the learning journal application."""

ENTRIES = [
    {
        "title": "Day Fifteen",
        "body": "Friday was a long day of code review. I have a better sense of the templating feature in jinja2 after the review. And I'm looking forward to re-implementing the templates so that step2 of the this very learning journal starts to have less hard coded items and more dynamically rendered ones.",
        "id": 15,
        "creation_date": "2017-11-04T05:00:57.379633",
    },
    {
        "title": "Day Fourteen",
        "body": "Pyramid's file structure is starting to make sense to me but only because this evening has gone so late in troubleshooting heroku deployment. It is still not working but there are fewer errors than there were a few hours ago. Progress.",
        "id": 14,
        "creation_date": "2017-11-03T05:00:57.379633",
    },
    {
        "title": "Day Thirteen",
        "body": "The max heap project moves apace. Gabe had really thought a lot about how to break out our functions so that the push method for our max heap data structure could work without being entirely cluttered. He really held himself - and therefore us - to staying within a one-function-for-one-thing approach. We also worked on the pop method on the white board. Because of a robust sudo code, mostly code with some non-code words thrown-in, the actual code should go fast tomorrow.",
        "id": 13,
        "creation_date": "2017-11-02T14:35:09.367906",
    },
    {
        "title": "Day Twelve",
        "body": "Today tired me out. After yesterday's introduction to Pyramid there was little respite. We had to put it into practice. At the start, the file system was more complex than I had encountered before. In particular, it became very clear that I needed to get tree into my bash. Well, that makes it sound so smooth since I spent far more time wondering why I was not able to see my entire file tree as it was presented in the notes for the class. I did ultimately realize that it was not standard. And then once it was uploaded I had the ability to see the tree structure of all my files. YAY!\r\nMostly the day was blurred by trying to figure out a max heap. Gabe and I spent a lot of time wondering whether we should think through the heap as a series of nodes or whether to think of it as a list. We realized that a list would work better after we had white-boarded. And then after we drew. And then after we read. And then did it all over again. The heap is not done yet in our repository but we know what the end looks like.",
        "id": 12,
        "creation_date": "2017-11-01T03:13:48.218663",
    },
    {
        "title": "Day Ten",
        "body": "A good week of work and learning. Rob and I went through the singly linked list assignment in the morning before lecture. It was slow going but he worked me through a white board. It was painful and it was awesome. The main take away was the head is everything that matters. And once you know what the head is doing that's it. In other words, the list is abstract. There is no list per se. There is only the head and pointer to another, i.e. next node, if there is a next node. It put me in a good frame of mind for the rest of the day. I did not complete the gist but I was really close. And the white board challenge broke my brain. But the good start to the morning kept me buoyed throughout.",
        "id": 11,
        "creation_date": "2017-10-28T19:42:11.111629",
    },
    {
        "title": "Day Nine",
        "body": "Today my data structures partner and I worked through doubly linked lists. It was a good time figuring out how to make the pointers point in both directions. In particular, my partner seized on the visual of a thermos, a mouse, and cellphone to demonstrate in three dimensions a linked-list in action.\r\n\r\nThe thermos was first in. It was the head and the tail. The mouse joined the thermos in the list to become the next to the thermos's previous. And thus the mouse was the new head. Once we added the cellphone, the mouse became the previous to the cellphone's next. And the cellphone was now at the head of the list.\r\n\r\nIt was great to hear about the experience of former python 401 students. The most impressive aspect was how they were continuing to grow and push themselves. It was amazing to think that they had just recently - only six months earlier - been at the end of their python course.",
        "id": 10,
        "creation_date": "2017-10-27T04:02:58.589705",
    },
    {
        "title": "Day Eight",
        "body": "Today I learned that there is a lot more to do in the rest of the week. One small yet mind-blowing realization. A stack can have multiple meanings in tech. When implementing the stack exercise for data structures, a stack is simply a collection of data. So for example the stack of a singly linked list, means the collection of nodes of that that list. And to retrieve data from the stack, aka the linked list, one needs only to retrieve the last item into that stack. LIFO. I know it sounds really idiotic but recognizing that a stack can be as small as a linked list with two items to being as large as an entire computer framework blows my mind. Ever onwards!",
        "id": 9,
        "creation_date": "2017-10-26T14:50:15.961996",
    },
    {
        "title": "Day Seven",
        "body": "Lots to learn today. Code review was slightly different, since instead of walking through someone's base code, we built up the code together. It was really good. And really taxing. It was particularly good to see how to keep tests simple. Or not to overthink the tests. Small tests work well.\r\n\r\nThe remove method in linked list was surprisingly difficult to work out. I'm still not sure I know what we did. I've gone through thinking about the list as a set of three, which is basically how we structured some of the other testing functions, and then I can keep clear what is happening in the function, called ```remove```. Yet I've yet to implement through drawing what it would look like if the linked list became twenty or thirty. A challenge for the morning. Ever onwards!",
        "id": 8,
        "creation_date": "2017-10-25T04:42:34.523542",
    },
    {
        "title": "Day 6",
        "body": "First the good. I wrote a while loop without hyperventilating. I wrote a try and except, with a lot of coaching from Megan, in the sockets exercise. And with the testing in the linked list exercise, Gabe and I were able to test some functionality, particularly in testing the counter that we had set up. Tests that actually test functionality are pretty great. And then there was the not so great: recognizing that a lot of mailroom is not going to be done in time when it is handed in tomorrow and committing way too late to a refactor for the nth series kata. Ever onwards!",
        "id": 7,
        "creation_date": "2017-10-24T06:09:21.620436",
    },
    {
        "title": "Day Five: Day of Code",
        "body": "That was amazing! Not only did many code wars challenges get done but I also think I got my head around testing. Thanks to all those people who made tox understandable, you know who you are!",
        "id": 6,
        "creation_date": "2017-10-22T06:33:33.866831",
    },
    {
        "title": "Day Four",
        "body": "Today was hard. My confidence got sapped after completing, there should be air quotes around completing, the lightning challenge at the end of class. Chai and I made it through nearly all of the kata fourteen on milkwood. In particular, it was interesting to see the __name__ = __main__ doing something more than printing out words to the command line. For instance, within the it we placed a variables and other stuff necessary to run the command line for a user. It was a new wrinkle for what is possible there. Looking forward to tomorrow to work through some challenges and experience my first 'snow day', err day of doing Code Wars, at Code Fellows.",
        "id": 5,
        "creation_date": "2017-10-21T04:03:59.142183",
    },
    {
        "title": "Day Three",
        "body": "What I learned today was that learning a new language is not all unicorns kissing narwhals. Simple string mutation, as my partner and I were trying to do this afternoon, proved to be a real challenge. We worked through the logic of word-challenge problem, on trigrams, somewhat cleanly. And then we spent most of the afternoon doing simple string manipulation, getting different types of errors. It was really slow going.",
        "id": 4,
        "creation_date": "2017-10-20T15:03:15.568643",
    },
    {
        "title": "Day Two: Partner Work",
        "body": "Chai and I finished up our lab. It was a good time figuring out the Fibonacci sequence and figuring out what was happening within the module itself. We had an interesting time figuring out what exactly name and main was, i.e. 'if __name__ == \"__main__\":'. As far as I can tell, right now, the list of functions and print calls is the way to keep all the functions bundled to the specific module and to let a user know what functions are indeed inside a particular module. It was also simply a good time to catch up on readings. Ever onwards!",
        "id": 3,
        "creation_date": "2017-10-19T03:57:34.538784",
    },
    {
        "title": "Day Two: Pair Programming Begins",
        "body": "I was particularly excited about reading the first three chapters of how to think like a computer a scientist. Besides the book being somewhat buggy, I felt confident going through the exercises. And the errors of: syntax, attribution, and type seemed very familiar, especially in light of the work from Day One. It was great to be pair-programming again. We did not, as quickly as I would have liked, get the hang of making tests. The pull to dive into the function to get it to work, without the tests, was pretty strong. I look forward to getting better at making tests and thinking more creatively about edge-cases.",
        "id": 2,
        "creation_date": "2017-10-18T04:40:30.312862",
    },
    {
        "title": "Today I learned...",
        "body": "Today I really felt the rush of learning something new. I had the experience, while doing the prework, of making my first cross linguistic mistake - I was assigning a variable as if I was coding javascript rather than in python. It felt really great. I wrote down the date and time. Now as class gets under way I feel like every mistake and each new thing is going to come faster and faster. And I won't have time to mark just how quickly it is all happening. So, with this first journal entry of python, I simply would like to mark my overall enthusiasm for the journey that has begun.",
        "id": 1,
        "creation_date": "2017-10-17T00:55:57.230347",
    }
]
