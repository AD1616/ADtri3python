{% include navigation.html %}

# Hack 1

```html
 <div class="container py-4">
        <header class="pb-3 mb-4 border-bottom border-primary text-dark">
            <span class="fs-4">SQL CRUD Sign Up Page</span>
        </header>
    </div>

    <div class="container py-4 text-light bg-success">

        <div class="container bg-secondary py-4">
            <div class="p-5 mb-4 bg-light text-dark rounded-3">
                <form method="POST" ID="authUser" action={{url_for('crud.crud_authorize')}} >
                    <table>
                        <tr><th><label for="user_name">Username</label></th></tr>
                        <tr><td><input type="text" id='user_name' name="user_name" size="20" required></td></tr>
                        <tr><th><label for="email">Email</label></th></tr>
                        <tr><td><input type="email" id="email" name="email" size="20" required></td></tr>
                        <tr><th><label for="phone">Phone Number</label></th></tr>
                        <tr><td><input type="tel" id="phone" name="phone" size="20" required></td></tr>
                        <tr><th><label for="ghuser">GitHub Username</label></th></tr>
                        <tr><td><input type="text" id="ghuser" name="ghuser" size="20" required></td></tr>
                        <tr><th><label for="password1">Password</label></th></tr>
                        <tr><td><input type="password" id='password1' name="password1" size="20" required></td></tr>
                        <tr><th><label for="password2">Password Confirmation</label></th></tr>
                        <tr><td><input type="password" id='password2' name="password2" size="20" required></td></tr>
                        <tr><th><input type="submit" value="Submit"></th></tr>
                        <tr><td><a href={{url_for('crud.crud_login')}}>Log In</a></td></tr>
                    </table>
                </form>
            </div>
        </div>

    </div>
```

- Adding phone number to sign up screen consisting of adding it as an input parameter to this page, authorize.html. Phone was already a column in the database defined in model. In App_Crud it was also there in the create function.

# Hack 2

```python
@app_crud.route('/logout')
@login_required
def crud_logout():
    logout_user()
    return redirect(url_for('crud.crud_login'))
```

```python
# logout user
def logout():
    logout_user()  # removes login state of user from session
```

```html
<p> Logged in user: {{current_user.name}} <a href={{url_for('crud.crud_logout')}}>Log out</a></p>
```

- The second code snippet is from the query file; this is where we imported the logout_user function defined in flask_login. This is imported into app_crud and the logout_user function is called under crud_logout. This function can be referenced by an html by doing crud.crud_logout, which is done after a user has logged in; the implementation on the crud page with the data table shown after logging in is in the html code above.


# Hack 3

```python
@app_frontend.route('/snake')
@login_required
def snake():
    return render_template("snake.html")
```

- Added in login required to snake. Just consists of adding @login_required before the render template function. 


# Navbar

```html
<p> Logged in user: {{current_user.name}} </p>
<div>
    <!-- <a href={{url_for('crud.crud_login')}}>Log In</a> -->
    <button type="button" onclick="window.location.href='{{url_for('crud.crud_login')}}';">Log In</button>
</div>

<div>
    <!-- <a href={{url_for('crud.crud_logout')}}>Log out</a> -->
    <button type="button" onclick="window.location.href='{{url_for('crud.crud_logout')}}';">Log Out</button>
</div>
```

- Above is the code for adding the login and logout to the navbar, along with current user info.

```html
<div class="collapse navbar-collapse justify-content-end" id="navbarSupportedContent">
            <div>
                <button class="btn btn-primary bg-secondary" data-bs-toggle="offcanvas" data-bs-target="#searchBar">Show User Info</button>
            </div>
        </div>

        "here goes curly brace percent block navbar_script percent curly brace"
            <!-- Navigation bar JavaScript support -->
            <script src={{  url_for("static", filename="javascript/navbar.js", version='140') }}></script>
        "here goes curly brace percent endblock percent curly brace"


    </div>
</nav>

<div class="offcanvas offcanvas-end bg-white text-dark" tabindex="-1" id="searchBar" aria-labelledby="offcanvasEndLabel">
    <div class="offcanvas-header">
        <h5 class="offcanvas-title" id="offcanvasEndLabel"> Your User Information </h5>
    </div>
    <div class="offcanvas-body small">
        <div class="container">
            <table class="table">
                <tr>
                    <th>Username</th>
                    <td> Logged in user: {{current_user.name}} </td>
                </tr>
                <tr>
                    <th>Login Button </th>
                    <td> <a href={{url_for('crud.crud_login')}}>Log In</a> </td>
                </tr>
                <tr>
                    <th> Logout Button </th>
                    <td> <a href={{url_for('crud.crud_logout')}}>Log out</a> </td>
                </tr>
            </table>
        </div>
    </div>
</div>
```

- Above is an attempt for offcanvas implementation. It should work, the only problem is I think the version of bootstrap may have slightly different syntax because the box is grayed out. 


