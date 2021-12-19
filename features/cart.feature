Feature: Shopping cart functionality

	Scenario: Adding an item to the cart by hovering over the image
		Given the user goes to page http://automationpractice.com/index.php
		And the cart is empty
		And the user clicks T-Shirts button
		When user hovers over the first visible image 
		And the Add to cart button is visible
		And user clicks the button Add to cart
		Then an item is added to the cart
