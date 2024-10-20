This is information on how to use the spotify dedup playlist songs program.

Start by going to https://developer.spotify.com/ and log in by clicking the hamburger menu in the upper-right hand corner.

Click the hamburger menu item again and click dashboard.

Click create new app.

Give the app a name, description, and make the redirect URL to be open.spotify.com.

Save the app.

Go into the settings and paste the Client ID into the client_id variable in the script.

Now view the client secret and paste that into the client_secret variable in the script.

Open a new tab and go to open.spotify.com.

Select the playlist that has duplicate songs. 

Take a look at the url of this playlist, and copy everything to the right of the final '/' character in the URL. This represents the playlist id.

Paste this playlist id into the playlist_id variable in the script.

Run the script.