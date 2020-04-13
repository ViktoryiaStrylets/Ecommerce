# Ecommerce
Django/Bootstrap4/Mysql
<!DOCTYPE>
<head>
 <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
  </head>
<header>
<h2> ShopWorld E-Commerce Platform</h2>
  <p>I love :shopping:</p>
</header>
<body>
  <h2>Getting Started </h2>
  <section id="prereq">
    <h3>Prerequisites</h3>
    <ul>
    <li>Python 2.7. x or 3.4. x.</li>
    <li>easy_install and Pip.</li>
    <li>Git.</li>
    <li>virtualenv.</li>
    <li>Django.</li>
    <li>Database (SQLite, MySQL, PostgreSQL, MongoDB, etc.)</li>
    <li> Text editor (Sublime, vim, Komodo, gedit)</li>
    </ul>
  </section>
   <hr>
  <section id = "installation">
    <h3> SetUp </h3>
    <div id = "setup">
      <ol>
        <li>Grab a copy of the project.</li>
        <p><code> git clone ecommerce.git</code></p>
         <li>Create a virtual environment and install dependencies.</li>
        <p><code>mkvirtualenv ecommerce</code></p>
        <p><code>pip install -r requirements.txt </code></p>
        <li>Enter your database settings in settings.py.</li>
        <p></p>
        <li>Initialize your database.</li>
        <p> <code>python ./manage.py syncdb</code></p>
        <p><code>python ./manage.py migrate</code></p>
        <p>If your app has a custom user model, you'll need to create a new superuser for the admin.</p>
        <p><code>python ./manage.py createsuperuser</code></p>
         <li>Run the development server to verify everything is working..</li>
        <p> <code>python ./manage.py runserver</code></p>
      </ol>
      </ol>
    </div>
    
  </section>
 
  <hr>
  <section id= "build_with">
  <h3>Build with</h3>
  <div class = "build">
    <ul>
      <li>MySql - Backend</li>
      <li>Django - Python Web framework to handle th backend application layer</li>
      <li>Bootstrap -The CSS framework was used to build the front-end </li>
    </ul>
  </div>
  </section>
<h3>Navigation</h3>
<div class = "Home">
  <img src = "https://github.com/ViktoryiaStrylets/Ecommerce/blob/master/blog/static/blog/Annotation%202020-04-08%20125109.png">
</div>
<hr>
<div class = "Login">
  <img src = "https://github.com/ViktoryiaStrylets/Ecommerce/blob/master/blog/static/blog/LOGIN.png">
</div>
<hr>
<div class = "Search">
  <img src = "https://github.com/ViktoryiaStrylets/Ecommerce/blob/master/blog/static/blog/search_sort.png">
</div>
<hr>
<div class = "Cart">
  <img src = "https://github.com/ViktoryiaStrylets/Ecommerce/blob/master/blog/static/blog/CART.png">
</div>
<hr>
<div class = "Cart">
  <img src = "https://github.com/ViktoryiaStrylets/Ecommerce/blob/master/blog/static/blog/REVIEW.png">
</div>
<small>&copyright copyright ShopWorld</small>
</body>
