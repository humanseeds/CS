# Ascii Conversion App
####https://www.youtube.com/watch?v=bhJ31YchaHc


####Description

So for my final project I decided to make an asci art app! I have always considered ascii art a type of computer magic more than science. When we are young we all looked at computers as moe magic than science and i felt that this project exemplifies that concept. Except now, thanks to cs50, i see that it is well, science.

The app itself is rather simple in its organization. I have my final-project folder, and it conatains a templates folder for my .html files, an upload folder and of course my App.py. I also have a helper file that has all of the differnt functions that i needed to make the artwork. The uploads folder is where all the images are saved and the App.py does all the heavy lifting for the web app itself

Anyone can go to the apps, upload page. I kept it as simple and user friendly as possible. the upload page has some bsaic html to create a nice container that has a prompt to upload your image. It accepts a range of different file types and there will an error message if the wrong type of file is used. After the user uploads and image they are redirected to the restuls.html

For the results.html i thought it would be nice if the user could view a before and after. So the original uploaded image is displayed up top, and below it is displayed their ascii art! there is also a button at the bottom asking if they would like to upload another image which will redirect them back to uploads.

So underneath the hood of the app we have a pretty simple structure. It is a throwback to week 4s homework assignments. This isnt written in C, but the principals are the same. We have a series of helper functions that we use to transform the users image into an ascii art rendition. I was tempted to right out the functions myself but after week 6 python seeing how nice and simple it was to import libraries to do the hard work i figured i would give that a shot, since i was less familiar with libraries than creating the functions.

The main process is as follows. We take the image that is uploaded from the user. we create a path for it so that flask can access it later, and so that we can pass the file around different functions easily. The first step is making sure the aspect ratio is correct. each charcter is more tall than wide, so I wanted to adjust this so the ascii art would not looked stretch out. After this we then create a greyscale version of the image just like in the Filter assignment. This gives us the brightness of each pixel so to speak. Once we have the brightness value of each pixel we can then create a map to assign ascii charcters to the representation of each pixel

To be honest this was the hardest part, mainly because at first I thought I was just making a filter that could be stored in the same file format as the original image, but what I learned is that so make an ascii image, you are actually making a string! And because it is a string, it has to be stored as a .txt file and not one of the image files that are accepted as an upload. The string matches the same width and height of the pixels so when it is displayed it resembles the image.

After all the we save the image and serve it back up to the results.html to be displayed. The app.py handles all of the routes and assembles the functions in the helper folder to make everything work. i wanted to keep the helper functions and app.py as seperated as possible to make everything easier to follow. I did have issues trying to run all of the ascii conversioins in helpers but i soon realized the app.py is where i had to call all of the helper functions together.

Now that I have a working app and model of how the functions flow, in the future I would like to try and add sobel operator to give the images more definition. By highlighting the edges i could create a different set of ascii charcter to define the outlines of features in the images. I could use radians to determine the direction of the edges and make more detail on the images. I would also like to create user log ins, a public gallery to show off examples and even work on useing color channels

With all of that said I am extremely thankful to Harvard for allowing a non student like me to take this class, Cs50 and David Malan for putting such a beuitful program together that was challenging and informative. Before this class I didnt know the difference between a file and folder, and today I am making a web app and computer magic to share with others. Thank you for everything.
