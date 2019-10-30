<h1>Shopping cart</h1>

<p>This is created Pyhon's Django Framework</p>
<p>This program will do the following</p>
 <ul style="list-style-type:disc;">
  <li>Signup</li>
 <p>Sign up uses buitin Userauth libarary in django it takes username and password and send its primary checks it csrf token for security </p>
<img src="img/screen1.png">

 
 
 
 
 
 
 
 
 
 
 
  <li>Login</li>
  <p>Login uses buitin Userauth libarary in django it takes username and password and send its primary checks it also uses csrf token</p>
  <img src="img/sceen2">
 
  <li>Display Products</li>
  <p>I created model known as product with its follwoing attributes the built a specific url and sent requset to view product list
 and renderd it into template</p>
 <img src="img/sceen2">
   <li>Display Details</li>
 <p>The link diplays all the details of the product in  separate page </p>
 <img src="img/sceen3">
 
   
  <li>Add to a cart</li>
  <p>created models order and order items when add to cart is pressed it request a view acces the product id and add it to order item then its added to order</p>
  <img src="img/sceen4">
 <img src="img/sceen5">
  
  <li>Calculate total</li>
  <p>the add to cart view returns product price tottal</p>
  <li>Delete item</li>
  <p>It calls delete view which deletes the order item by using its object id </p>
  <img src="img/sceen6">
 <img src="img/sceen7">
  <li>Add inventory</li>
 <p>I made a custom form and django form template to add new product</p>
 <img src="img/sceen8">
 <img src="img/sceen9">
 
</ul> 
