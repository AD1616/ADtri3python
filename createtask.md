{% include style.html %}


{% include navigation.html %}



# Create Task Project

## Runtime

[Link to runtime](https://nastyawakened.cf/quizcrud/quizDB/)

## Code File

[Link to code](https://github.com/NastyAwakened/NastyAwakened/blob/nastys/crud2/templates/crud2/quizDB.html)

## Idea
* Create a system of taking a quiz where you can see if you are correct or incorrect, move to next question, and get a score.
* Also have a database so that quiz questions can be created and stored server side. 
* [Issue with commits](https://github.com/NastyAwakened/NastyAwakened/issues/136)
* [Jump to my video and written responses](https://github.com/AD1616/ADtri3python/blob/main/createtask.md#my-video)
* PBL Feature: This is implemented as PBL and can be found under the "Classes tab" and is called "Quiz Page".

# My Video

* [Sahil Create Task Video](https://www.youtube.com/watch?v=ZSTxeuZcMHY)

# Written Responses

* 3a-3d responses should not be more than 750 words, not including code.

## 3a. Provide a written response that does all three of the following:

### Describes the overall purpose of the program

* The overall purpose of the program is to provide functionality for an interactive quiz. The program will have questions and four answer choices for the user to select. The user will see if they got the question right or wrong, and they can see their score.

### Describes what functionality of the program is demonstrated in the video

* The functionality of the program shown is taking a quiz and being able to select an answer choice for each question. The program will tell you if the selected answer choice is correct or wrong. A running score can also be toggled on and off by the user.

### Describes the input and output of the program demonstrated in the video

* Input is the answer choice selection for the presented questions and the buttons for "Next Question" and "Submit". Output is the display of the question and four answer choices, "Correct!"/"Incorrect!" assessment upon answering the questions, and both a running and final score. Another input is a text box where the user types "Yes" or "No", and output is to show or hide the score.

## 3b. Capture and paste two program code segments you developed during the administration of this task that contain a list (or other collection type) being used to manage complexity in your program.

###  The first program code segment must show how data have been stored in the list. 

```javascript 
        var allQuizData = [
            {'questionID': 1, 'question': 'Which of these is a paradigm of Object Oriented Program?', 'answer1': 'Class', 'answer2': 'Blueprint', 'answer3': 'IP Address', 'answer4': 'GET', 'correctAnswer': 'Class'},
            {'questionID': 2, 'question': 'Which of these is a binary number?', 'answer1': '0101', 'answer2': '#FFFFFF', 'answer3': '49', 'answer4': '2', 'correctAnswer': '0101'},
            {'questionID': 3, 'question': 'Which of these is NOT an HTTP verb for requests?', 'answer1': 'GET', 'answer2': 'POST', 'answer3': 'DELETE', 'answer4': 'GIVE', 'correctAnswer': 'GIVE'},
        ]
```


### The second program code segment must show the data in the same list being used, such as creating new data from the existing data or accessing multiple elements in the list, as part of fulfilling the program’s purpose. 


```javascript
        
 {# This function is called by the button for begin quiz/next question/endquiz; it determines what questions and answers to display based on the value of question number. #}
        function newQuestion() {
            ...
            document.getElementById('showQuestion').innerHTML = allQuizData[questionNumber]['question'];
            document.getElementById('choice1').innerHTML = allQuizData[questionNumber]['answer1'];
            document.getElementById('choice2').innerHTML = allQuizData[questionNumber]['answer2'];
            document.getElementById('choice3').innerHTML = allQuizData[questionNumber]['answer3'];
            document.getElementById('choice4').innerHTML = allQuizData[questionNumber]['answer4'];
            ...
        }
```

### Identifies the name of the list being used in this response

* The name of the list is "allQuizData". 

### Describes what the data contained in the list represent in your program

* The list, "allQuizData" represents the question bank for the quiz. It is a list of three dictionary elements, and each dictionary contains key value pairs as follows: "questionID" (the ID of the question) , "question" (the question itself), "answer1" (first answer choice), "answer2" (second answer choice), "answer3" (third answer choice), "answer4" (fourth answer choice), and "correctAnswer" (the correct answer option). Each list element independently completely represents all the data for one question that will be later needed by the code.

### Explains how the selected list manages complexity in your program code by explaining why your program code could not be written, or how it would be written differently, if you did not use the list.

* By using the "allQuizData" list, each question can be easily displayed through the following process: create a variable called questionNumber representing the question number and starting it at 0; index the list at questionNumber to get the dictionary with all the data for that question; get the value for the needed key and then display each value as needed by assigning it to different HTML elements; update questionNumber to move to the next question. Without using a list, the second code segment would be duplicated as many times as there are questions (three times for three questions), with the questionNumber variable instead being replaced by a hardcoded number for each new question. Without a list, the code is not scalable as the code size dramatically would increase with each added question.

## 3c. Capture and paste two program code segments you developed during the administration of this task that contain a student-developed procedure that implements an algorithm used in your program and a call to that procedure. 

### The first program code segment must be a student-developed procedure that:

1. Defines the procedure’s name and return type (if necessary)
2. Contains and uses one or more parameters that have an effect
on the functionality of the procedure
3. Implements an algorithm that includes sequencing, selection,
and iteration 

```javascript

        function evaluation(view) {
            {# Storing the correct answer; answerindex was updated in the newQuestion function, and the list is indexed at this value to get the dictionary for the current question
            and then the value for the key "correctAnswer" is accessed. #}
            var correct = allQuizData[answerindex]['correctAnswer'].toString()

            {# Iterating through all of the choices to see if they were selected by the user. If selected, the selected choice is compared to the correct answer stored in the database.#}
            for (let i = 1; i < 5; i++) {
                {# The first if statement checks if the user has selected the current choice. If they have not, then the code moves on to the next iteration of the for loop. #}
                {# The loop has to check option1, option2, etc. so it gets the current option by concatonating the word "option" with the current index. #}
                if (document.getElementById('option' + i.toString()).checked) {
                    {# The second if statement checks if the chosen answer choice matches the correct answer. #}
                    if (correct ==  allQuizData[answerindex]['answer' + i.toString()]) {
                        {# If it does, I format a green border and show text that says correct #}
                        document.getElementById('block' + i.toString()).style.border = '5px solid green'
                        document.getElementById('result' + i.toString()).style.color = 'green'
                        document.getElementById('result' + i.toString()).innerHTML = 'Correct!'
                        {# The score is updated regardless of the view parameter #}
                        if (view == null) {
                            score = score + 1
                        }
                    }
                    {# If the answer is incorrect, I format a red border and show text that says incorrect #}
                    else {
                        document.getElementById('block' + i.toString()).style.border = '5px solid red'
                        document.getElementById('result' + i.toString()).style.color = 'red'
                        document.getElementById('result' + i.toString()).innerHTML = 'Incorrect!'
                    }
                }
            }
            {# The score text is set to the value of score. #}
            document.getElementById('score').innerHTML = "Score:" + score;

            {# Based on the parameter of view, calling the function will either yield the score to be displayed or not displayed.#}

            if(view == "Yes") {
                {# If the passed in parameter was Yes, then the current score will be displayed. #}
                document.getElementById("score").style.display = 'block';
            }
            else if(view == "No") {
                {# If the parameter was No, then the current score will not be displayed. #}
                document.getElementById("score").style.display = 'none';
            }
            else {
                {# If the parameter was not yes or no, then the current score will not be displayed. #}
                {# The submit button calls evaluation with a view parameter of null, which is also handled by this else statement. #}
                document.getElementById("score").style.display = 'none';
            }
        }
        
```

### The second program code segment must show where your student-developed procedure is being called in your program.


```javascript

        {# Called by the button next to the input box to show the running score #}
        function showScore() {
            {# Setting a variable to the text in the input box #}
            var chosen = document.getElementById('scoreView').value;
            {# Calling the function, evaluation, with a parameter to show score or not #}
            evaluation(chosen);
        }
        
```

### Describes in general what the identified procedure does and how it contributes to the overall functionality of the program

* The "evaluation" procedure helps with the interactive quiz program by checking the submitted answer and displaying whether it was correct or incorrect. It also updates the score and determines whether the current score is displayed or not based on a parameter called view.

###  Explains in detailed steps how the algorithm implemented in the identified procedure works. Your explanation must be detailed enough for someone else to recreate it.

* The "evaluation" procedure takes an input parameter called "view" which determines whether the running score is shown. First, the list containing the question dictionaries must be indexed (the index is determined by a global variable which is updated by a separate procedure) at the current question to get the dictionary containing all the data for the question. The "correctAnswer" key in the dictionary is accessed, and the value is stored in the variable "correct". Then, the procedure iterates through the answer options using a for loop and an if statement checks if the user has selected the option. If they have not, then the code moves on to the next iteration. The loop gets the current option by concatenating the word "option" with the current index, as these are the corresponding HTML element names. A second if statement checks if the chosen answer choice matches the correct answer. If it does, format a green border and show text that says "correct". Add an if statement so that the score is updated when "evaluation" is called with a "view" parameter that is null. If the answer is incorrect, determined through an else statement, format a red border and show text that says "incorrect". Set the score text element in the html to the value of score. Next, check if the view parameter is "Yes"; if it is, then display the score. If it is "No", then do not display the score. If it is neither "Yes" or "no", then do not display the score.

## 3d. Describes two calls to the procedure identified in written response 3c. Each call must pass a different argument(s) that causes a different segment of code in the algorithm to execute.

### First call: 

If the procedure "evaluation" is called with the "view" parameter "Yes" when the user types "Yes" into the input box, then the segment of code will execute to display the html element that contains the current score. 

### Second call: 

If the procedure "evaluation" is called with the "view" parameter "No" or anything else but "Yes", then the segment of code will execute to hide the html element that contains the current score. 

### Describes what condition(s) is being tested by each call to the procedure. Condition(s) tested by the first call: 

The condition tested is if the parameter, "view", is equal to the string "Yes".

### Condition(s) tested by the second call: 

The condition tested is if the parameter, "view", is equal to the string "No", or if "view" is equal to neither "Yes" nor "No".

### Identifies the result of each call. Result of the first call: 

The DOM(Document Object Model) of the score text will be shown; in other words, the current score will be visible to the user. 

### Result of the second call: 

The DOM of the score text will not be shown, so the current score will not be visible to the user. 
