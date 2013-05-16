README

PSB_PEP8_features2

This program comply with PEP8 (OR ELSE EVRY1 WILL B SOOPER MAD @ U! LIKE DIS >8-[!
								Read pep8 or you will be flamed)

Naming conventions:
	all_functions_and_local_vars_will_be_named_like_this
	ALL_EXTRA_GLOBALS_WILL_BE_LIKE_THIS
	all local variables that = request.POST[something] will start with 
		psb_front_ or psb_back	
	
Features:
	Subscription/ Recurring payment
		This will require setting up cron jobs to send out emails + attached 
		invoices at regular intervals. As far as I know, Paysbuy.com does not
		currently support subscriptions or recurring payments.
		We COULD make some super hacky function that fills in forms for the 
		customer using locally stored cc info, but that sounds really stupid, 
		so lets not.		
	Future proofing + version toggle (v3.01 vs v3.04)
		This we will just have to build and test for. It would be really nice 
		if we could just toggle the versions in the admin. If we put a boolean
		value in the config.py file and some coditionals(if statements) in the
		urls.py that set function names as string viables, then call them in the
		urls it should work. Any (better) ideas here?
	Documentation
		Satchmo's documentation is pretty lame(they are a fairly new project 
		after all) and I think we should help change that.  Satchmo is lacking 
		good docs about writing cutom code and modules for it, AND installation.
		I think anyone who CAN contibute to this effort SHOULD.
	# The next two features are Paysbuy things that appear to be broken.
	 Let's not give up hope.
	GetExchangeRate
	GetOrderStatus
	
Advice:
	Whenever you add new code to your server, or are testing on you dev 
	environment always remember to DELETE YOUR .PYC FILES. This can be done
	easily with "pyclean /" in the command line. restart your project while you're 
	at it too.
	There are a bunch of bug fixes in requred libraries that will BREAK satchmo.
	Satchmo is highly version dependent and it may take you a while to get it 
	insalled right. For those of you who already got it right, congrats, tell
	us as much as you can about you install environment, commands used, library 
	versions, etc. so that others get it right too.
