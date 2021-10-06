# Face-Recognition-WebApp
A Facial Analysis Web-App deployed live on Heroku.

This is a Facial Analysis WebApp build with the help of Django and Deep Neural Networks. 

## Features
- This WebApp crop the face from the picture.
- Compute the face detection score using (0 to 1) which tells that we have detect the face correct from the image. 
- Name of the person in the picture. <br> This WebApp can only tell the name of few celebrities since the model is trained only on given list of celebrities. <br> 
  <ul>
  <li>Aamir khan</li>
  <li>Angelina Jolie</li>
  <li>Barack Obama</li>
  <li>Cristiano Ronaldo</li>
  <li>Donald Trump</li>
  <li>Elon Musk</li>
  <li>Joe Biden</li>
  <li>Leonardo DiCaprio</li>
  <li>Lionel Messi</li>
  <li>Robert Downey Jr</li>
  <li>Roger Federer</li>
  <li>Sachin Tendulkar</li>
  <li>Salman Khan</li>
  <li>Scarlett Johansson</li>
  <li>Tom Cruise</li>
  </ul>
-  Face Name score
-  Emotion Name (Angry, Disgust, Fear, Happy, Neutral, Sad, Surprise)
-  Emotion Score

## Steps to run
1. Clone this repo
```
https://github.com/jatin9909/Face-Recognition-WebApp.git
```
2. cd into directory
```
cd facerecognition
```
3. Download the requirements
```
pip install -r requirements.txt
```
4. Runserver
```
python manage.py runserver
```
5. Open web browser at http://localhost:8000
