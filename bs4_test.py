#!/usr/bin/env python
# _*_ coding: utf-8 _*_

from bs4 import BeautifulSoup
import re

html = """<body><iframe src="http://secure-us.imrworldwide.com/storageframe.html" id="LOCSTORAGE" scrolling="no" name="empty" hidden="true" style="width: 1px; height: 1px; position: absolute; top: -7px; left: -7px; border: 0px;"></iframe>



<div id="site_layout">
    <div id="masthead">


                    <div id="omnibar_wrapper">

        <div id="omnibar" class="ad_unit" style="display: none;">

                            <script type="text/javascript">

                        googletag.cmd.push(function() {

                                                            window.metac_g_ad_omnibar = googletag.defineSlot("/8264/aw-metacritic/movies",[980,45], "omnibar").addService(googletag.pubads()).setTargeting("pos", "top").setCollapseEmptyDiv(true, true);


                        });


                        window.metac_ads_pushdisplay.push("omnibar");
                                    </script>
                            <div id="google_ads_iframe_/8264/aw-metacritic/movies_0__container__" style="border: 0pt none;"><iframe id="google_ads_iframe_/8264/aw-metacritic/movies_0" title="3rd party ad content" name="google_ads_iframe_/8264/aw-metacritic/movies_0" width="980" height="45" scrolling="no" marginwidth="0" marginheight="0" frameborder="0" src="javascript:&quot;<html><body style='background:transparent'></body></html>&quot;" style="border: 0px; vertical-align: bottom;"></iframe></div><iframe id="google_ads_iframe_/8264/aw-metacritic/movies_0__hidden__" title="" name="google_ads_iframe_/8264/aw-metacritic/movies_0__hidden__" width="0" height="0" scrolling="no" marginwidth="0" marginheight="0" frameborder="0" src="javascript:&quot;<html><body style='background:transparent'></body></html>&quot;" style="border: 0px; vertical-align: bottom; visibility: hidden; display: none;"></iframe></div>



            </div>
                <div id="masthead_primary">
            <div class="masthead_wrap">
                <div class="logo">
    <a href="http://www.metacritic.com">

        <img src="/images/layout/mc_logo_inverted.png">
    </a>
</div>
                    <div class="masthead_search">
        <div class="search basic_search has_adv_search_link">
        <div class="search_section basic_search_section">
            <form class="search" method="post" action="/search">
                <fieldset>
                    <legend>Basic Search Fields</legend>
                    <div class="search_wrap">

                        <ol class="fields search_fields">

                            <li class="field search_field search_query">
                                <div class="field_wrap">
                                    <span class="field">
                                        <input class="text" type="text" size="50" name="search_term" id="masthead_search_term" tabindex="1" value="" autocomplete="off">
                                    </span>
                                    <span class="search_msg" style="display: inline;">
                                        Search Metacritic
                                    </span>
                                </div>
                            </li>
                            <li class="field search_field search_submit">
                                <div class="submit"><div class="btn"><button class="submit" type="submit"><span>Search</span></button></div></div>
                            </li>
                            <li class="field hidden">
                                <input type="hidden" name="search_filter" value="all">
                            </li>
                        </ol>
                    </div>
                </fieldset>
            </form>
        </div>









    </div>
    </div>


                <div id="primary_nav">
    <ul class="nav_items primary_nav">
                <li class="nav nav_movies active_nav has_menu_set">
            <span class="nav_item menu_hover_toggler">
                <span class="nav_item_wrap">
                    <a href="http://www.metacritic.com/movie">
                        <span class="nav_text">Movies</span>
                    </a>
                                            <span class="menu_click_toggler">»</span>
                                    </span>
            </span>
                            <div id="primary_nav_movies_menu" class="menu_items primary_nav_menu">
                    <ul class="menu_items">
                                            <li class="menu_item">
                            <a href="http://www.metacritic.com/browse/movies/release-date/theaters/date">In Theaters</a>
                        </li>
                                            <li class="menu_item">
                            <a href="http://www.metacritic.com/browse/dvds/release-date/new-releases/date">DVD / Blu-ray</a>
                        </li>
                                            <li class="menu_item">
                            <a href="http://www.metacritic.com/browse/movies/release-date/coming-soon/date">Coming Soon</a>
                        </li>
                                            <li class="menu_item">
                            <a href="http://www.metacritic.com/browse/movies/trailers/date">Trailers</a>
                        </li>
                                        </ul>
                </div>
                    </li>
                <li class="nav nav_games has_menu_set">
            <span class="nav_item menu_hover_toggler">
                <span class="nav_item_wrap">
                    <a href="http://www.metacritic.com/game">
                        <span class="nav_text">Games</span>
                    </a>
                                            <span class="menu_click_toggler">»</span>
                                    </span>
            </span>
                            <div id="primary_nav_games_menu" class="menu_items primary_nav_menu">
                    <ul class="menu_items">
                                            <li class="menu_item">
                            <a href="http://www.metacritic.com/game/playstation-4">PS4</a>
                        </li>
                                            <li class="menu_item">
                            <a href="http://www.metacritic.com/game/xbox-one">Xbox One</a>
                        </li>
                                            <li class="menu_item">
                            <a href="http://www.metacritic.com/game/playstation-3">PS3</a>
                        </li>
                                            <li class="menu_item">
                            <a href="http://www.metacritic.com/game/xbox-360">Xbox 360</a>
                        </li>
                                            <li class="menu_item">
                            <a href="http://www.metacritic.com/game/pc">PC</a>
                        </li>
                                            <li class="menu_item">
                            <a href="http://www.metacritic.com/game/wii-u">Wii U</a>
                        </li>
                                            <li class="menu_item">
                            <a href="http://www.metacritic.com/game/3ds">3DS</a>
                        </li>
                                            <li class="menu_item">
                            <a href="http://www.metacritic.com/game/playstation-vita">PS Vita</a>
                        </li>
                                            <li class="menu_item">
                            <a href="http://www.metacritic.com/game/ios">iPhone/iPad</a>
                        </li>
                                            <li class="menu_item">
                            <a href="http://www.metacritic.com/game/legacy">Legacy</a>
                        </li>
                                        </ul>
                </div>
                    </li>
                <li class="nav nav_tv">
            <span class="nav_item">
                <span class="nav_item_wrap">
                    <a href="http://www.metacritic.com/tv">
                        <span class="nav_text">TV</span>
                    </a>
                                    </span>
            </span>
                    </li>
                <li class="nav nav_music">
            <span class="nav_item">
                <span class="nav_item_wrap">
                    <a href="http://www.metacritic.com/music">
                        <span class="nav_text">Music</span>
                    </a>
                                    </span>
            </span>
                    </li>
                <li class="nav nav_features">
            <span class="nav_item">
                <span class="nav_item_wrap">
                    <a href="http://www.metacritic.com/feature">
                        <span class="nav_text">Features</span>
                    </a>
                                    </span>
            </span>
                    </li>
            </ul>
</div>

                <div class="clr"></div>
            </div>
        </div>
        <div id="masthead_secondary">
            <div class="masthead_wrap">
                <div id="secondary_nav">
    <ul class="nav_items secondary_nav">
                <li class="nav">
            <span class="nav_item">
                <span class="nav_item_wrap">
                                                                                    <a href="/browse/movies/release-date/theaters/date">New Releases</a>
                </span>
            </span>
        </li>
                <li class="nav">
            <span class="nav_item">
                <span class="nav_item_wrap">
                                                                                    <a href="/browse/movies/release-date/coming-soon/date">Coming Soon</a>
                </span>
            </span>
        </li>
                <li class="nav">
            <span class="nav_item">
                <span class="nav_item_wrap">
                                                                                    <a href="/browse/movies/score/metascore/90day/filtered">High Scores</a>
                </span>
            </span>
        </li>
                <li class="nav">
            <span class="nav_item">
                <span class="nav_item_wrap">
                                                                                    <a href="/browse/movies/title/dvd">Browse A-Z</a>
                </span>
            </span>
        </li>
                <li class="nav">
            <span class="nav_item">
                <span class="nav_item_wrap">
                                                                                    <a href="/browse/movies/publication/reviewed">Publications</a>
                </span>
            </span>
        </li>
                <li class="nav">
            <span class="nav_item">
                <span class="nav_item_wrap">
                                                                                    <a href="/browse/movies/critic/reviewed">Critics</a>
                </span>
            </span>
        </li>
                <li class="nav">
            <span class="nav_item">
                <span class="nav_item_wrap">
                                                                                    <a href="/browse/movies/people/reviewed">People</a>
                </span>
            </span>
        </li>
                <li class="nav">
            <span class="nav_item">
                <span class="nav_item_wrap">
                                                                                    <a href="/browse/movies/trailers/date">Trailers</a>
                </span>
            </span>
        </li>
            </ul>
</div>


<div id="userpanel">
    <div class="panel_wrap logged_out">
                <div class="user_options">
            <div class="user_options_label">User Panel Options!!</div>
            <ul class="user_options">
                                    <li class="user_option login">
                        <a name="login" href="https://secure.metacritic.com/login">Log In</a>
                    </li>
                    <li class="user_option signup">
                        <a name="signup" href="https://secure.metacritic.com/signup">Sign up</a>
                    </li>

            </ul>
        </div>
    </div>
</div>

            </div>
        </div>
    </div>

                        <div id="mantle_skin" class="site_gutters">
                        <div id="gutters" class="site_gutters">
                    <div id="superleader">
        <div id="leader_plus_top" class="ad_unit">

                            <script type="text/javascript">

                        googletag.cmd.push(function() {

                                                            window.metac_g_ad_leader_plus_top = googletag.defineSlot("/8264/aw-metacritic/movies",[[728,90],[970,66],[970,250],[728,91]], "leader_plus_top").addService(googletag.pubads()).setTargeting("pos", "top");


                        });


                        window.metac_ads_pushdisplay.push("leader_plus_top");
                                    </script>
                            <div id="google_ads_iframe_/8264/aw-metacritic/movies_1__container__" style="border: 0pt none;"><iframe id="google_ads_iframe_/8264/aw-metacritic/movies_1" title="3rd party ad content" name="google_ads_iframe_/8264/aw-metacritic/movies_1" width="728" height="90" scrolling="no" marginwidth="0" marginheight="0" frameborder="0" src="javascript:&quot;<html><body style='background:transparent'></body></html>&quot;" style="border: 0px; vertical-align: bottom;"></iframe></div></div>


</div>
                <div id="gutters_mid" class="site_gutters">
            <div id="gutters_btm" class="site_gutters">
                <div id="gutters_top" class="site_gutters">
                    <div id="container">

<div id="col_layout" class="col_layout">
        <div id="main_content" class="content_section mpu_layout">
                <div class="layout">


                        <div id="main" class="col main_col">
                <div class="content_head product_content_head movie_content_head">



<div class="sharing ">

    <a class="sharing-facebook" title="Share on Facebook" rel="nofollow popup:external" data-mc-social-url="http://www.metacritic.com/movie/spider-man-3?ftag=fbsoshares" href="javascript:void(0);"><span class="fa fa-fw fa-facebook"></span></a><a class="sharing-twitter" title="Share on Twitter" rel="nofollow popup:external" href="http://twitter.com/intent/tweet?via=metacritic&amp;text=Read%20User%20Reviews%20and%20Submit%20your%20own%20for%20Spider-Man%203&amp;url=http%3A%2F%2Fmtcr.tc%2F1i0om9w" target="_blank"><span class="fa fa-fw fa-twitter"></span></a><a class="sharing-pinterest" title="Share on Pinterest" rel="nofollow popup:external" data-mc-social-track-id="5" target="_blank" href="//pinterest.com/pin/create/link/?url=http%3A%2F%2Fwww.metacritic.com%2Fmovie%2Fspider-man-3%3Fftag%3Dpinsoshares&amp;description=Read%20User%20Reviews%20and%20Submit%20your%20own%20for%20Spider-Man%203&amp;media=http://static.metacritic.com/images/products/movies/2/04da79f8424a5c379c0ca5847deeb540-98.jpg"><span class="fa fa-fw fa-pinterest"></span></a><a class="sharing-google-plus" title="Share on Google+" rel="nofollow popup:external" data-mc-social-track-id="3" target="_blank" href="https://plus.google.com/share?url=http%3A%2F%2Fwww.metacritic.com%2Fmovie%2Fspider-man-3%3Fftag%3Dgplussoshares" "=""><span class="fa fa-fw fa-google-plus"></span></a><a class="sharing-reddit" title="Share on Reddit" rel="nofollow popup:external" data-mc-social-track-id="6" target="_blank" href="http://www.reddit.com/submit?url=http%3A%2F%2Fwww.metacritic.com%2Fmovie%2Fspider-man-3%3Fftag%3Dredsoshares&amp;title=Read%20User%20Reviews%20and%20Submit%20your%20own%20for%20Spider-Man%203"><span class="fa fa-fw fa-reddit"></span></a>
    </div>


        <h1 class="product_title">
	        <a href="/movie/spider-man-3" class="hover_none">
                        Spider-Man 3
                    </a>

        </h1>
    <div class="product_data">
        <ul class="summary_details">
							<li class="summary_detail publisher">
					<span class="label">Studio:</span>
					<span class="data">
                        <a href="/company/columbia-pictures">
                                                        Columbia Pictures
                                                    </a>
					</span>
				</li>
						<li class="summary_detail release_data">
				<span class="label">Release Date:</span>
									<span class="data">
                        May 4, 2007
                    </span>
							</li>
        </ul>
    </div>
</div>



    <div class="content_nav">
        <ul class="nav_items content_nav">
                            <li class="nav nav_summary first_nav">
                    <span class="nav_item">
                        <span class="nav_item_wrap">
                                                            <a class="action" href="/movie/spider-man-3">Summary</a>
                                                    </span>
                    </span>
                </li>
                            <li class="nav nav_critic_reviews">
                    <span class="nav_item">
                        <span class="nav_item_wrap">
                                                            <a class="action" href="/movie/spider-man-3/critic-reviews">Critic Reviews</a>
                                                    </span>
                    </span>
                </li>
                            <li class="nav nav_user_reviews active_nav">
                    <span class="nav_item">
                        <span class="nav_item_wrap">
                                                            <span class="action">User Reviews</span>
                                                    </span>
                    </span>
                </li>
                            <li class="nav nav_details">
                    <span class="nav_item">
                        <span class="nav_item_wrap">
                                                            <a class="action" href="/movie/spider-man-3/details">Details &amp; Credits</a>
                                                    </span>
                    </span>
                </li>
                            <li class="nav nav_trailers last_nav">
                    <span class="nav_item">
                        <span class="nav_item_wrap">
                                                            <a class="action" href="/movie/spider-man-3/trailers">Trailers &amp; Videos</a>
                                                    </span>
                    </span>
                </li>
                    </ul>
    </div>







<div class="module score_details_module"><div class="score_details userscore_details">
        <div class="score_summary">
    <div class="userscore_wrap feature_userscore">
        <div class="label">User Score</div>

<div class="metascore_w user large movie positive">6.7</div>



        <div class="summary">
            <p><span class="desc">Generally favorable reviews</span><span class="count"><span class="separator">- </span><span class="based">based on</span> <strong>1219 Ratings</strong></span></p>
        </div>
    </div>
</div>
    <div class="score_distribution">
    <div class="distribution_wrap">
        <div class="distribution_title">User score distribution:</div>
        <ol class="score_counts">
                        <li class="score_count">
                <div class="count_wrap">
                    <span class="label">Positive:</span>
                    <span class="data">
                        <a href="/movie/spider-man-3/user-reviews?dist=positive">                            <span class="total" style="width:100%;">
                                <span class="count">693</span>
                                <span class="distribution positive"> out of 1219</span>
                            </span>
                        </a>                    </span>
                </div>
            </li>
                        <li class="score_count">
                <div class="count_wrap">
                    <span class="label">Mixed:</span>
                    <span class="data">
                        <a href="/movie/spider-man-3/user-reviews?dist=neutral">                            <span class="total" style="width:42%;">
                                <span class="count">290</span>
                                <span class="distribution mixed"> out of 1219</span>
                            </span>
                        </a>                    </span>
                </div>
            </li>
                        <li class="score_count">
                <div class="count_wrap">
                    <span class="label">Negative:</span>
                    <span class="data">
                        <a href="/movie/spider-man-3/user-reviews?dist=negative">                            <span class="total" style="width:34%;">
                                <span class="count">236</span>
                                <span class="distribution negative"> out of 1219</span>
                            </span>
                        </a>                    </span>
                </div>
            </li>
                    </ol>
		    </div>
</div>

</div>
</div>



























<div class="esite_list where_esite_list"><div class="module"><div class="head head_type_1"><div class="head_wrap"><h2 class="module_title">Where To Watch</h2></div></div></div><div class="esite_items clearfix list_expand_wrapper">


<div class="esite_btn_wrapper">
    <div class="esite_btn esite_amazon esite_aiv" title="Watch Now with Amazon Instant Video">
        <table>
            <tbody><tr>
                <td class="esite_label_wrapper">
                    <span>Stream On</span>
                </td>
                <td class="esite_img_wrapper">
                    <a rel="nofollow" target="_blank" class="esite_url" href="http://www.amazon.com/dp/B000UU4NE4%3FSubscriptionId%3DAKIAJHSMUOWEQCQ7QDAQ%26tag%3Dmetacritic_aiv_product-20%26linkCode%3Dxm2%26camp%3D2025%26creative%3D165953%26creativeASIN%3DB000UU4NE4" data-leadtype="Digital Product" data-leadtag="metacritic_aiv_product-20" data-leadid="1" data-leadname="amazon" data-leadplace="upper body">
                        <img src="/images/buttons/esites/amazon_iv_30.png">
                    </a>
                </td>
            </tr>
        </tbody></table>
    </div>
</div>


<div class="esite_btn_wrapper">
    <div class="esite_btn esite_itunes" title="Watch Now on iTunes">
        <table>
            <tbody><tr>
                <td class="esite_label_wrapper">
                    <span>Stream On</span>
                </td>
                <td class="esite_img_wrapper">
                    <a rel="nofollow" target="itunes_store" class="esite_url" href="http://itunes.apple.com/video/spider-man-3/id270784998?uo=5&amp;at=1l3vbvV&amp;ct=ProductPage" data-leadtype="Digital Product" data-leadtag="1l3vbvV" data-leadid="3" data-leadname="apple" data-leadplace="upper body">
                        <img src="/images/buttons/esites/badge_itunes-lrg2.svg">
                    </a>
                </td>
            </tr>
        </tbody></table>
    </div>
</div></div><script type="text/javascript">window.eventAmazonBuyView = true;</script></div>


<div class="partial_wrap">

<div class="module review_product_module">
    <div class="head head_type_1"><div class="head_wrap"><h2 class="module_title">Review this movie</h2></div></div>
    <div class="body">
                    <div class="review_product user_input_form user_input_disabled">
                <div class="user_input_wrap review_product_wrap">
                    <ol class="form_fields">
                        <li class="form_field review_score">
                            <div class="field_wrap">



        <div class="score_summary yourscore_summary {'review_id': '0', 'request_url': '/jl/rate/set-rating?product_type=movie&amp;title=Spider-Man+3&amp;release_date=2007-05-04+00%3A00%3A00&amp;ref_type_id=150&amp;ref_id=500252'} ">
    <div class="yourscore_wrap">
        <div class="label label_movie">Your Score</div>
        <div class="data yourscore">
            <span class="score_value">0</span>
            <span class="score_total">out of 10</span>
        </div>
        <div class="summary feedback has_feedback">
                    <p class="rating_error"></p>
                    </div>


        <div class="rating_picker rating_picker_movie">
                    <input type="hidden" name="review_score" value="">
                    <div class="rating_picker_std">
                <div class="rating_label">Rate this:</div>
                <ul class="rating_actions rating_values  ">
                <input type="hidden" name="csrf" value="32c5a2710a2f72c75787154e0478b540">
                                    <li class="rating_value_item rating_value_100">
                        <div class="rating_action  rating_action_100 " rel="nofollow" data-rateref="#10" title="Rate 10 out of 10">
                                <span class="rating_value">10</span>
                        </div>
                    </li>
                                    <li class="rating_value_item rating_value_90">
                        <div class="rating_action  rating_action_90 " rel="nofollow" data-rateref="#9" title="Rate 9 out of 10">
                                <span class="rating_value">9</span>
                        </div>
                    </li>
                                    <li class="rating_value_item rating_value_80">
                        <div class="rating_action  rating_action_80 " rel="nofollow" data-rateref="#8" title="Rate 8 out of 10">
                                <span class="rating_value">8</span>
                        </div>
                    </li>
                                    <li class="rating_value_item rating_value_70">
                        <div class="rating_action  rating_action_70 " rel="nofollow" data-rateref="#7" title="Rate 7 out of 10">
                                <span class="rating_value">7</span>
                        </div>
                    </li>
                                    <li class="rating_value_item rating_value_60">
                        <div class="rating_action  rating_action_60 " rel="nofollow" data-rateref="#6" title="Rate 6 out of 10">
                                <span class="rating_value">6</span>
                        </div>
                    </li>
                                    <li class="rating_value_item rating_value_50">
                        <div class="rating_action  rating_action_50 " rel="nofollow" data-rateref="#5" title="Rate 5 out of 10">
                                <span class="rating_value">5</span>
                        </div>
                    </li>
                                    <li class="rating_value_item rating_value_40">
                        <div class="rating_action  rating_action_40 " rel="nofollow" data-rateref="#4" title="Rate 4 out of 10">
                                <span class="rating_value">4</span>
                        </div>
                    </li>
                                    <li class="rating_value_item rating_value_30">
                        <div class="rating_action  rating_action_30 " rel="nofollow" data-rateref="#3" title="Rate 3 out of 10">
                                <span class="rating_value">3</span>
                        </div>
                    </li>
                                    <li class="rating_value_item rating_value_20">
                        <div class="rating_action  rating_action_20 " rel="nofollow" data-rateref="#2" title="Rate 2 out of 10">
                                <span class="rating_value">2</span>
                        </div>
                    </li>
                                    <li class="rating_value_item rating_value_10">
                        <div class="rating_action  rating_action_10 " rel="nofollow" data-rateref="#1" title="Rate 1 out of 10">
                                <span class="rating_value">1</span>
                        </div>
                    </li>
                                    <li class="rating_value_item rating_value_0">
                        <div class="rating_action  rating_action_0 " rel="nofollow" data-rateref="#0" title="Rate 0 out of 10">
                                <span class="rating_value">0</span>
                        </div>
                    </li>
                                    <li class="rating_value_item rating_value_delete">
                        <div class="rating_action  rating_action_delete " rel="nofollow" data-rateref="#-1" title="Delete rating">
                                <span class="rating_value">0</span>
                        </div>
                    </li>
                                </ul>
            </div>


            <div class="rating_values  scale disabled">
                <div class="status"></div>
            </div>
        </div>
    </div>
</div>




<div class="rating_signin_tmpl">
    <div class="message">
        Log in to finish rating <span class="product_name">Spider-Man 3</span>
    </div>

    <div class="product_data">
        <div class="product_media">
            <div class="product_image large_image">
                <img class="product_image large_image" src="http://static.metacritic.com/images/products/movies/2/04da79f8424a5c379c0ca5847deeb540-98.jpg" alt="Spider-Man 3 Image">
            </div>
        </div>
        <div class="yourscore_login_wrapper">
            <div class="product_name_wrapper">
                <span class="product_name">Spider-Man 3</span>
            </div>
            <div class="score_summary yourscore_login">
                <div class="protector"></div>
                <div class="yourscore_wrap">
                    <div class="label label_movie">Your Score</div>
                    <div class="data yourscore">
                        <span class="score_value">0</span>
                        <span class="score_total">out of 10</span>
                    </div>
                    <div class="summary feedback">
                    </div>


                    <div class="rating_picker rating_picker_movie">
                        <input type="hidden" name="review_score" value="0">

                        <div class="rating_picker_std">
                            <div class="rating_label">Rate this:</div>
                            <ul class="rating_actions rating_values  ">
                                <input type="hidden" name="csrf" value="32c5a2710a2f72c75787154e0478b540">
                                                                    <li class="rating_value_item rating_value_100">
                                        <div class="rating_action  rating_action_100 " rel="nofollow" title="Rate 10 out of 10" data-rateref="/jl/rate/set-rating?score=10&amp;ref_type_id=150&amp;ref_id=500252">
                                            <span class="rating_value">10</span>
                                        </div>
                                    </li>
                                                                    <li class="rating_value_item rating_value_90">
                                        <div class="rating_action  rating_action_90 " rel="nofollow" title="Rate 9 out of 10" data-rateref="/jl/rate/set-rating?score=9&amp;ref_type_id=150&amp;ref_id=500252">
                                            <span class="rating_value">9</span>
                                        </div>
                                    </li>
                                                                    <li class="rating_value_item rating_value_80">
                                        <div class="rating_action  rating_action_80 " rel="nofollow" title="Rate 8 out of 10" data-rateref="/jl/rate/set-rating?score=8&amp;ref_type_id=150&amp;ref_id=500252">
                                            <span class="rating_value">8</span>
                                        </div>
                                    </li>
                                                                    <li class="rating_value_item rating_value_70">
                                        <div class="rating_action  rating_action_70 " rel="nofollow" title="Rate 7 out of 10" data-rateref="/jl/rate/set-rating?score=7&amp;ref_type_id=150&amp;ref_id=500252">
                                            <span class="rating_value">7</span>
                                        </div>
                                    </li>
                                                                    <li class="rating_value_item rating_value_60">
                                        <div class="rating_action  rating_action_60 " rel="nofollow" title="Rate 6 out of 10" data-rateref="/jl/rate/set-rating?score=6&amp;ref_type_id=150&amp;ref_id=500252">
                                            <span class="rating_value">6</span>
                                        </div>
                                    </li>
                                                                    <li class="rating_value_item rating_value_50">
                                        <div class="rating_action  rating_action_50 " rel="nofollow" title="Rate 5 out of 10" data-rateref="/jl/rate/set-rating?score=5&amp;ref_type_id=150&amp;ref_id=500252">
                                            <span class="rating_value">5</span>
                                        </div>
                                    </li>
                                                                    <li class="rating_value_item rating_value_40">
                                        <div class="rating_action  rating_action_40 " rel="nofollow" title="Rate 4 out of 10" data-rateref="/jl/rate/set-rating?score=4&amp;ref_type_id=150&amp;ref_id=500252">
                                            <span class="rating_value">4</span>
                                        </div>
                                    </li>
                                                                    <li class="rating_value_item rating_value_30">
                                        <div class="rating_action  rating_action_30 " rel="nofollow" title="Rate 3 out of 10" data-rateref="/jl/rate/set-rating?score=3&amp;ref_type_id=150&amp;ref_id=500252">
                                            <span class="rating_value">3</span>
                                        </div>
                                    </li>
                                                                    <li class="rating_value_item rating_value_20">
                                        <div class="rating_action  rating_action_20 " rel="nofollow" title="Rate 2 out of 10" data-rateref="/jl/rate/set-rating?score=2&amp;ref_type_id=150&amp;ref_id=500252">
                                            <span class="rating_value">2</span>
                                        </div>
                                    </li>
                                                                    <li class="rating_value_item rating_value_10">
                                        <div class="rating_action  rating_action_10 " rel="nofollow" title="Rate 1 out of 10" data-rateref="/jl/rate/set-rating?score=1&amp;ref_type_id=150&amp;ref_id=500252">
                                            <span class="rating_value">1</span>
                                        </div>
                                    </li>
                                                                    <li class="rating_value_item rating_value_0">
                                        <div class="rating_action  rating_action_0 " rel="nofollow" title="Rate 0 out of 10" data-rateref="/jl/rate/set-rating?score=0&amp;ref_type_id=150&amp;ref_id=500252">
                                            <span class="rating_value">0</span>
                                        </div>
                                    </li>
                                                                    <li class="rating_value_item rating_value_delete">
                                        <div class="rating_action  rating_action_delete " rel="nofollow" title="Delete rating" data-rateref="/jl/rate/set-rating?score=-1&amp;ref_type_id=150&amp;ref_id=500252">
                                            <span class="rating_value">                                                0</span>
                                        </div>
                                    </li>
                                                            </ul>
                        </div>
                    </div>
                </div>
            </div>

            <div>
                <div class="score_details userscore_details">
                        <div class="score_summary">
    <div class="userscore_wrap feature_userscore">
        <div class="label">User Score</div>

<div class="metascore_w user large movie positive">6.7</div>



        <div class="summary">
            <p><span class="desc">Generally favorable reviews</span><span class="count"><span class="separator">- </span><span class="based">based on</span> <strong>1219 Ratings</strong></span></p>
        </div>
    </div>
</div>
                </div>
            </div>
        </div>
        <div class="clr"></div>
    </div>

    <div class="login_wrapper" data-fbenabled="1">
    </div>
    <div class="after_login">
        <div class="after_message">Would you like to write a review?</div>
        <div class="login_success">
            <input class="BUTTON bigger" type="button" name="review" value="Write a Review" data-href="/movie/spider-man-3/user-reviews">
            <input class="BUTTON bigger gray" type="button" name="close" value="Close">
            <hr>

                                                                                                <div>
                    <div class="share_message">Share this?</div>


<div class="inline_social product_social">

            <div class="inline_social_button">
            <iframe id="twitter-widget-0" scrolling="no" frameborder="0" allowtransparency="true" class="twitter-share-button twitter-share-button-rendered twitter-tweet-button" title="Twitter Tweet Button" src="http://platform.twitter.com/widgets/tweet_button.b41e99df00581dc95d7fdd63f3283511.en.html#dnt=false&amp;id=twitter-widget-0&amp;lang=en&amp;original_referer=http%3A%2F%2Fwww.metacritic.com%2Fmovie%2Fspider-man-3%2Fuser-reviews%3Fpage%3D1&amp;size=m&amp;text=Read%20User%20Reviews%20and%20Submit%20your%20own%20for%20Spider-Man%203%20-%20Metacritic&amp;time=1468819706181&amp;type=share&amp;url=http%3A%2F%2Fmtcr.tc%2F1i0om9w&amp;via=metacritic" data-url="http://mtcr.tc/1i0om9w" style="position: static; visibility: visible; width: 63px; height: 20px;"></iframe>
        </div>
                <div class="inline_social_button facebook_sharing">
        <noscript>
            &lt;a href="http://www.facebook.com/sharer/sharer.php?u=http://www.metacritic.com/movie/spider-man-3&amp;t=Read User Reviews and Submit your own for Spider-Man 3" rel="nofollow popup:external"&gt;
                &lt;img src="/images/buttons/facebook_inline.png" alt="Share this on Facebook" rel="nofollow" /&gt;
            &lt;/a&gt;
        </noscript>
        <fb:like href="http://www.metacritic.com/movie/spider-man-3" send="false" layout="button_count" width="100" show_faces="false" font="" class=" fb_iframe_widget" fb-xfbml-state="rendered" fb-iframe-plugin-query="app_id=123113677890173&amp;container_width=0&amp;href=http%3A%2F%2Fwww.metacritic.com%2Fmovie%2Fspider-man-3&amp;layout=button_count&amp;locale=en_US&amp;sdk=joey&amp;send=false&amp;show_faces=false&amp;width=100"><span style="vertical-align: bottom; width: 80px; height: 20px;"><iframe name="f1117d7b8cdbe8c" width="100px" height="1000px" frameborder="0" allowtransparency="true" allowfullscreen="true" scrolling="no" title="fb:like Facebook Social Plugin" src="https://www.facebook.com/v2.6/plugins/like.php?app_id=123113677890173&amp;channel=http%3A%2F%2Fstaticxx.facebook.com%2Fconnect%2Fxd_arbiter%2Fr%2Fbz-D0tzmBsw.js%3Fversion%3D42%23cb%3Dfadf53e5e758d%26domain%3Dwww.metacritic.com%26origin%3Dhttp%253A%252F%252Fwww.metacritic.com%252Ff654a175f6b1d%26relation%3Dparent.parent&amp;container_width=0&amp;href=http%3A%2F%2Fwww.metacritic.com%2Fmovie%2Fspider-man-3&amp;layout=button_count&amp;locale=en_US&amp;sdk=joey&amp;send=false&amp;show_faces=false&amp;width=100" class="" style="border: none; visibility: visible; width: 80px; height: 20px;"></iframe></span></fb:like>
        </div>
    </div>
                <div style="clear: both;"></div>
                </div>
                    </div>
    </div>
    <div style="clear:both;"></div>
</div>

                                                            </div>
                        </li>
                        <li class="form_field review_body">
                            <div class="label">
                                <label for="review_body">Review:</label>
                            </div>
                            <div class="data">
                                                                    <p class="msg login_msg">
                                        Please <a href="https://secure.metacritic.com/login">sign in</a> or <a name="signup" href="https://secure.metacritic.com/signup">create an account</a> before writing a review.
                                    </p>
                                                            </div>
                        </li>
                        <li class="form_field review_spoiler">
                            <div class="field_wrap">
                                <div class="label">
                                    <label for="review_spoiler">Check box if your review contains spoilers</label>
                                </div>
                                <div class="data">
                                    <input type="checkbox" disabled="disabled">
                                </div>
                            </div>
                        </li>
                    </ol>


<div class="form_actions">
        <ol class="form_actions">
        <li class="form_action post_form">
            <div class="btn submit">
                <div class="btn_wrap">
                    <div class="btn_text">Submit</div>
                </div>
            </div>
        </li>
                <li class="form_action spellcheck_form">
            <div class="btn submit">
                <div class="btn_wrap">
                    <div class="btn_text">Check Spelling</div>
                </div>
            </div>
        </li>
                    </ol>
</div>

                </div>
            </div>
            </div>
</div>


<div class="module nobtm">
    <div class="head head_type_1"><div class="head_wrap"><h2 class="module_title">User Reviews</h2></div></div>
</div>


<div class="module reviews_module user_reviews_module">

        <div class="body product_reviews">
                            <div class="tabs ">
        <div class="tab_wrap">
                            <ul class="tabs tabs_type_1">            <li class="tab tab_type_1 tab_sort-score first">
                                                        <a href="/movie/spider-man-3/user-reviews?sort-by=score&amp;num_items=100"><span>User score</span></a>
                            </li>
                                                        <li class="tab tab_type_1 tab_sort-date">
                                                        <a href="/movie/spider-man-3/user-reviews?sort-by=date&amp;num_items=100"><span>By date</span></a>
                            </li>
                                                        <li class="tab tab_type_1 tab_sort-most-helpful last">
                                    <span class="active"><span>Most helpful</span></span>
                            </li>
            </ul>
            <div class="tab_options_wrap">
                            <div class="page_nav_options">
    <div class="options_wrap">
        <div class="label">view</div>
        <div class="options">
            <ul class="options">
                <li class="option">
                                                                <a href="/movie/spider-man-3/user-reviews?sort-by=most-helpful&amp;num_items=30"><span>30</span></a>
                                    </li>
                <li class="option">
                                                                <span>100</span>
                                    </li>
            </ul>
        </div>
        <div class="desc">per page</div>
    </div>
</div>

                                </div>


            </div>
    </div>



                                                    <ol class="reviews user_reviews">                                <li id="user_review_272063" class="review user_review first_review">
                    <div class="review_btm review_btm_r"><div class="review_btm review_btm_l"><div class="review_top review_top_r"><div class="review_top review_top_l">
                        <div class="review_content">
                            <div class="review_section">
                                <div class="review_stats">
                                    <div class="review_critic">
                                        <div class="name">
                                                                                            <span>ChrisA.</span>
                                                                                                                                </div>
                                                                                    <div class="date">May  5, 2007</div>
                                                                            </div>

                                    <div class="review_grade">

<div class="metascore_w user medium movie positive indiv perfect">10</div>

                                    </div>
                                </div>
                                <div class="review_body">

                                        <span> Powerfully gripping, and touching film, and Harry Osborn was actually good in this film. Too bad the Eddie Brock character seemed inconsistent, and the plot seemed rushed. Haydn Church was great in the bit role as the down on his luck, the good-hearted but criminally Sandman, and this film was awesome. Good storyline, and buddy buddy film.</span>
            </div>
                            </div>
                                                        <div class="review_section review_actions ">
                                <ul class="review_actions">
                                                                            <li class="review_action review_helpful">
                                            <div class="review_helpful">
    <div class="rating_thumbs">
        			<div class="helpful_summary thumb_count">
				<a href="https://secure.metacritic.com/login">
				<span class="total_ups">0</span>
				of
				<span class="total_thumbs">0</span>
				users found this helpful
                </a>
			</div>
                <div style="clear:both;"></div>
    </div>
</div>
                                        </li>
                                                                                                                                            </ul>
                            </div>
                                                    </div>
                    </div></div></div></div>
                </li>
                                                                                    <li id="user_review_272138" class="review user_review">
                    <div class="review_btm review_btm_r"><div class="review_btm review_btm_l"><div class="review_top review_top_r"><div class="review_top review_top_l">
                        <div class="review_content">
                            <div class="review_section">
                                <div class="review_stats">
                                    <div class="review_critic">
                                        <div class="name">
                                                                                            <span>Snortch</span>
                                                                                                                                </div>
                                                                                    <div class="date">May  5, 2007</div>
                                                                            </div>

                                    <div class="review_grade">

<div class="metascore_w user medium movie negative indiv">1</div>

                                    </div>
                                </div>
                                <div class="review_body">

                                        <span class="inline_expand_collapse inline_collapsed" id="review_blurb_272138"><span class="blurb blurb_collapsed"> This movie has about as appealing as freshly mowed over dog poop. I love SM and I enjoyed the first 2, but this one was really a waste. My eyes about rolled to the back of my head in several scenes...especially the contrived spidey swinging in slow motion in front of the American flag...as if to say that Venom and Sandman are the terrorists...was surprised that the Proud to be American</span><span class="blurb blurb_expanded"> This movie has about as appealing as freshly mowed over dog poop. I love SM and I enjoyed the first 2, but this one was really a waste. My eyes about rolled to the back of my head in several scenes...especially the contrived spidey swinging in slow motion in front of the American flag...as if to say that Venom and Sandman are the terrorists...was surprised that the Proud to be American song didnt make it in there. Guhhh...what a waste!</span><span class="blurb_etc">…</span> <a rel="nofollow" class="toggle_expand_collapse toggle_expand" href="/movie/spider-man-3/user-reviews?page=1&amp;user_review_id=272138">Expand</a></span>
            </div>
                            </div>
                                                        <div class="review_section review_actions ">
                                <ul class="review_actions">
                                                                            <li class="review_action review_helpful">
                                            <div class="review_helpful">
    <div class="rating_thumbs">
        			<div class="helpful_summary thumb_count">
				<a href="https://secure.metacritic.com/login">
				<span class="total_ups">0</span>
				of
				<span class="total_thumbs">0</span>
				users found this helpful
                </a>
			</div>
                <div style="clear:both;"></div>
    </div>
</div>
                                        </li>
                                                                                                                                            </ul>
                            </div>
                                                    </div>
                    </div></div></div></div>
                </li>
                                                                                    <li id="user_review_272137" class="review user_review">
                    <div class="review_btm review_btm_r"><div class="review_btm review_btm_l"><div class="review_top review_top_r"><div class="review_top review_top_l">
                        <div class="review_content">
                            <div class="review_section">
                                <div class="review_stats">
                                    <div class="review_critic">
                                        <div class="name">
                                                                                            <span>ChuckB.</span>
                                                                                                                                </div>
                                                                                    <div class="date">May  5, 2007</div>
                                                                            </div>

                                    <div class="review_grade">

<div class="metascore_w user medium movie negative indiv">3</div>

                                    </div>
                                </div>
                                <div class="review_body">

                                        <span> Predicable story and film school dialogue </span>
            </div>
                            </div>
                                                        <div class="review_section review_actions ">
                                <ul class="review_actions">
                                                                            <li class="review_action review_helpful">
                                            <div class="review_helpful">
    <div class="rating_thumbs">
        			<div class="helpful_summary thumb_count">
				<a href="https://secure.metacritic.com/login">
				<span class="total_ups">0</span>
				of
				<span class="total_thumbs">0</span>
				users found this helpful
                </a>
			</div>
                <div style="clear:both;"></div>
    </div>
</div>
                                        </li>
                                                                                                                                            </ul>
                            </div>
                                                    </div>
                    </div></div></div></div>
                </li>
                                                                                    <li id="user_review_272056" class="review user_review">
                    <div class="review_btm review_btm_r"><div class="review_btm review_btm_l"><div class="review_top review_top_r"><div class="review_top review_top_l">
                        <div class="review_content">
                            <div class="review_section">
                                <div class="review_stats">
                                    <div class="review_critic">
                                        <div class="name">
                                                                                            <span>DavidR.</span>
                                                                                                                                </div>
                                                                                    <div class="date">May  5, 2007</div>
                                                                            </div>

                                    <div class="review_grade">

<div class="metascore_w user medium movie negative indiv">2</div>

                                    </div>
                                </div>
                                <div class="review_body">

                                        <span> I was generous with this high of a rating. The movie was awful!! I went to see an action film not a stupid comedy. Putting a huge american flag behind spider man is ridiculous!! Venom is a beast in the comics but he is merely a witty Topher Grace in this one. DO NOT see this movie if you like the first 2. Like X-Men they ruined the whole serious in one shot.</span>
            </div>
                            </div>
                                                        <div class="review_section review_actions ">
                                <ul class="review_actions">
                                                                            <li class="review_action review_helpful">
                                            <div class="review_helpful">
    <div class="rating_thumbs">
        			<div class="helpful_summary thumb_count">
				<a href="https://secure.metacritic.com/login">
				<span class="total_ups">0</span>
				of
				<span class="total_thumbs">0</span>
				users found this helpful
                </a>
			</div>
                <div style="clear:both;"></div>
    </div>
</div>
                                        </li>
                                                                                                                                            </ul>
                            </div>
                                                    </div>
                    </div></div></div></div>
                </li>
                                                                                    <li id="user_review_272076" class="review user_review">
                    <div class="review_btm review_btm_r"><div class="review_btm review_btm_l"><div class="review_top review_top_r"><div class="review_top review_top_l">
                        <div class="review_content">
                            <div class="review_section">
                                <div class="review_stats">
                                    <div class="review_critic">
                                        <div class="name">
                                                                                            <span>BigRed</span>
                                                                                                                                </div>
                                                                                    <div class="date">May  5, 2007</div>
                                                                            </div>

                                    <div class="review_grade">

<div class="metascore_w user medium movie mixed indiv">6</div>

                                    </div>
                                </div>
                                <div class="review_body">

                                        <span> Who would have thought that I would actually want to leave a Spider-Man movie?</span>
            </div>
                            </div>
                                                        <div class="review_section review_actions ">
                                <ul class="review_actions">
                                                                            <li class="review_action review_helpful">
                                            <div class="review_helpful">
    <div class="rating_thumbs">
        			<div class="helpful_summary thumb_count">
				<a href="https://secure.metacritic.com/login">
				<span class="total_ups">0</span>
				of
				<span class="total_thumbs">0</span>
				users found this helpful
                </a>
			</div>
                <div style="clear:both;"></div>
    </div>
</div>
                                        </li>
                                                                                                                                            </ul>
                            </div>
                                                    </div>
                    </div></div></div></div>
                </li>
                                                                                    <li id="user_review_272058" class="review user_review">
                    <div class="review_btm review_btm_r"><div class="review_btm review_btm_l"><div class="review_top review_top_r"><div class="review_top review_top_l">
                        <div class="review_content">
                            <div class="review_section">
                                <div class="review_stats">
                                    <div class="review_critic">
                                        <div class="name">
                                                                                            <span>JustinS.</span>
                                                                                                                                </div>
                                                                                    <div class="date">May  5, 2007</div>
                                                                            </div>

                                    <div class="review_grade">

<div class="metascore_w user medium movie negative indiv">2</div>

                                    </div>
                                </div>
                                <div class="review_body">

                                        <span> A few good action sequences can't make up for the woeful and overstuffed plot.</span>
            </div>
                            </div>
                                                        <div class="review_section review_actions ">
                                <ul class="review_actions">
                                                                            <li class="review_action review_helpful">
                                            <div class="review_helpful">
    <div class="rating_thumbs">
        			<div class="helpful_summary thumb_count">
				<a href="https://secure.metacritic.com/login">
				<span class="total_ups">0</span>
				of
				<span class="total_thumbs">0</span>
				users found this helpful
                </a>
			</div>
                <div style="clear:both;"></div>
    </div>
</div>
                                        </li>
                                                                                                                                            </ul>
                            </div>
                                                    </div>
                    </div></div></div></div>
                </li>
                                                                                    <li id="user_review_272080" class="review user_review">
                    <div class="review_btm review_btm_r"><div class="review_btm review_btm_l"><div class="review_top review_top_r"><div class="review_top review_top_l">
                        <div class="review_content">
                            <div class="review_section">
                                <div class="review_stats">
                                    <div class="review_critic">
                                        <div class="name">
                                                                                            <span>BenjaminB.</span>
                                                                                                                                </div>
                                                                                    <div class="date">May  5, 2007</div>
                                                                            </div>

                                    <div class="review_grade">

<div class="metascore_w user medium movie positive indiv">7</div>

                                    </div>
                                </div>
                                <div class="review_body">

                                        <span class="inline_expand_collapse inline_collapsed" id="review_blurb_272080"><span class="blurb blurb_collapsed">The problem with this movie are that there are too many unneccessary scenes. do you want to see how MJ and Harry are cooking, do you want to see how peter is dancing to express his evil character traits, or do you want to see how he tries to be a macho? I don't want. Maybe they were ment to be ironic, but they were too normal to be ironic and too stupid to be normal. the other movies</span><span class="blurb blurb_expanded">The problem with this movie are that there are too many unneccessary scenes. do you want to see how MJ and Harry are cooking, do you want to see how peter is dancing to express his evil character traits, or do you want to see how he tries to be a macho? I don't want. Maybe they were ment to be ironic, but they were too normal to be ironic and too stupid to be normal. the other movies had no ironie in it, so no one in the cinema got that it was (maybe) ment to be ironic. without these stupid scenes and a little bit more fighting-action I would give it a 10.</span><span class="blurb_etc">…</span> <a rel="nofollow" class="toggle_expand_collapse toggle_expand" href="/movie/spider-man-3/user-reviews?page=1&amp;user_review_id=272080">Expand</a></span>
            </div>
                            </div>
                                                        <div class="review_section review_actions ">
                                <ul class="review_actions">
                                                                            <li class="review_action review_helpful">
                                            <div class="review_helpful">
    <div class="rating_thumbs">
        			<div class="helpful_summary thumb_count">
				<a href="https://secure.metacritic.com/login">
				<span class="total_ups">0</span>
				of
				<span class="total_thumbs">0</span>
				users found this helpful
                </a>
			</div>
                <div style="clear:both;"></div>
    </div>
</div>
                                        </li>
                                                                                                                                            </ul>
                            </div>
                                                    </div>
                    </div></div></div></div>
                </li>
                                                                                    <li id="user_review_272081" class="review user_review">
                    <div class="review_btm review_btm_r"><div class="review_btm review_btm_l"><div class="review_top review_top_r"><div class="review_top review_top_l">
                        <div class="review_content">
                            <div class="review_section">
                                <div class="review_stats">
                                    <div class="review_critic">
                                        <div class="name">
                                                                                            <span>Moo</span>
                                                                                                                                </div>
                                                                                    <div class="date">May  5, 2007</div>
                                                                            </div>

                                    <div class="review_grade">

<div class="metascore_w user medium movie negative indiv">3</div>

                                    </div>
                                </div>
                                <div class="review_body">

                                        <span> The worst superhero movie I have seen so far. Even ELEKTRA and the 1st FF movie was better than this one. Stupid dialogue (nearly as crap as in STAR WARS), lame actors (or rather flat characters), too exaggerated fighting scences, boring script (Uncle Ben RIP!?).The only things I liked were the supporting actors like Bruce Campbell and the very aesthetic "birth sequence" of Sandman.</span>
            </div>
                            </div>
                                                        <div class="review_section review_actions ">
                                <ul class="review_actions">
                                                                            <li class="review_action review_helpful">
                                            <div class="review_helpful">
    <div class="rating_thumbs">
        			<div class="helpful_summary thumb_count">
				<a href="https://secure.metacritic.com/login">
				<span class="total_ups">0</span>
				of
				<span class="total_thumbs">0</span>
				users found this helpful
                </a>
			</div>
                <div style="clear:both;"></div>
    </div>
</div>
                                        </li>
                                                                                                                                            </ul>
                            </div>
                                                    </div>
                    </div></div></div></div>
                </li>
                                                                                    <li id="user_review_272060" class="review user_review">
                    <div class="review_btm review_btm_r"><div class="review_btm review_btm_l"><div class="review_top review_top_r"><div class="review_top review_top_l">
                        <div class="review_content">
                            <div class="review_section">
                                <div class="review_stats">
                                    <div class="review_critic">
                                        <div class="name">
                                                                                            <span>AMovieCriticYo</span>
                                                                                                                                </div>
                                                                                    <div class="date">May  5, 2007</div>
                                                                            </div>

                                    <div class="review_grade">

<div class="metascore_w user medium movie positive indiv perfect">10</div>

                                    </div>
                                </div>
                                <div class="review_body">

                                        <span class="inline_expand_collapse inline_collapsed" id="review_blurb_272060"><span class="blurb blurb_collapsed"> Riveting, touching, brilliant. This divisiveness is what spurs on greatness. Every great underrated action cannot go without being in question. The film delivered on its promise. It brings humanity into its superheroes, and delivers with its comedic and dramatic potential and fulfills it. It is like Arrested Development meets Superman 2. An overall superb film. Also, Harry Osborn finally</span><span class="blurb blurb_expanded"> Riveting, touching, brilliant. This divisiveness is what spurs on greatness. Every great underrated action cannot go without being in question. The film delivered on its promise. It brings humanity into its superheroes, and delivers with its comedic and dramatic potential and fulfills it. It is like Arrested Development meets Superman 2. An overall superb film. Also, Harry Osborn finally gets to show that he is a likeable character, and not whiny, and his part in the movie was incredible as a homicidal maniac-on and off again crazy best friend, who becomes an amnesiac, fights, and later, grows a conscience. The Green Goblin cooks, and paints. This is hillarious. Also, Venom was a dousche, but a convincing one at that. Lay off, haters.</span><span class="blurb_etc">…</span> <a rel="nofollow" class="toggle_expand_collapse toggle_expand" href="/movie/spider-man-3/user-reviews?page=1&amp;user_review_id=272060">Expand</a></span>
            </div>
                            </div>
                                                        <div class="review_section review_actions ">
                                <ul class="review_actions">
                                                                            <li class="review_action review_helpful">
                                            <div class="review_helpful">
    <div class="rating_thumbs">
        			<div class="helpful_summary thumb_count">
				<a href="https://secure.metacritic.com/login">
				<span class="total_ups">0</span>
				of
				<span class="total_thumbs">0</span>
				users found this helpful
                </a>
			</div>
                <div style="clear:both;"></div>
    </div>
</div>
                                        </li>
                                                                                                                                            </ul>
                            </div>
                                                    </div>
                    </div></div></div></div>
                </li>
                                                                                    <li id="user_review_272084" class="review user_review">
                    <div class="review_btm review_btm_r"><div class="review_btm review_btm_l"><div class="review_top review_top_r"><div class="review_top review_top_l">
                        <div class="review_content">
                            <div class="review_section">
                                <div class="review_stats">
                                    <div class="review_critic">
                                        <div class="name">
                                                                                            <span>777</span>
                                                                                                                                </div>
                                                                                    <div class="date">May  5, 2007</div>
                                                                            </div>

                                    <div class="review_grade">

<div class="metascore_w user medium movie mixed indiv">5</div>

                                    </div>
                                </div>
                                <div class="review_body">

                                        <span> The basic story line was good and the action was just outstanding but there was so many dumb sceens they should be ashamed.</span>
            </div>
                            </div>
                                                        <div class="review_section review_actions ">
                                <ul class="review_actions">
                                                                            <li class="review_action review_helpful">
                                            <div class="review_helpful">
    <div class="rating_thumbs">
        			<div class="helpful_summary thumb_count">
				<a href="https://secure.metacritic.com/login">
				<span class="total_ups">0</span>
				of
				<span class="total_thumbs">0</span>
				users found this helpful
                </a>
			</div>
                <div style="clear:both;"></div>
    </div>
</div>
                                        </li>
                                                                                                                                            </ul>
                            </div>
                                                    </div>
                    </div></div></div></div>
                </li>
                                                                                    <li id="user_review_272095" class="review user_review">
                    <div class="review_btm review_btm_r"><div class="review_btm review_btm_l"><div class="review_top review_top_r"><div class="review_top review_top_l">
                        <div class="review_content">
                            <div class="review_section">
                                <div class="review_stats">
                                    <div class="review_critic">
                                        <div class="name">
                                                                                            <span>TomW.</span>
                                                                                                                                </div>
                                                                                    <div class="date">May  5, 2007</div>
                                                                            </div>

                                    <div class="review_grade">

<div class="metascore_w user medium movie positive indiv perfect">10</div>

                                    </div>
                                </div>
                                <div class="review_body">

                                        <span class="inline_expand_collapse inline_collapsed" id="review_blurb_272095"><span class="blurb blurb_collapsed"> This movie may have had alot more cheesy lines than the first two, but it's still an epic Spidey adventure like them also. I can tell many of these people commenting obviously did not watch or understand the movie. It was hinted throughout the entire movie that Flint was a good person. He didn't suddenly become good in the end. Talor P. obviously has to go back and watch the</span><span class="blurb blurb_expanded"> This movie may have had alot more cheesy lines than the first two, but it's still an epic Spidey adventure like them also. I can tell many of these people commenting obviously did not watch or understand the movie. It was hinted throughout the entire movie that Flint was a good person. He didn't suddenly become good in the end. Talor P. obviously has to go back and watch the movie again.</span><span class="blurb_etc">…</span> <a rel="nofollow" class="toggle_expand_collapse toggle_expand" href="/movie/spider-man-3/user-reviews?page=1&amp;user_review_id=272095">Expand</a></span>
            </div>
                            </div>
                                                        <div class="review_section review_actions ">
                                <ul class="review_actions">
                                                                            <li class="review_action review_helpful">
                                            <div class="review_helpful">
    <div class="rating_thumbs">
        			<div class="helpful_summary thumb_count">
				<a href="https://secure.metacritic.com/login">
				<span class="total_ups">0</span>
				of
				<span class="total_thumbs">0</span>
				users found this helpful
                </a>
			</div>
                <div style="clear:both;"></div>
    </div>
</div>
                                        </li>
                                                                                                                                            </ul>
                            </div>
                                                    </div>
                    </div></div></div></div>
                </li>
                                                                                    <li id="user_review_272151" class="review user_review">
                    <div class="review_btm review_btm_r"><div class="review_btm review_btm_l"><div class="review_top review_top_r"><div class="review_top review_top_l">
                        <div class="review_content">
                            <div class="review_section">
                                <div class="review_stats">
                                    <div class="review_critic">
                                        <div class="name">
                                                                                            <span>MattW.</span>
                                                                                                                                </div>
                                                                                    <div class="date">May  6, 2007</div>
                                                                            </div>

                                    <div class="review_grade">

<div class="metascore_w user medium movie positive indiv">9</div>

                                    </div>
                                </div>
                                <div class="review_body">

                                        <span> I liked it. As a stand alone movie, its great. Its funny, action packed, and a lot better than most super hero movies.</span>
            </div>
                            </div>
                                                        <div class="review_section review_actions ">
                                <ul class="review_actions">
                                                                            <li class="review_action review_helpful">
                                            <div class="review_helpful">
    <div class="rating_thumbs">
        			<div class="helpful_summary thumb_count">
				<a href="https://secure.metacritic.com/login">
				<span class="total_ups">0</span>
				of
				<span class="total_thumbs">0</span>
				users found this helpful
                </a>
			</div>
                <div style="clear:both;"></div>
    </div>
</div>
                                        </li>
                                                                                                                                            </ul>
                            </div>
                                                    </div>
                    </div></div></div></div>
                </li>
                                                                                    <li id="user_review_272191" class="review user_review">
                    <div class="review_btm review_btm_r"><div class="review_btm review_btm_l"><div class="review_top review_top_r"><div class="review_top review_top_l">
                        <div class="review_content">
                            <div class="review_section">
                                <div class="review_stats">
                                    <div class="review_critic">
                                        <div class="name">
                                                                                            <span>JudyT</span>
                                                                                                                                </div>
                                                                                    <div class="date">May  6, 2007</div>
                                                                            </div>

                                    <div class="review_grade">

<div class="metascore_w user medium movie negative indiv">3</div>

                                    </div>
                                </div>
                                <div class="review_body">

                                        <span> Pitiful movie. Never did like Tobey as Spidey. In the comic he wasn't so nerdy, that Clark Kent not Peter Parker.</span>
            </div>
                            </div>
                                                        <div class="review_section review_actions ">
                                <ul class="review_actions">
                                                                            <li class="review_action review_helpful">
                                            <div class="review_helpful">
    <div class="rating_thumbs">
        			<div class="helpful_summary thumb_count">
				<a href="https://secure.metacritic.com/login">
				<span class="total_ups">0</span>
				of
				<span class="total_thumbs">0</span>
				users found this helpful
                </a>
			</div>
                <div style="clear:both;"></div>
    </div>
</div>
                                        </li>
                                                                                                                                            </ul>
                            </div>
                                                    </div>
                    </div></div></div></div>
                </li>
                                                                                    <li id="user_review_272157" class="review user_review">
                    <div class="review_btm review_btm_r"><div class="review_btm review_btm_l"><div class="review_top review_top_r"><div class="review_top review_top_l">
                        <div class="review_content">
                            <div class="review_section">
                                <div class="review_stats">
                                    <div class="review_critic">
                                        <div class="name">
                                                                                            <span>LeeH.</span>
                                                                                                                                </div>
                                                                                    <div class="date">May  6, 2007</div>
                                                                            </div>

                                    <div class="review_grade">

<div class="metascore_w user medium movie positive indiv">9</div>

                                    </div>
                                </div>
                                <div class="review_body">

                                        <span class="inline_expand_collapse inline_collapsed" id="review_blurb_272157"><span class="blurb blurb_collapsed"> A fantastic movie suffering from inevitable hype and high expectations. Yes it crams a lot in the time it has, but how many other movies could still do it as well as it does? Not perfect but lots of fun, bringing three villians (or are they?) into the mix as well as the romance and laughs. If this were the last in the series I would be far from disappointed - everything is concluded well</span><span class="blurb blurb_expanded"> A fantastic movie suffering from inevitable hype and high expectations. Yes it crams a lot in the time it has, but how many other movies could still do it as well as it does? Not perfect but lots of fun, bringing three villians (or are they?) into the mix as well as the romance and laughs. If this were the last in the series I would be far from disappointed - everything is concluded well given how much it has to do. Thank you Marvel, thank you Sony, thank you Sam!</span><span class="blurb_etc">…</span> <a rel="nofollow" class="toggle_expand_collapse toggle_expand" href="/movie/spider-man-3/user-reviews?page=1&amp;user_review_id=272157">Expand</a></span>
            </div>
                            </div>
                                                        <div class="review_section review_actions ">
                                <ul class="review_actions">
                                                                            <li class="review_action review_helpful">
                                            <div class="review_helpful">
    <div class="rating_thumbs">
        			<div class="helpful_summary thumb_count">
				<a href="https://secure.metacritic.com/login">
				<span class="total_ups">0</span>
				of
				<span class="total_thumbs">0</span>
				users found this helpful
                </a>
			</div>
                <div style="clear:both;"></div>
    </div>
</div>
                                        </li>
                                                                                                                                            </ul>
                            </div>
                                                    </div>
                    </div></div></div></div>
                </li>
                                                                                    <li id="user_review_272158" class="review user_review">
                    <div class="review_btm review_btm_r"><div class="review_btm review_btm_l"><div class="review_top review_top_r"><div class="review_top review_top_l">
                        <div class="review_content">
                            <div class="review_section">
                                <div class="review_stats">
                                    <div class="review_critic">
                                        <div class="name">
                                                                                            <span>NelsonS.</span>
                                                                                                                                </div>
                                                                                    <div class="date">May  6, 2007</div>
                                                                            </div>

                                    <div class="review_grade">

<div class="metascore_w user medium movie negative indiv">3</div>

                                    </div>
                                </div>
                                <div class="review_body">

                                        <span> Too many villains with no depth...too long which is one of the best marvel characters.</span>
            </div>
                            </div>
                                                        <div class="review_section review_actions ">
                                <ul class="review_actions">
                                                                            <li class="review_action review_helpful">
                                            <div class="review_helpful">
    <div class="rating_thumbs">
        			<div class="helpful_summary thumb_count">
				<a href="https://secure.metacritic.com/login">
				<span class="total_ups">0</span>
				of
				<span class="total_thumbs">0</span>
				users found this helpful
                </a>
			</div>
                <div style="clear:both;"></div>
    </div>
</div>
                                        </li>
                                                                                                                                            </ul>
                            </div>
                                                    </div>
                    </div></div></div></div>
                </li>
                                                                                    <li id="user_review_272159" class="review user_review">
                    <div class="review_btm review_btm_r"><div class="review_btm review_btm_l"><div class="review_top review_top_r"><div class="review_top review_top_l">
                        <div class="review_content">
                            <div class="review_section">
                                <div class="review_stats">
                                    <div class="review_critic">
                                        <div class="name">
                                                                                            <span>Easky</span>
                                                                                                                                </div>
                                                                                    <div class="date">May  6, 2007</div>
                                                                            </div>

                                    <div class="review_grade">

<div class="metascore_w user medium movie positive indiv">7</div>

                                    </div>
                                </div>
                                <div class="review_body">

                                        <span> This one may not be as good as last 2,however,it's a deeper one.</span>
            </div>
                            </div>
                                                        <div class="review_section review_actions ">
                                <ul class="review_actions">
                                                                            <li class="review_action review_helpful">
                                            <div class="review_helpful">
    <div class="rating_thumbs">
        			<div class="helpful_summary thumb_count">
				<a href="https://secure.metacritic.com/login">
				<span class="total_ups">0</span>
				of
				<span class="total_thumbs">0</span>
				users found this helpful
                </a>
			</div>
                <div style="clear:both;"></div>
    </div>
</div>
                                        </li>
                                                                                                                                            </ul>
                            </div>
                                                    </div>
                    </div></div></div></div>
                </li>
                                                                                    <li id="user_review_272161" class="review user_review">
                    <div class="review_btm review_btm_r"><div class="review_btm review_btm_l"><div class="review_top review_top_r"><div class="review_top review_top_l">
                        <div class="review_content">
                            <div class="review_section">
                                <div class="review_stats">
                                    <div class="review_critic">
                                        <div class="name">
                                                                                            <span>ChrisM.</span>
                                                                                                                                </div>
                                                                                    <div class="date">May  6, 2007</div>
                                                                            </div>

                                    <div class="review_grade">

<div class="metascore_w user medium movie negative indiv">2</div>

                                    </div>
                                </div>
                                <div class="review_body">

                                        <span class="inline_expand_collapse inline_collapsed" id="review_blurb_272161"><span class="blurb blurb_collapsed"> It's really pretty bad. I love Spiderman and I wanted it to be good, but it was really bad. The story lacks any kind of depth, there are many scenes that didn't need to be in the movie at all and were just plain stupid. (Like the dance scene in the Cafe). They need to go back to the drawing board with the fanchise, because it's become indulgent, bloated and really</span><span class="blurb blurb_expanded"> It's really pretty bad. I love Spiderman and I wanted it to be good, but it was really bad. The story lacks any kind of depth, there are many scenes that didn't need to be in the movie at all and were just plain stupid. (Like the dance scene in the Cafe). They need to go back to the drawing board with the fanchise, because it's become indulgent, bloated and really disappointing. Don't waste your money on this movie.</span><span class="blurb_etc">…</span> <a rel="nofollow" class="toggle_expand_collapse toggle_expand" href="/movie/spider-man-3/user-reviews?page=1&amp;user_review_id=272161">Expand</a></span>
            </div>
                            </div>
                                                        <div class="review_section review_actions ">
                                <ul class="review_actions">
                                                                            <li class="review_action review_helpful">
                                            <div class="review_helpful">
    <div class="rating_thumbs">
        			<div class="helpful_summary thumb_count">
				<a href="https://secure.metacritic.com/login">
				<span class="total_ups">0</span>
				of
				<span class="total_thumbs">0</span>
				users found this helpful
                </a>
			</div>
                <div style="clear:both;"></div>
    </div>
</div>
                                        </li>
                                                                                                                                            </ul>
                            </div>
                                                    </div>
                    </div></div></div></div>
                </li>
                                                                                    <li id="user_review_272162" class="review user_review">
                    <div class="review_btm review_btm_r"><div class="review_btm review_btm_l"><div class="review_top review_top_r"><div class="review_top review_top_l">
                        <div class="review_content">
                            <div class="review_section">
                                <div class="review_stats">
                                    <div class="review_critic">
                                        <div class="name">
                                                                                            <span>DavidP.</span>
                                                                                                                                </div>
                                                                                    <div class="date">May  6, 2007</div>
                                                                            </div>

                                    <div class="review_grade">

<div class="metascore_w user medium movie negative indiv">3</div>

                                    </div>
                                </div>
                                <div class="review_body">

                                        <span class="inline_expand_collapse inline_collapsed" id="review_blurb_272162"><span class="blurb blurb_collapsed"> I REALLY wanted to like this movie more. I have been a fan of the last 2 movies and have had some exposure of the Spiderman franchise (in the earlier years). But although there was a need to fulfill the fanboy wishes the movie falls flat on its face for pretty much all reasons. Visual effects although I'm sure they were pushing boundaries with the sandman 'particle' effects</span><span class="blurb blurb_expanded"> I REALLY wanted to like this movie more. I have been a fan of the last 2 movies and have had some exposure of the Spiderman franchise (in the earlier years). But although there was a need to fulfill the fanboy wishes the movie falls flat on its face for pretty much all reasons. Visual effects although I'm sure they were pushing boundaries with the sandman 'particle' effects there were some hideous compositing in that movie. Script suffered from really corny one liners. Look, I KNOW these actors can act but goddam the dialogue was so bad they really couldn't. And the story and themes and not to mention some really subpar editing and music. The pacing was too slow and then suddenly rushed in the last 15minutes to set up the final battle. And then, some more dialogue about forgiveness and everyone is ok.</span><span class="blurb_etc">…</span> <a rel="nofollow" class="toggle_expand_collapse toggle_expand" href="/movie/spider-man-3/user-reviews?page=1&amp;user_review_id=272162">Expand</a></span>
            </div>
                            </div>
                                                        <div class="review_section review_actions ">
                                <ul class="review_actions">
                                                                            <li class="review_action review_helpful">
                                            <div class="review_helpful">
    <div class="rating_thumbs">
        			<div class="helpful_summary thumb_count">
				<a href="https://secure.metacritic.com/login">
				<span class="total_ups">0</span>
				of
				<span class="total_thumbs">0</span>
				users found this helpful
                </a>
			</div>
                <div style="clear:both;"></div>
    </div>
</div>
                                        </li>
                                                                                                                                            </ul>
                            </div>
                                                    </div>
                    </div></div></div></div>
                </li>
                                                                                    <li id="user_review_272165" class="review user_review">
                    <div class="review_btm review_btm_r"><div class="review_btm review_btm_l"><div class="review_top review_top_r"><div class="review_top review_top_l">
                        <div class="review_content">
                            <div class="review_section">
                                <div class="review_stats">
                                    <div class="review_critic">
                                        <div class="name">
                                                                                            <span>SteveS.</span>
                                                                                                                                </div>
                                                                                    <div class="date">May  6, 2007</div>
                                                                            </div>

                                    <div class="review_grade">

<div class="metascore_w user medium movie negative indiv">2</div>

                                    </div>
                                </div>
                                <div class="review_body">

                                        <span> It fell into all the traps of previous comic book films, particularly the third and fourth "Batman" movies -- too many villains and not enough development of the characters. The "bad" Peter Parker sequence was dreadful and by the end, when Spider-Man was taking on a 40-foot Sandman, I felt like I was watching the Stay-Puft Marshmallow Man from "Ghostbusters." Don't bother.</span>
            </div>
                            </div>
                                                        <div class="review_section review_actions ">
                                <ul class="review_actions">
                                                                            <li class="review_action review_helpful">
                                            <div class="review_helpful">
    <div class="rating_thumbs">
        			<div class="helpful_summary thumb_count">
				<a href="https://secure.metacritic.com/login">
				<span class="total_ups">0</span>
				of
				<span class="total_thumbs">0</span>
				users found this helpful
                </a>
			</div>
                <div style="clear:both;"></div>
    </div>
</div>
                                        </li>
                                                                                                                                            </ul>
                            </div>
                                                    </div>
                    </div></div></div></div>
                </li>
                                                                                    <li id="user_review_272166" class="review user_review">
                    <div class="review_btm review_btm_r"><div class="review_btm review_btm_l"><div class="review_top review_top_r"><div class="review_top review_top_l">
                        <div class="review_content">
                            <div class="review_section">
                                <div class="review_stats">
                                    <div class="review_critic">
                                        <div class="name">
                                                                                            <span>BenB.</span>
                                                                                                                                </div>
                                                                                    <div class="date">May  6, 2007</div>
                                                                            </div>

                                    <div class="review_grade">

<div class="metascore_w user medium movie mixed indiv">5</div>

                                    </div>
                                </div>
                                <div class="review_body">

                                        <span> What a disappointment. This should have been the reinging moment for the franchise... instead all we get is an asinine plot, cardboard characters, and some of the worst dialogue I've heard in quite some time ("I'm the sherrif in these here parts!") Sam Raimi, what have you done?</span>
            </div>
                            </div>
                                                        <div class="review_section review_actions ">
                                <ul class="review_actions">
                                                                            <li class="review_action review_helpful">
                                            <div class="review_helpful">
    <div class="rating_thumbs">
        			<div class="helpful_summary thumb_count">
				<a href="https://secure.metacritic.com/login">
				<span class="total_ups">0</span>
				of
				<span class="total_thumbs">0</span>
				users found this helpful
                </a>
			</div>
                <div style="clear:both;"></div>
    </div>
</div>
                                        </li>
                                                                                                                                            </ul>
                            </div>
                                                    </div>
                    </div></div></div></div>
                </li>
                                                                                    <li id="user_review_272168" class="review user_review">
                    <div class="review_btm review_btm_r"><div class="review_btm review_btm_l"><div class="review_top review_top_r"><div class="review_top review_top_l">
                        <div class="review_content">
                            <div class="review_section">
                                <div class="review_stats">
                                    <div class="review_critic">
                                        <div class="name">
                                                                                            <span>Alex</span>
                                                                                                                                </div>
                                                                                    <div class="date">May  6, 2007</div>
                                                                            </div>

                                    <div class="review_grade">

<div class="metascore_w user medium movie positive indiv">7</div>

                                    </div>
                                </div>
                                <div class="review_body">

                                        <span class="inline_expand_collapse inline_collapsed" id="review_blurb_272168"><span class="blurb blurb_collapsed">As far as some franchise/superhero movies go, Spiderman 3 isn't bad. its entertaining enough to keep a Monster-addicted high-schooler (me) watching happily for the two hour running time. unfortunately, there are some departments where it just falls short. the movie has a tendancy to skip around a bit, making it midly difficult to follow, and some of the acting (especially on Toby</span><span class="blurb blurb_expanded">As far as some franchise/superhero movies go, Spiderman 3 isn't bad. its entertaining enough to keep a Monster-addicted high-schooler (me) watching happily for the two hour running time. unfortunately, there are some departments where it just falls short. the movie has a tendancy to skip around a bit, making it midly difficult to follow, and some of the acting (especially on Toby McGuire's part) just plain sucks. and then there was Venom. quite simply, he could not have been more poorly excecuted. he just came off as an evil, power hungry version of spiderman with bad teeth and black webs who wanted to exact revenge because he lost his job. Venom is one of my favorite bad guys, but after this movie, i'm not sure i can still say the same thing. but, i guess, in the end, it was still a fairly good movie. could have been better, but its still worth a good rental, or even a buy. overall, 7 out of 10.</span><span class="blurb_etc">…</span> <a rel="nofollow" class="toggle_expand_collapse toggle_expand" href="/movie/spider-man-3/user-reviews?page=1&amp;user_review_id=272168">Expand</a></span>
            </div>
                            </div>
                                                        <div class="review_section review_actions ">
                                <ul class="review_actions">
                                                                            <li class="review_action review_helpful">
                                            <div class="review_helpful">
    <div class="rating_thumbs">
        			<div class="helpful_summary thumb_count">
				<a href="https://secure.metacritic.com/login">
				<span class="total_ups">0</span>
				of
				<span class="total_thumbs">0</span>
				users found this helpful
                </a>
			</div>
                <div style="clear:both;"></div>
    </div>
</div>
                                        </li>
                                                                                                                                            </ul>
                            </div>
                                                    </div>
                    </div></div></div></div>
                </li>
                                                                                    <li id="user_review_272231" class="review user_review">
                    <div class="review_btm review_btm_r"><div class="review_btm review_btm_l"><div class="review_top review_top_r"><div class="review_top review_top_l">
                        <div class="review_content">
                            <div class="review_section">
                                <div class="review_stats">
                                    <div class="review_critic">
                                        <div class="name">
                                                                                            <span>Rick</span>
                                                                                                                                </div>
                                                                                    <div class="date">May  7, 2007</div>
                                                                            </div>

                                    <div class="review_grade">

<div class="metascore_w user medium movie positive indiv perfect">10</div>

                                    </div>
                                </div>
                                <div class="review_body">

                                        <span class="inline_expand_collapse inline_collapsed" id="review_blurb_272231"><span class="blurb blurb_collapsed"> Funny, amazing, incredible, goofy, all around great movie. The thing I like about the Spiderman movies is the villians. In all three movies the villian is not just evil to be evil but a person who has taken a few wrong turns. [***SPOILER***] Green Goblin had this moment of good at the end same for the Doc is Spiderman 2 and continued with Harry and Sandman in 3. Nothing is as simple as</span><span class="blurb blurb_expanded"> Funny, amazing, incredible, goofy, all around great movie. The thing I like about the Spiderman movies is the villians. In all three movies the villian is not just evil to be evil but a person who has taken a few wrong turns. [***SPOILER***] Green Goblin had this moment of good at the end same for the Doc is Spiderman 2 and continued with Harry and Sandman in 3. Nothing is as simple as good and evil especially when dealing with people.</span><span class="blurb_etc">…</span> <a rel="nofollow" class="toggle_expand_collapse toggle_expand" href="/movie/spider-man-3/user-reviews?page=1&amp;user_review_id=272231">Expand</a></span>
            </div>
                            </div>
                                                        <div class="review_section review_actions ">
                                <ul class="review_actions">
                                                                            <li class="review_action review_helpful">
                                            <div class="review_helpful">
    <div class="rating_thumbs">
        			<div class="helpful_summary thumb_count">
				<a href="https://secure.metacritic.com/login">
				<span class="total_ups">0</span>
				of
				<span class="total_thumbs">0</span>
				users found this helpful
                </a>
			</div>
                <div style="clear:both;"></div>
    </div>
</div>
                                        </li>
                                                                                                                                            </ul>
                            </div>
                                                    </div>
                    </div></div></div></div>
                </li>
                                                                                    <li id="user_review_272210" class="review user_review">
                    <div class="review_btm review_btm_r"><div class="review_btm review_btm_l"><div class="review_top review_top_r"><div class="review_top review_top_l">
                        <div class="review_content">
                            <div class="review_section">
                                <div class="review_stats">
                                    <div class="review_critic">
                                        <div class="name">
                                                                                            <span>KairiS.</span>
                                                                                                                                </div>
                                                                                    <div class="date">May  7, 2007</div>
                                                                            </div>

                                    <div class="review_grade">

<div class="metascore_w user medium movie positive indiv perfect">10</div>

                                    </div>
                                </div>
                                <div class="review_body">

                                        <span> Great flick. Good pacing. Just enough mix of humor, action, and fun. 2 thumbs up.</span>
            </div>
                            </div>
                                                        <div class="review_section review_actions ">
                                <ul class="review_actions">
                                                                            <li class="review_action review_helpful">
                                            <div class="review_helpful">
    <div class="rating_thumbs">
        			<div class="helpful_summary thumb_count">
				<a href="https://secure.metacritic.com/login">
				<span class="total_ups">0</span>
				of
				<span class="total_thumbs">0</span>
				users found this helpful
                </a>
			</div>
                <div style="clear:both;"></div>
    </div>
</div>
                                        </li>
                                                                                                                                            </ul>
                            </div>
                                                    </div>
                    </div></div></div></div>
                </li>
                                                                                    <li id="user_review_272211" class="review user_review">
                    <div class="review_btm review_btm_r"><div class="review_btm review_btm_l"><div class="review_top review_top_r"><div class="review_top review_top_l">
                        <div class="review_content">
                            <div class="review_section">
                                <div class="review_stats">
                                    <div class="review_critic">
                                        <div class="name">
                                                                                            <span>KenJ.</span>
                                                                                                                                </div>
                                                                                    <div class="date">May  7, 2007</div>
                                                                            </div>

                                    <div class="review_grade">

<div class="metascore_w user medium movie positive indiv">8</div>

                                    </div>
                                </div>
                                <div class="review_body">

                                        <span class="inline_expand_collapse inline_collapsed" id="review_blurb_272211"><span class="blurb blurb_collapsed"> Overall it was ok, the ending just didn't make any sense. [***SPOILERS***] The villians become these big soft wussies. They killed off the enemy way too quickly(Venom). Yes lots of cheesy moments but it is after all a movie that was based off of the comics which were just as cheesy and the first two films had corny scenes as well. It tends to get a bit confusing with all the</span><span class="blurb blurb_expanded"> Overall it was ok, the ending just didn't make any sense. [***SPOILERS***] The villians become these big soft wussies. They killed off the enemy way too quickly(Venom). Yes lots of cheesy moments but it is after all a movie that was based off of the comics which were just as cheesy and the first two films had corny scenes as well. It tends to get a bit confusing with all the characters being introduced at once, they probably should have just stuck with venom and the new goblin. The "depressed" peter parker was a joke, wasnt necessary. The fight scenes were pretty good, sandman appears about 10 mins in the movie just like venom...the fight at the end is about the best part of the movie, not the best movie but not the worst either, if you can live through the corny lines and all the lovey dovey bullsh.t.</span><span class="blurb_etc">…</span> <a rel="nofollow" class="toggle_expand_collapse toggle_expand" href="/movie/spider-man-3/user-reviews?page=1&amp;user_review_id=272211">Expand</a></span>
            </div>
                            </div>
                                                        <div class="review_section review_actions ">
                                <ul class="review_actions">
                                                                            <li class="review_action review_helpful">
                                            <div class="review_helpful">
    <div class="rating_thumbs">
        			<div class="helpful_summary thumb_count">
				<a href="https://secure.metacritic.com/login">
				<span class="total_ups">0</span>
				of
				<span class="total_thumbs">0</span>
				users found this helpful
                </a>
			</div>
                <div style="clear:both;"></div>
    </div>
</div>
                                        </li>
                                                                                                                                            </ul>
                            </div>
                                                    </div>
                    </div></div></div></div>
                </li>
                                                                                    <li id="user_review_272213" class="review user_review">
                    <div class="review_btm review_btm_r"><div class="review_btm review_btm_l"><div class="review_top review_top_r"><div class="review_top review_top_l">
                        <div class="review_content">
                            <div class="review_section">
                                <div class="review_stats">
                                    <div class="review_critic">
                                        <div class="name">
                                                                                            <span>NickP.</span>
                                                                                                                                </div>
                                                                                    <div class="date">May  7, 2007</div>
                                                                            </div>

                                    <div class="review_grade">

<div class="metascore_w user medium movie positive indiv">8</div>

                                    </div>
                                </div>
                                <div class="review_body">

                                        <span class="inline_expand_collapse inline_collapsed" id="review_blurb_272213"><span class="blurb blurb_collapsed"> Overall this movie was great, but it did have a couple flaws. [***SPOILER***] Harry dying at the end and little bit of time that you see Venom in there were some causes for concern. Also when things were going down nobody explained anything to anyone, like MJ breaking up with Peter and Peter not telling MJ about Harry, oh and don't forget the butler holding his breath until after</span><span class="blurb blurb_expanded"> Overall this movie was great, but it did have a couple flaws. [***SPOILER***] Harry dying at the end and little bit of time that you see Venom in there were some causes for concern. Also when things were going down nobody explained anything to anyone, like MJ breaking up with Peter and Peter not telling MJ about Harry, oh and don't forget the butler holding his breath until after Peter and Harry beat the hell out of each other. I'm a fan of the series, but the fourth one needs to explain everything so the fans can have some closure.</span><span class="blurb_etc">…</span> <a rel="nofollow" class="toggle_expand_collapse toggle_expand" href="/movie/spider-man-3/user-reviews?page=1&amp;user_review_id=272213">Expand</a></span>
            </div>
                            </div>
                                                        <div class="review_section review_actions ">
                                <ul class="review_actions">
                                                                            <li class="review_action review_helpful">
                                            <div class="review_helpful">
    <div class="rating_thumbs">
        			<div class="helpful_summary thumb_count">
				<a href="https://secure.metacritic.com/login">
				<span class="total_ups">0</span>
				of
				<span class="total_thumbs">0</span>
				users found this helpful
                </a>
			</div>
                <div style="clear:both;"></div>
    </div>
</div>
                                        </li>
                                                                                                                                            </ul>
                            </div>
                                                    </div>
                    </div></div></div></div>
                </li>
                                                                                    <li id="user_review_272216" class="review user_review">
                    <div class="review_btm review_btm_r"><div class="review_btm review_btm_l"><div class="review_top review_top_r"><div class="review_top review_top_l">
                        <div class="review_content">
                            <div class="review_section">
                                <div class="review_stats">
                                    <div class="review_critic">
                                        <div class="name">
                                                                                            <span>ReelWorld</span>
                                                                                                                                </div>
                                                                                    <div class="date">May  7, 2007</div>
                                                                            </div>

                                    <div class="review_grade">

<div class="metascore_w user medium movie mixed indiv">5</div>

                                    </div>
                                </div>
                                <div class="review_body">

                                        <span class="inline_expand_collapse inline_collapsed" id="review_blurb_272216"><span class="blurb blurb_collapsed"> Just caught the film last night and I have mixed emotions. Overall, it was an enjoyable romp for a summer movie, but not without its flaws. The action scenes were very good - albeit a LOT of CG that looked obviously so. The plot was all over the place, and character development was almost non-existent. In a lot of ways, the film reminded me of "X-Men 3" - very rushed, with a storyline</span><span class="blurb blurb_expanded"> Just caught the film last night and I have mixed emotions. Overall, it was an enjoyable romp for a summer movie, but not without its flaws. The action scenes were very good - albeit a LOT of CG that looked obviously so. The plot was all over the place, and character development was almost non-existent. In a lot of ways, the film reminded me of "X-Men 3" - very rushed, with a storyline that jumped between the multiple plot points way too much. The CG effects of Sandman were hit and miss IMO. In some cases - it looked really good - and others not so much. Venom was majorly underused and when he was he looked a lot like that dog Milo from "The Mask" when he sticks the mask on - overexaggerated fangs, and lacking the protruding jaw from the comics - just something didn't look right with him. Add to that the fact that even when in full on fangs and white eyes mode - Venom still speaks with Topher's voice - no effect has been added to it at all - which quite honestly looked really off! In some cases it looked like pre-viz work almost. I knew it would be hard to pull of Venom - but with today's state of the art - I was expecting something different. Acting-wise - well - this is a comic book film, so I'm not looking for next year's potential Best Actor or Actress nominees here...When Peter goes evil mode with the black suit, the scenes are almost too much. I'm not sure what effect Raimi was looking to convey here, but I found much of the time he was just acting plain stupid. Spidey's fights while clad in black are much more brutal - with him not afraid to go beyond what is necessary in the battle - even to the extent of playing dirty. I've long stood by the theory that Dunst can't act and she once again proves it with a 2-dimensional run at MJ. Church, as Sandman, was a throwaway character. They gave him nothing to do except be a stand in for the CG department. Topher as Brock/Venom really didn't have ample time to create anything of a character - another drawback from the loopy storyline. James Franco sways between acting like Willem Dafoe - right down to the squinting left eye thing - to Degrassi mode when he has amnesia. Like I said - I'm not expecting awards here unless they're Razzies. The big huge battle royale has its moments of pure wow factor, offset by Venom's comical appearance. For most of the fight, Topher has the face pulled away, but you do get 4 or 5 really good looks at him in full on symbiote mode. Without ruining anything, the ending was a bit of a let-down. The Stan Lee cameo was a nice touch, and Campbell as the French waiter was funny, but the spidey sense line was right up there with the "Holy rusted metal" schtick. Again, stuff like that really detracted from the film IMO. All in all, I suppose it's a film worth seeing - but if you go in there thinking this is the superhero film to top the likes of "Batman Begins" or the second Spider-Man, you might be disappointed. Worth the price of admission at a matinée, and I look forward to the DVD in November in hopes of some deleted material to fill in some of the gaps and make some sense of the multitude of story arcs.</span><span class="blurb_etc">…</span> <a rel="nofollow" class="toggle_expand_collapse toggle_expand" href="/movie/spider-man-3/user-reviews?page=1&amp;user_review_id=272216">Expand</a></span>
            </div>
                            </div>
                                                        <div class="review_section review_actions ">
                                <ul class="review_actions">
                                                                            <li class="review_action review_helpful">
                                            <div class="review_helpful">
    <div class="rating_thumbs">
        			<div class="helpful_summary thumb_count">
				<a href="https://secure.metacritic.com/login">
				<span class="total_ups">0</span>
				of
				<span class="total_thumbs">0</span>
				users found this helpful
                </a>
			</div>
                <div style="clear:both;"></div>
    </div>
</div>
                                        </li>
                                                                                                                                            </ul>
                            </div>
                                                    </div>
                    </div></div></div></div>
                </li>
                                                                                    <li id="user_review_272215" class="review user_review">
                    <div class="review_btm review_btm_r"><div class="review_btm review_btm_l"><div class="review_top review_top_r"><div class="review_top review_top_l">
                        <div class="review_content">
                            <div class="review_section">
                                <div class="review_stats">
                                    <div class="review_critic">
                                        <div class="name">
                                                                                            <span>PatrickC</span>
                                                                                                                                </div>
                                                                                    <div class="date">May  7, 2007</div>
                                                                            </div>

                                    <div class="review_grade">

<div class="metascore_w user medium movie mixed indiv">6</div>

                                    </div>
                                </div>
                                <div class="review_body">

                                        <span> This movie looks, visually, great. Too bad the script and lack of good acting make this movie unenjoyable. The film is too long with too little action fights which are the best scenes in the film. The film is a bad addition to a good superhero series.</span>
            </div>
                            </div>
                                                        <div class="review_section review_actions ">
                                <ul class="review_actions">
                                                                            <li class="review_action review_helpful">
                                            <div class="review_helpful">
    <div class="rating_thumbs">
        			<div class="helpful_summary thumb_count">
				<a href="https://secure.metacritic.com/login">
				<span class="total_ups">0</span>
				of
				<span class="total_thumbs">0</span>
				users found this helpful
                </a>
			</div>
                <div style="clear:both;"></div>
    </div>
</div>
                                        </li>
                                                                                                                                            </ul>
                            </div>
                                                    </div>
                    </div></div></div></div>
                </li>
                                                                                    <li id="user_review_272214" class="review user_review">
                    <div class="review_btm review_btm_r"><div class="review_btm review_btm_l"><div class="review_top review_top_r"><div class="review_top review_top_l">
                        <div class="review_content">
                            <div class="review_section">
                                <div class="review_stats">
                                    <div class="review_critic">
                                        <div class="name">
                                                                                            <span>Giga</span>
                                                                                                                                </div>
                                                                                    <div class="date">May  7, 2007</div>
                                                                            </div>

                                    <div class="review_grade">

<div class="metascore_w user medium movie positive indiv">8</div>

                                    </div>
                                </div>
                                <div class="review_body">

                                        <span> A very entertaining comic-movie with marvelous special effects, naive plot and funny little jokes. What else do you need to relax a bit?</span>
            </div>
                            </div>
                                                        <div class="review_section review_actions ">
                                <ul class="review_actions">
                                                                            <li class="review_action review_helpful">
                                            <div class="review_helpful">
    <div class="rating_thumbs">
        			<div class="helpful_summary thumb_count">
				<a href="https://secure.metacritic.com/login">
				<span class="total_ups">0</span>
				of
				<span class="total_thumbs">0</span>
				users found this helpful
                </a>
			</div>
                <div style="clear:both;"></div>
    </div>
</div>
                                        </li>
                                                                                                                                            </ul>
                            </div>
                                                    </div>
                    </div></div></div></div>
                </li>
                                                                                    <li id="user_review_272221" class="review user_review">
                    <div class="review_btm review_btm_r"><div class="review_btm review_btm_l"><div class="review_top review_top_r"><div class="review_top review_top_l">
                        <div class="review_content">
                            <div class="review_section">
                                <div class="review_stats">
                                    <div class="review_critic">
                                        <div class="name">
                                                                                            <span>NickB.</span>
                                                                                                                                </div>
                                                                                    <div class="date">May  7, 2007</div>
                                                                            </div>

                                    <div class="review_grade">

<div class="metascore_w user medium movie mixed indiv">6</div>

                                    </div>
                                </div>
                                <div class="review_body">

                                        <span class="inline_expand_collapse inline_collapsed" id="review_blurb_272221"><span class="blurb blurb_collapsed"> This movie was ok but so many of the key points of spider man were lost somewhere between the 2nd and the 3rd movie for example no spidey senses at all in the 3rd movie he literally gets hit in the back like 14 times without seeing it coming. And it doesn't have a lot of the points from the comic books where the sand man never was this good guy who apologized at the end he was always</span><span class="blurb blurb_expanded"> This movie was ok but so many of the key points of spider man were lost somewhere between the 2nd and the 3rd movie for example no spidey senses at all in the 3rd movie he literally gets hit in the back like 14 times without seeing it coming. And it doesn't have a lot of the points from the comic books where the sand man never was this good guy who apologized at the end he was always mean so it was ok but not very good.</span><span class="blurb_etc">…</span> <a rel="nofollow" class="toggle_expand_collapse toggle_expand" href="/movie/spider-man-3/user-reviews?page=1&amp;user_review_id=272221">Expand</a></span>
            </div>
                            </div>
                                                        <div class="review_section review_actions ">
                                <ul class="review_actions">
                                                                            <li class="review_action review_helpful">
                                            <div class="review_helpful">
    <div class="rating_thumbs">
        			<div class="helpful_summary thumb_count">
				<a href="https://secure.metacritic.com/login">
				<span class="total_ups">0</span>
				of
				<span class="total_thumbs">0</span>
				users found this helpful
                </a>
			</div>
                <div style="clear:both;"></div>
    </div>
</div>
                                        </li>
                                                                                                                                            </ul>
                            </div>
                                                    </div>
                    </div></div></div></div>
                </li>
                                                                                    <li id="user_review_272223" class="review user_review">
                    <div class="review_btm review_btm_r"><div class="review_btm review_btm_l"><div class="review_top review_top_r"><div class="review_top review_top_l">
                        <div class="review_content">
                            <div class="review_section">
                                <div class="review_stats">
                                    <div class="review_critic">
                                        <div class="name">
                                                                                            <span>RichardR.</span>
                                                                                                                                </div>
                                                                                    <div class="date">May  7, 2007</div>
                                                                            </div>

                                    <div class="review_grade">

<div class="metascore_w user medium movie mixed indiv">5</div>

                                    </div>
                                </div>
                                <div class="review_body">

                                        <span class="inline_expand_collapse inline_collapsed" id="review_blurb_272223"><span class="blurb blurb_collapsed"> Oh boy, I was so exicted about watching this film. I abandoned the girlfriend, sat down with my oversized portions of snacks and beverages and prepared myself for the webslinging event of the year. This time spiderman had a whole array of problems and bad guys to deal with. There was of course the continuing saga of the murder of his unlce, his friendship with harry and also lets not</span><span class="blurb blurb_expanded"> Oh boy, I was so exicted about watching this film. I abandoned the girlfriend, sat down with my oversized portions of snacks and beverages and prepared myself for the webslinging event of the year. This time spiderman had a whole array of problems and bad guys to deal with. There was of course the continuing saga of the murder of his unlce, his friendship with harry and also lets not forget his efforts to make MJ the only woman in his life. And then there are the bad guys, Sandman, the hobgoblin and Venom. Does it sound like there is too much going going on? Well you would be right. This film did not have the boldness to follow one theme and one bad guy. I would have been happy to have spiderman slug it out with venom, who was extremly under used, and leave it at that. Forgiveness, commitment, vanity and pride were all addressed in this final part of the trilogy and it was hard to figure out what the film was trying to say. The effects of course were amazing and you know where all of the money went into making the film. Its a shame after such a brilliant second part of the trilogy, Spiderman 3 left me wanting more and extremly unsatisfied, maybe I need to see it again....</span><span class="blurb_etc">…</span> <a rel="nofollow" class="toggle_expand_collapse toggle_expand" href="/movie/spider-man-3/user-reviews?page=1&amp;user_review_id=272223">Expand</a></span>
            </div>
                            </div>
                                                        <div class="review_section review_actions ">
                                <ul class="review_actions">
                                                                            <li class="review_action review_helpful">
                                            <div class="review_helpful">
    <div class="rating_thumbs">
        			<div class="helpful_summary thumb_count">
				<a href="https://secure.metacritic.com/login">
				<span class="total_ups">0</span>
				of
				<span class="total_thumbs">0</span>
				users found this helpful
                </a>
			</div>
                <div style="clear:both;"></div>
    </div>
</div>
                                        </li>
                                                                                                                                            </ul>
                            </div>
                                                    </div>
                    </div></div></div></div>
                </li>
                                                                                    <li id="user_review_272228" class="review user_review">
                    <div class="review_btm review_btm_r"><div class="review_btm review_btm_l"><div class="review_top review_top_r"><div class="review_top review_top_l">
                        <div class="review_content">
                            <div class="review_section">
                                <div class="review_stats">
                                    <div class="review_critic">
                                        <div class="name">
                                                                                            <span>NadieT.</span>
                                                                                                                                </div>
                                                                                    <div class="date">May  7, 2007</div>
                                                                            </div>

                                    <div class="review_grade">

<div class="metascore_w user medium movie negative indiv">2</div>

                                    </div>
                                </div>
                                <div class="review_body">

                                        <span> Loooooooong and boring. Tobey can't play a bad guy, looks like a parody of himself. Great effects but what's new. Please stop here and don't make us suffer thru a 4th one.</span>
            </div>
                            </div>
                                                        <div class="review_section review_actions ">
                                <ul class="review_actions">
                                                                            <li class="review_action review_helpful">
                                            <div class="review_helpful">
    <div class="rating_thumbs">
        			<div class="helpful_summary thumb_count">
				<a href="https://secure.metacritic.com/login">
				<span class="total_ups">0</span>
				of
				<span class="total_thumbs">0</span>
				users found this helpful
                </a>
			</div>
                <div style="clear:both;"></div>
    </div>
</div>
                                        </li>
                                                                                                                                            </ul>
                            </div>
                                                    </div>
                    </div></div></div></div>
                </li>
                                                                                    <li id="user_review_272256" class="review user_review">
                    <div class="review_btm review_btm_r"><div class="review_btm review_btm_l"><div class="review_top review_top_r"><div class="review_top review_top_l">
                        <div class="review_content">
                            <div class="review_section">
                                <div class="review_stats">
                                    <div class="review_critic">
                                        <div class="name">
                                                                                            <span>ChadS.</span>
                                                                                                                                </div>
                                                                                    <div class="date">May  8, 2007</div>
                                                                            </div>

                                    <div class="review_grade">

<div class="metascore_w user medium movie mixed indiv">6</div>

                                    </div>
                                </div>
                                <div class="review_body">

                                        <span class="inline_expand_collapse inline_collapsed" id="review_blurb_272256"><span class="blurb blurb_collapsed"> A plot convolution that preceeds the final action set-piece prevents "Spider-Man 3" from soaring to even the modest level of the original(never-mind the near-brilliant second installment) "Spider-Man". The piece of pertinent information that Harry(James Franco) at long last learns is baffling in its tardiness, because you can't figure out the logic behind the teller's</span><span class="blurb blurb_expanded"> A plot convolution that preceeds the final action set-piece prevents "Spider-Man 3" from soaring to even the modest level of the original(never-mind the near-brilliant second installment) "Spider-Man". The piece of pertinent information that Harry(James Franco) at long last learns is baffling in its tardiness, because you can't figure out the logic behind the teller's machinations in needlessly drawing out the long-standing vendetta his employer has against Peter Parker(Tobey Maguire). To spill the beans so late in the trilogy seems like an arbitrary decision on the screenwriter's part to move the story along. It doesn't feel organic. "Spider-Man 3" peaks during Maguire's dance number which smartly deconstructs the movie musical by lifting the veil of narcissism that's inherent in all musical numbers. Parker must have some deep-seated jealousy towards Mary Jane(Kirsten Dunst) and her burgeoning musical career. Since this is apparently the case(Parker never attends another performance), there should be some alteration in Maguire's glowing demeanor throughout Mary Jane's performance of the Broadway show's opening number as an indicator to his threatened ego.</span><span class="blurb_etc">…</span> <a rel="nofollow" class="toggle_expand_collapse toggle_expand" href="/movie/spider-man-3/user-reviews?page=1&amp;user_review_id=272256">Expand</a></span>
            </div>
                            </div>
                                                        <div class="review_section review_actions ">
                                <ul class="review_actions">
                                                                            <li class="review_action review_helpful">
                                            <div class="review_helpful">
    <div class="rating_thumbs">
        			<div class="helpful_summary thumb_count">
				<a href="https://secure.metacritic.com/login">
				<span class="total_ups">0</span>
				of
				<span class="total_thumbs">0</span>
				users found this helpful
                </a>
			</div>
                <div style="clear:both;"></div>
    </div>
</div>
                                        </li>
                                                                                                                                            </ul>
                            </div>
                                                    </div>
                    </div></div></div></div>
                </li>
                                                                                    <li id="user_review_272259" class="review user_review">
                    <div class="review_btm review_btm_r"><div class="review_btm review_btm_l"><div class="review_top review_top_r"><div class="review_top review_top_l">
                        <div class="review_content">
                            <div class="review_section">
                                <div class="review_stats">
                                    <div class="review_critic">
                                        <div class="name">
                                                                                            <span>MarkS</span>
                                                                                                                                </div>
                                                                                    <div class="date">May  8, 2007</div>
                                                                            </div>

                                    <div class="review_grade">

<div class="metascore_w user medium movie positive indiv">8</div>

                                    </div>
                                </div>
                                <div class="review_body">

                                        <span class="inline_expand_collapse inline_collapsed" id="review_blurb_272259"><span class="blurb blurb_collapsed"> In opposition to most of the other reviewers I felt that 2 was a let-down from the excellence of the first film. In my mind this was much better than the weak, repetitive second installment. While it still has problems (it sometimes feels like they had two ideas for the film, but neither would be long enough so they were grafted together, a number of George Lucas caliber bad "romantic"</span><span class="blurb blurb_expanded"> In opposition to most of the other reviewers I felt that 2 was a let-down from the excellence of the first film. In my mind this was much better than the weak, repetitive second installment. While it still has problems (it sometimes feels like they had two ideas for the film, but neither would be long enough so they were grafted together, a number of George Lucas caliber bad "romantic" moments, and some scenes that feel forced) it was a worthy sequel. So, considering that I liked the first one, felt the second was weak, and am a long-time comic fan (though, not generally a big reader of super-hero fare) this came out as the second-best in the series and a great way to spend a few hours.</span><span class="blurb_etc">…</span> <a rel="nofollow" class="toggle_expand_collapse toggle_expand" href="/movie/spider-man-3/user-reviews?page=1&amp;user_review_id=272259">Expand</a></span>
            </div>
                            </div>
                                                        <div class="review_section review_actions ">
                                <ul class="review_actions">
                                                                            <li class="review_action review_helpful">
                                            <div class="review_helpful">
    <div class="rating_thumbs">
        			<div class="helpful_summary thumb_count">
				<a href="https://secure.metacritic.com/login">
				<span class="total_ups">0</span>
				of
				<span class="total_thumbs">0</span>
				users found this helpful
                </a>
			</div>
                <div style="clear:both;"></div>
    </div>
</div>
                                        </li>
                                                                                                                                            </ul>
                            </div>
                                                    </div>
                    </div></div></div></div>
                </li>
                                                                                    <li id="user_review_272268" class="review user_review">
                    <div class="review_btm review_btm_r"><div class="review_btm review_btm_l"><div class="review_top review_top_r"><div class="review_top review_top_l">
                        <div class="review_content">
                            <div class="review_section">
                                <div class="review_stats">
                                    <div class="review_critic">
                                        <div class="name">
                                                                                            <span>TravisC.</span>
                                                                                                                                </div>
                                                                                    <div class="date">May  8, 2007</div>
                                                                            </div>

                                    <div class="review_grade">

<div class="metascore_w user medium movie positive indiv">8</div>

                                    </div>
                                </div>
                                <div class="review_body">

                                        <span> People sure seem to be expecting quite a bit from a movie basically made for children. It's a fun way to spend two and a half hours and just as good as the first two.</span>
            </div>
                            </div>
                                                        <div class="review_section review_actions ">
                                <ul class="review_actions">
                                                                            <li class="review_action review_helpful">
                                            <div class="review_helpful">
    <div class="rating_thumbs">
        			<div class="helpful_summary thumb_count">
				<a href="https://secure.metacritic.com/login">
				<span class="total_ups">0</span>
				of
				<span class="total_thumbs">0</span>
				users found this helpful
                </a>
			</div>
                <div style="clear:both;"></div>
    </div>
</div>
                                        </li>
                                                                                                                                            </ul>
                            </div>
                                                    </div>
                    </div></div></div></div>
                </li>
                                                                                    <li id="user_review_272321" class="review user_review">
                    <div class="review_btm review_btm_r"><div class="review_btm review_btm_l"><div class="review_top review_top_r"><div class="review_top review_top_l">
                        <div class="review_content">
                            <div class="review_section">
                                <div class="review_stats">
                                    <div class="review_critic">
                                        <div class="name">
                                                                                            <span>AlexB.</span>
                                                                                                                                </div>
                                                                                    <div class="date">May  9, 2007</div>
                                                                            </div>

                                    <div class="review_grade">

<div class="metascore_w user medium movie mixed indiv">4</div>

                                    </div>
                                </div>
                                <div class="review_body">

                                        <span class="inline_expand_collapse inline_collapsed" id="review_blurb_272321"><span class="blurb blurb_collapsed"> First let me start by saying that "Spider-Man 3" was three-and-a-half of the most mediocre films I have ever seen crammed into two-and-a-half hours of sub par editing. Second, I'd like to mention that there is something to be said about the fact that the majority of those that seem to be giving this film any positive reviews are those that read negative reviews, first, before</span><span class="blurb blurb_expanded"> First let me start by saying that "Spider-Man 3" was three-and-a-half of the most mediocre films I have ever seen crammed into two-and-a-half hours of sub par editing. Second, I'd like to mention that there is something to be said about the fact that the majority of those that seem to be giving this film any positive reviews are those that read negative reviews, first, before actually seeing the movie. Coincidence! Me thinks not! Benificiaries of lowered expectations! Me thinks so! That said, those of us Spider-Man fanatics (made so by the comic books, and even more so by the solid "Spider-Man" and the superb "Spider-Man 2" films) that caught "S3" on an early screening, expecting to see an exponetial improvement in the third installment, were (*understatement alert*) let down like some many eleviated subway trains without a real hero to stop us from falling! I, however, have something much more thought provoking than throwing my full-headed mask in the ring of what has become a litany of critizism! I have a conspiracy theory! Could it be that an obviously exhausted Sam Raimi, as well as his cast, took a dive! Why, you say? Reason 1: He's tired! Its easier to make a crappy movie than a good one! (Duh!) Reason 2: After the truly "amazing" first sequel, and millions in promo, they knew you couldn't stay away. Plus, contracts are up! So, why not!?!? Reason 3: With a character as complex and likeable as this one, and with the huge fan following Spider-Man has, as well as the many well know, multi-dimensional, interesting roster of rogues that litter the Spider-Man mythology, it had been my assumption from the start that Spider-Man would become the next James Bond, with a seemingly limitless number of sequels. Sequels that, even if they lost some intrigue over the years, would still make only more money than 95% of the competition! Maybe Raimi purposely blew his load with three villians, over-the-top (attempts at) comedy, under-the-bottom dramatic perfomances, and the resolution (Parker forgiving the perp) of the driving force of Spidey's purpose for crime fighting! Maybe Sam and Co. are saying, "Whoever takes over," and someone will (Don't ever underestimate corporate greed. There will be more Spider-Man movies)", is going to have to start from scratch!" So, purely out of ego, they decide to crap in a box, wrap it up in a nice little (well promoted) package, and smear it up on the screen for our spewing (not a typo) pleasure. Bad form Sam! Bad form indeed, good sir! But I'm just saying. . . P.S. Venom was in this movie? Oh, that's right! Nature called! It must have been during those 5 minutes! I knew I shouldn't have washed my hands! I was so looking foward to seeing Venom! (Cricket! Cricket! Cricket!)</span><span class="blurb_etc">…</span> <a rel="nofollow" class="toggle_expand_collapse toggle_expand" href="/movie/spider-man-3/user-reviews?page=1&amp;user_review_id=272321">Expand</a></span>
            </div>
                            </div>
                                                        <div class="review_section review_actions ">
                                <ul class="review_actions">
                                                                            <li class="review_action review_helpful">
                                            <div class="review_helpful">
    <div class="rating_thumbs">
        			<div class="helpful_summary thumb_count">
				<a href="https://secure.metacritic.com/login">
				<span class="total_ups">0</span>
				of
				<span class="total_thumbs">0</span>
				users found this helpful
                </a>
			</div>
                <div style="clear:both;"></div>
    </div>
</div>
                                        </li>
                                                                                                                                            </ul>
                            </div>
                                                    </div>
                    </div></div></div></div>
                </li>
                                                                                    <li id="user_review_272293" class="review user_review">
                    <div class="review_btm review_btm_r"><div class="review_btm review_btm_l"><div class="review_top review_top_r"><div class="review_top review_top_l">
                        <div class="review_content">
                            <div class="review_section">
                                <div class="review_stats">
                                    <div class="review_critic">
                                        <div class="name">
                                                                                            <span>BenM.</span>
                                                                                                                                </div>
                                                                                    <div class="date">May  9, 2007</div>
                                                                            </div>

                                    <div class="review_grade">

<div class="metascore_w user medium movie mixed indiv">6</div>

                                    </div>
                                </div>
                                <div class="review_body">

                                        <span class="inline_expand_collapse inline_collapsed" id="review_blurb_272293"><span class="blurb blurb_collapsed"> I dunno about this one. It's something that felt like overreaching. Like the original "Batman" or "War of the Worlds", some viewers will be fooled into thinking it's a great movie, but it's not. It's a mediocre movie made up of great things, good things and really, really bad things. I HATED Tobey Maguire's performance in this movie. And he made "Spider-Man 2" the</span><span class="blurb blurb_expanded"> I dunno about this one. It's something that felt like overreaching. Like the original "Batman" or "War of the Worlds", some viewers will be fooled into thinking it's a great movie, but it's not. It's a mediocre movie made up of great things, good things and really, really bad things. I HATED Tobey Maguire's performance in this movie. And he made "Spider-Man 2" the great movie it was. My view of the "Spider-Man" series is like a juicy, succulent piece of meat sandwiched between two stale pieces of bread. You tolerate it, but you wish the bread was fresher. Spidey 1: 7/10 Spidey 2: 10/10 Spidey 3: 6/10</span><span class="blurb_etc">…</span> <a rel="nofollow" class="toggle_expand_collapse toggle_expand" href="/movie/spider-man-3/user-reviews?page=1&amp;user_review_id=272293">Expand</a></span>
            </div>
                            </div>
                                                        <div class="review_section review_actions ">
                                <ul class="review_actions">
                                                                            <li class="review_action review_helpful">
                                            <div class="review_helpful">
    <div class="rating_thumbs">
        			<div class="helpful_summary thumb_count">
				<a href="https://secure.metacritic.com/login">
				<span class="total_ups">0</span>
				of
				<span class="total_thumbs">0</span>
				users found this helpful
                </a>
			</div>
                <div style="clear:both;"></div>
    </div>
</div>
                                        </li>
                                                                                                                                            </ul>
                            </div>
                                                    </div>
                    </div></div></div></div>
                </li>
                                                                                    <li id="user_review_273253" class="review user_review">
                    <div class="review_btm review_btm_r"><div class="review_btm review_btm_l"><div class="review_top review_top_r"><div class="review_top review_top_l">
                        <div class="review_content">
                            <div class="review_section">
                                <div class="review_stats">
                                    <div class="review_critic">
                                        <div class="name">
                                                                                            <span>AB</span>
                                                                                                                                </div>
                                                                                    <div class="date">Jun  2, 2007</div>
                                                                            </div>

                                    <div class="review_grade">

<div class="metascore_w user medium movie negative indiv">3</div>

                                    </div>
                                </div>
                                <div class="review_body">

                                        <span> As a strong fan of the first two Spider-Man movies, I find myself inexplicably disappointed in the third installment. The action scenes are mildly entertaining portions of an incredibly disastrous whole. The dialog is horrific, and, at best, the plot is senseless, containing numerous fallacies. Along with Shrek the Third, Spider-Man 3 is a major letdown.</span>
            </div>
                            </div>
                                                        <div class="review_section review_actions ">
                                <ul class="review_actions">
                                                                            <li class="review_action review_helpful">
                                            <div class="review_helpful">
    <div class="rating_thumbs">
        			<div class="helpful_summary thumb_count">
				<a href="https://secure.metacritic.com/login">
				<span class="total_ups">0</span>
				of
				<span class="total_thumbs">0</span>
				users found this helpful
                </a>
			</div>
                <div style="clear:both;"></div>
    </div>
</div>
                                        </li>
                                                                                                                                            </ul>
                            </div>
                                                    </div>
                    </div></div></div></div>
                </li>
                                                                                    <li id="user_review_273913" class="review user_review">
                    <div class="review_btm review_btm_r"><div class="review_btm review_btm_l"><div class="review_top review_top_r"><div class="review_top review_top_l">
                        <div class="review_content">
                            <div class="review_section">
                                <div class="review_stats">
                                    <div class="review_critic">
                                        <div class="name">
                                                                                            <span>WilliamB.</span>
                                                                                                                                </div>
                                                                                    <div class="date">Jun 21, 2007</div>
                                                                            </div>

                                    <div class="review_grade">

<div class="metascore_w user medium movie positive indiv">8</div>

                                    </div>
                                </div>
                                <div class="review_body">

                                        <span> Good action combined with several laughs made it a fun time all around.</span>
            </div>
                            </div>
                                                        <div class="review_section review_actions ">
                                <ul class="review_actions">
                                                                            <li class="review_action review_helpful">
                                            <div class="review_helpful">
    <div class="rating_thumbs">
        			<div class="helpful_summary thumb_count">
				<a href="https://secure.metacritic.com/login">
				<span class="total_ups">0</span>
				of
				<span class="total_thumbs">0</span>
				users found this helpful
                </a>
			</div>
                <div style="clear:both;"></div>
    </div>
</div>
                                        </li>
                                                                                                                                            </ul>
                            </div>
                                                    </div>
                    </div></div></div></div>
                </li>
                                                                                    <li id="user_review_273476" class="review user_review">
                    <div class="review_btm review_btm_r"><div class="review_btm review_btm_l"><div class="review_top review_top_r"><div class="review_top review_top_l">
                        <div class="review_content">
                            <div class="review_section">
                                <div class="review_stats">
                                    <div class="review_critic">
                                        <div class="name">
                                                                                            <span>JohnK.</span>
                                                                                                                                </div>
                                                                                    <div class="date">Jun  7, 2007</div>
                                                                            </div>

                                    <div class="review_grade">

<div class="metascore_w user medium movie mixed indiv">5</div>

                                    </div>
                                </div>
                                <div class="review_body">

                                        <span class="inline_expand_collapse inline_collapsed" id="review_blurb_273476"><span class="blurb blurb_collapsed"> Not an awful movie, but not nearly as good as the first 2 movies. Much sappier, and the ending is way too drawn out and overly emotional. Plus, does every superhero/villain have to take off their mask every time they speak??? I mean, its called a SECRET identity for a reason, but none of these characters seem to know that. Even the action scenes aren't as good as the first 2. Bottom</span><span class="blurb blurb_expanded"> Not an awful movie, but not nearly as good as the first 2 movies. Much sappier, and the ending is way too drawn out and overly emotional. Plus, does every superhero/villain have to take off their mask every time they speak??? I mean, its called a SECRET identity for a reason, but none of these characters seem to know that. Even the action scenes aren't as good as the first 2. Bottom line, I think they tried to do too much. There are so many different stories going on that it just doesn't flow well. If you're one of the 2 or 3 people that haven't seen this yet, I would wait for the DVD.</span><span class="blurb_etc">…</span> <a rel="nofollow" class="toggle_expand_collapse toggle_expand" href="/movie/spider-man-3/user-reviews?page=1&amp;user_review_id=273476">Expand</a></span>
            </div>
                            </div>
                                                        <div class="review_section review_actions ">
                                <ul class="review_actions">
                                                                            <li class="review_action review_helpful">
                                            <div class="review_helpful">
    <div class="rating_thumbs">
        			<div class="helpful_summary thumb_count">
				<a href="https://secure.metacritic.com/login">
				<span class="total_ups">0</span>
				of
				<span class="total_thumbs">0</span>
				users found this helpful
                </a>
			</div>
                <div style="clear:both;"></div>
    </div>
</div>
                                        </li>
                                                                                                                                            </ul>
                            </div>
                                                    </div>
                    </div></div></div></div>
                </li>
                                                                                    <li id="user_review_274834" class="review user_review">
                    <div class="review_btm review_btm_r"><div class="review_btm review_btm_l"><div class="review_top review_top_r"><div class="review_top review_top_l">
                        <div class="review_content">
                            <div class="review_section">
                                <div class="review_stats">
                                    <div class="review_critic">
                                        <div class="name">
                                                                                            <span>AdamS</span>
                                                                                                                                </div>
                                                                                    <div class="date">Jul  9, 2007</div>
                                                                            </div>

                                    <div class="review_grade">

<div class="metascore_w user medium movie mixed indiv">4</div>

                                    </div>
                                </div>
                                <div class="review_body">

                                        <span class="inline_expand_collapse inline_collapsed" id="review_blurb_274834"><span class="blurb blurb_collapsed"> I really enjoyed the first two movies, and I've been an off-and-on fan of the comic book. I found this movie to be one of the most over-done, over-produced, heavy-handed, plot-hole-ridden films I've seen in a long time. The director / producers wanted to put so much action into the movie, it's hard to follow what's happening within the action scenes. They don't</span><span class="blurb blurb_expanded"> I really enjoyed the first two movies, and I've been an off-and-on fan of the comic book. I found this movie to be one of the most over-done, over-produced, heavy-handed, plot-hole-ridden films I've seen in a long time. The director / producers wanted to put so much action into the movie, it's hard to follow what's happening within the action scenes. They don't even look remotely realistic anymore -- how could they, when you have Spidey and the Green Goblin battling high-speed in a 10-foot-wide alleyway, with numerous explosions and things whizzing by and shouted "witty" repartee that's really cheese-tastic? I guess the producers were going for sensory overload, but some of us actually enjoy a decent PLOT. The comedy (if you can call it that) is heavy handed and poorly written; there's a scene where Sam Raimi appears that should have been cut completely as it lasts far too long, is really cheesy and adds nothing to the story. It's almost like it's there for self-gratification and for no other reason. There are glaring plot holes that leave you wondering, why didn't that character say that earlier, before all of this happened? Scenes where Parker is being a B.A. come off as ridiculous. The Moral of the Story isn't worked into the theme, it isn't suggested to you, it's HAMMERED into you, YOU HAVE A CHOICE, DARN IT! And in case you don't catch it the first time, they actually tell you over and over again. The whole thing left me really disappointed and almost offended that the people that made this movie had done this to the franchise. If this is what the series is to become, let McGuire and the others go on to other projects and leave Spidey alone.</span><span class="blurb_etc">…</span> <a rel="nofollow" class="toggle_expand_collapse toggle_expand" href="/movie/spider-man-3/user-reviews?page=1&amp;user_review_id=274834">Expand</a></span>
            </div>
                            </div>
                                                        <div class="review_section review_actions ">
                                <ul class="review_actions">
                                                                            <li class="review_action review_helpful">
                                            <div class="review_helpful">
    <div class="rating_thumbs">
        			<div class="helpful_summary thumb_count">
				<a href="https://secure.metacritic.com/login">
				<span class="total_ups">0</span>
				of
				<span class="total_thumbs">0</span>
				users found this helpful
                </a>
			</div>
                <div style="clear:both;"></div>
    </div>
</div>
                                        </li>
                                                                                                                                            </ul>
                            </div>
                                                    </div>
                    </div></div></div></div>
                </li>
                                                                                    <li id="user_review_184961" class="review user_review">
                    <div class="review_btm review_btm_r"><div class="review_btm review_btm_l"><div class="review_top review_top_r"><div class="review_top review_top_l">
                        <div class="review_content">
                            <div class="review_section">
                                <div class="review_stats">
                                    <div class="review_critic">
                                        <div class="name">
                                                                                            <span>kurtc</span>
                                                                                                                                </div>
                                                                                    <div class="date">Jul 13, 2008</div>
                                                                            </div>

                                    <div class="review_grade">

<div class="metascore_w user medium movie positive indiv">7</div>

                                    </div>
                                </div>
                                <div class="review_body">

                                        <span> A pretty good film, though not really a magnificent one. In the comics Venom is muscular and cool. In here, he's some skinny wimp.</span>
            </div>
                            </div>
                                                        <div class="review_section review_actions ">
                                <ul class="review_actions">
                                                                            <li class="review_action review_helpful">
                                            <div class="review_helpful">
    <div class="rating_thumbs">
        			<div class="helpful_summary thumb_count">
				<a href="https://secure.metacritic.com/login">
				<span class="total_ups">0</span>
				of
				<span class="total_thumbs">0</span>
				users found this helpful
                </a>
			</div>
                <div style="clear:both;"></div>
    </div>
</div>
                                        </li>
                                                                                                                                            </ul>
                            </div>
                                                    </div>
                    </div></div></div></div>
                </li>
                                                                                    <li id="user_review_91194" class="review user_review">
                    <div class="review_btm review_btm_r"><div class="review_btm review_btm_l"><div class="review_top review_top_r"><div class="review_top review_top_l">
                        <div class="review_content">
                            <div class="review_section">
                                <div class="review_stats">
                                    <div class="review_critic">
                                        <div class="name">
                                                                                            <span>AnonymousMC</span>
                                                                                                                                </div>
                                                                                    <div class="date">Nov 24, 2007</div>
                                                                            </div>

                                    <div class="review_grade">

<div class="metascore_w user medium movie positive indiv">8</div>

                                    </div>
                                </div>
                                <div class="review_body">

                                        <span>Compared to predecessors, Spidey three is a little choppy, but that doesn't prevent it from being entertaining. the "bad" peter is an absolute blast to watch, from his more outspoken behavioral qualities to his ferocious spidey fighting. Sandman's an awesome villain, and the arc with the three friends was wrapped up nicely.</span>
            </div>
                            </div>
                                                        <div class="review_section review_actions ">
                                <ul class="review_actions">
                                                                            <li class="review_action review_helpful">
                                            <div class="review_helpful">
    <div class="rating_thumbs">
        			<div class="helpful_summary thumb_count">
				<a href="https://secure.metacritic.com/login">
				<span class="total_ups">0</span>
				of
				<span class="total_thumbs">0</span>
				users found this helpful
                </a>
			</div>
                <div style="clear:both;"></div>
    </div>
</div>
                                        </li>
                                                                                                                                            </ul>
                            </div>
                                                    </div>
                    </div></div></div></div>
                </li>
                                                                                    <li id="user_review_175418" class="review user_review">
                    <div class="review_btm review_btm_r"><div class="review_btm review_btm_l"><div class="review_top review_top_r"><div class="review_top review_top_l">
                        <div class="review_content">
                            <div class="review_section">
                                <div class="review_stats">
                                    <div class="review_critic">
                                        <div class="name">
                                                                                            <span>JohnM.</span>
                                                                                                                                </div>
                                                                                    <div class="date">Dec  4, 2007</div>
                                                                            </div>

                                    <div class="review_grade">

<div class="metascore_w user medium movie positive indiv perfect">10</div>

                                    </div>
                                </div>
                                <div class="review_body">

                                        <span> So sue me, I loved it! Action-packed and full of fun. That's what I look for in a movie.</span>
            </div>
                            </div>
                                                        <div class="review_section review_actions ">
                                <ul class="review_actions">
                                                                            <li class="review_action review_helpful">
                                            <div class="review_helpful">
    <div class="rating_thumbs">
        			<div class="helpful_summary thumb_count">
				<a href="https://secure.metacritic.com/login">
				<span class="total_ups">0</span>
				of
				<span class="total_thumbs">0</span>
				users found this helpful
                </a>
			</div>
                <div style="clear:both;"></div>
    </div>
</div>
                                        </li>
                                                                                                                                            </ul>
                            </div>
                                                    </div>
                    </div></div></div></div>
                </li>
                                                                                    <li id="user_review_278703" class="review user_review">
                    <div class="review_btm review_btm_r"><div class="review_btm review_btm_l"><div class="review_top review_top_r"><div class="review_top review_top_l">
                        <div class="review_content">
                            <div class="review_section">
                                <div class="review_stats">
                                    <div class="review_critic">
                                        <div class="name">
                                                                                            <span>DavidC.</span>
                                                                                                                                </div>
                                                                                    <div class="date">Oct 24, 2007</div>
                                                                            </div>

                                    <div class="review_grade">

<div class="metascore_w user medium movie positive indiv perfect">10</div>

                                    </div>
                                </div>
                                <div class="review_body">

                                        <span> Excellent dazzling a 4 star opera.</span>
            </div>
                            </div>
                                                        <div class="review_section review_actions ">
                                <ul class="review_actions">
                                                                            <li class="review_action review_helpful">
                                            <div class="review_helpful">
    <div class="rating_thumbs">
        			<div class="helpful_summary thumb_count">
				<a href="https://secure.metacritic.com/login">
				<span class="total_ups">0</span>
				of
				<span class="total_thumbs">0</span>
				users found this helpful
                </a>
			</div>
                <div style="clear:both;"></div>
    </div>
</div>
                                        </li>
                                                                                                                                            </ul>
                            </div>
                                                    </div>
                    </div></div></div></div>
                </li>
                                                                                    <li id="user_review_272344" class="review user_review">
                    <div class="review_btm review_btm_r"><div class="review_btm review_btm_l"><div class="review_top review_top_r"><div class="review_top review_top_l">
                        <div class="review_content">
                            <div class="review_section">
                                <div class="review_stats">
                                    <div class="review_critic">
                                        <div class="name">
                                                                                            <span>EthanR.</span>
                                                                                                                                </div>
                                                                                    <div class="date">May 10, 2007</div>
                                                                            </div>

                                    <div class="review_grade">

<div class="metascore_w user medium movie mixed indiv">6</div>

                                    </div>
                                </div>
                                <div class="review_body">

                                        <span class="inline_expand_collapse inline_collapsed" id="review_blurb_272344"><span class="blurb blurb_collapsed"> Well first things first. The action scenes in this movie are amazing. But the storyline is mediocre. I personally liked all the things that was going on. But each storyline was pretty bland. I also would like to say that Toby Maguire had a huge double chin in the movie and looked really chubby. This movie had great special effects but it doesnt make up for an average movie. The fan</span><span class="blurb blurb_expanded"> Well first things first. The action scenes in this movie are amazing. But the storyline is mediocre. I personally liked all the things that was going on. But each storyline was pretty bland. I also would like to say that Toby Maguire had a huge double chin in the movie and looked really chubby. This movie had great special effects but it doesnt make up for an average movie. The fan favorite character Venom was awful in the movie with only about 20 minutes of screen time. The only actors I thought were into the movie were Topher Grace (Venom/Eddie Brock), J.K simmons (JJ) and I don't know his name but the new goblin. Average movie overall. I recommend that everyone wait until the dvd to see it!</span><span class="blurb_etc">…</span> <a rel="nofollow" class="toggle_expand_collapse toggle_expand" href="/movie/spider-man-3/user-reviews?page=1&amp;user_review_id=272344">Expand</a></span>
            </div>
                            </div>
                                                        <div class="review_section review_actions ">
                                <ul class="review_actions">
                                                                            <li class="review_action review_helpful">
                                            <div class="review_helpful">
    <div class="rating_thumbs">
        			<div class="helpful_summary thumb_count">
				<a href="https://secure.metacritic.com/login">
				<span class="total_ups">0</span>
				of
				<span class="total_thumbs">0</span>
				users found this helpful
                </a>
			</div>
                <div style="clear:both;"></div>
    </div>
</div>
                                        </li>
                                                                                                                                            </ul>
                            </div>
                                                    </div>
                    </div></div></div></div>
                </li>
                                                                                    <li id="user_review_272394" class="review user_review">
                    <div class="review_btm review_btm_r"><div class="review_btm review_btm_l"><div class="review_top review_top_r"><div class="review_top review_top_l">
                        <div class="review_content">
                            <div class="review_section">
                                <div class="review_stats">
                                    <div class="review_critic">
                                        <div class="name">
                                                                                            <span>CoryB.</span>
                                                                                                                                </div>
                                                                                    <div class="date">May 12, 2007</div>
                                                                            </div>

                                    <div class="review_grade">

<div class="metascore_w user medium movie negative indiv">2</div>

                                    </div>
                                </div>
                                <div class="review_body">

                                        <span> I think deep down I knew this movie was going to suck the moment I saw the costume they had James Franko (harry osborne) wear. What a pile of trash Spidey 3 is. I agree with my local paper that says J.K. Simmons and Bruce Campbell should make a movie. My biggest complaint is killing off Venom and lack of script. I'm so disappointed, Mr. Raimi....</span>
            </div>
                            </div>
                                                        <div class="review_section review_actions ">
                                <ul class="review_actions">
                                                                            <li class="review_action review_helpful">
                                            <div class="review_helpful">
    <div class="rating_thumbs">
        			<div class="helpful_summary thumb_count">
				<a href="https://secure.metacritic.com/login">
				<span class="total_ups">0</span>
				of
				<span class="total_thumbs">0</span>
				users found this helpful
                </a>
			</div>
                <div style="clear:both;"></div>
    </div>
</div>
                                        </li>
                                                                                                                                            </ul>
                            </div>
                                                    </div>
                    </div></div></div></div>
                </li>
                                                                                    <li id="user_review_272399" class="review user_review">
                    <div class="review_btm review_btm_r"><div class="review_btm review_btm_l"><div class="review_top review_top_r"><div class="review_top review_top_l">
                        <div class="review_content">
                            <div class="review_section">
                                <div class="review_stats">
                                    <div class="review_critic">
                                        <div class="name">
                                                                                            <span>P.</span>
                                                                                                                                </div>
                                                                                    <div class="date">May 12, 2007</div>
                                                                            </div>

                                    <div class="review_grade">

<div class="metascore_w user medium movie mixed indiv">4</div>

                                    </div>
                                </div>
                                <div class="review_body">

                                        <span>Yawn - worst of the series - 2 was pretty good and I had high expectations but overall I felt cheated - Sam Raimi has lost the plot and I agree with the guy who said Tim Burton should do more comic movies.</span>
            </div>
                            </div>
                                                        <div class="review_section review_actions ">
                                <ul class="review_actions">
                                                                            <li class="review_action review_helpful">
                                            <div class="review_helpful">
    <div class="rating_thumbs">
        			<div class="helpful_summary thumb_count">
				<a href="https://secure.metacritic.com/login">
				<span class="total_ups">0</span>
				of
				<span class="total_thumbs">0</span>
				users found this helpful
                </a>
			</div>
                <div style="clear:both;"></div>
    </div>
</div>
                                        </li>
                                                                                                                                            </ul>
                            </div>
                                                    </div>
                    </div></div></div></div>
                </li>
                                                                                    <li id="user_review_272438" class="review user_review">
                    <div class="review_btm review_btm_r"><div class="review_btm review_btm_l"><div class="review_top review_top_r"><div class="review_top review_top_l">
                        <div class="review_content">
                            <div class="review_section">
                                <div class="review_stats">
                                    <div class="review_critic">
                                        <div class="name">
                                                                                            <span>DuncanI.</span>
                                                                                                                                </div>
                                                                                    <div class="date">May 13, 2007</div>
                                                                            </div>

                                    <div class="review_grade">

<div class="metascore_w user medium movie negative indiv">1</div>

                                    </div>
                                </div>
                                <div class="review_body">

                                        <span> This is a shocker I went to see it today and I was so disapointed! It is a cross between Battle Field Earth &amp; Days of Our Lives. Don't bother yourself in seeing it just tell your Kids Spiderman was hit by a truck and died straight after the better Spiderman 2.</span>
            </div>
                            </div>
                                                        <div class="review_section review_actions ">
                                <ul class="review_actions">
                                                                            <li class="review_action review_helpful">
                                            <div class="review_helpful">
    <div class="rating_thumbs">
        			<div class="helpful_summary thumb_count">
				<a href="https://secure.metacritic.com/login">
				<span class="total_ups">0</span>
				of
				<span class="total_thumbs">0</span>
				users found this helpful
                </a>
			</div>
                <div style="clear:both;"></div>
    </div>
</div>
                                        </li>
                                                                                                                                            </ul>
                            </div>
                                                    </div>
                    </div></div></div></div>
                </li>
                                                                                    <li id="user_review_272334" class="review user_review">
                    <div class="review_btm review_btm_r"><div class="review_btm review_btm_l"><div class="review_top review_top_r"><div class="review_top review_top_l">
                        <div class="review_content">
                            <div class="review_section">
                                <div class="review_stats">
                                    <div class="review_critic">
                                        <div class="name">
                                                                                            <span>BillD.</span>
                                                                                                                                </div>
                                                                                    <div class="date">May 10, 2007</div>
                                                                            </div>

                                    <div class="review_grade">

<div class="metascore_w user medium movie positive indiv">8</div>

                                    </div>
                                </div>
                                <div class="review_body">

                                        <span> Best of the trilogy. Very successful management of multiple complex characters.</span>
            </div>
                            </div>
                                                        <div class="review_section review_actions ">
                                <ul class="review_actions">
                                                                            <li class="review_action review_helpful">
                                            <div class="review_helpful">
    <div class="rating_thumbs">
        			<div class="helpful_summary thumb_count">
				<a href="https://secure.metacritic.com/login">
				<span class="total_ups">0</span>
				of
				<span class="total_thumbs">0</span>
				users found this helpful
                </a>
			</div>
                <div style="clear:both;"></div>
    </div>
</div>
                                        </li>
                                                                                                                                            </ul>
                            </div>
                                                    </div>
                    </div></div></div></div>
                </li>
                                                                                    <li id="user_review_272521" class="review user_review">
                    <div class="review_btm review_btm_r"><div class="review_btm review_btm_l"><div class="review_top review_top_r"><div class="review_top review_top_l">
                        <div class="review_content">
                            <div class="review_section">
                                <div class="review_stats">
                                    <div class="review_critic">
                                        <div class="name">
                                                                                            <span>BrutusO.</span>
                                                                                                                                </div>
                                                                                    <div class="date">May 14, 2007</div>
                                                                            </div>

                                    <div class="review_grade">

<div class="metascore_w user medium movie positive indiv">8</div>

                                    </div>
                                </div>
                                <div class="review_body">

                                        <span class="inline_expand_collapse inline_collapsed" id="review_blurb_272521"><span class="blurb blurb_collapsed"> Everyone is being little over-critical here. Yes, it isn't as good as the last one. Yes, Harry and Mary Jane have outstayed their welcome. Yes the exposition of the story is a tad too complicated. But if you are a SpiderMan fan, this is still pretty good. For one thing, Venom is done brilliantly. And the Sandman comes in a close second. And Peter Parker is as hapless and nerdy as in</span><span class="blurb blurb_expanded"> Everyone is being little over-critical here. Yes, it isn't as good as the last one. Yes, Harry and Mary Jane have outstayed their welcome. Yes the exposition of the story is a tad too complicated. But if you are a SpiderMan fan, this is still pretty good. For one thing, Venom is done brilliantly. And the Sandman comes in a close second. And Peter Parker is as hapless and nerdy as in the comic. And there are lots of good supporting perormances eg J Jonah Jameson, and Robbie Robertson, and Betty, and Gwen Stacey isnt all that bad either. Should be films be made for broad audiences, or for the fan base? Decide for yourself, however the fans are not ill-served here. A little too long (hardly unusual these days), but a blockbuster anyway.An honourable attempt to keep the franchise going. When does Carnage hit the screen? I will go to the next one.</span><span class="blurb_etc">…</span> <a rel="nofollow" class="toggle_expand_collapse toggle_expand" href="/movie/spider-man-3/user-reviews?page=1&amp;user_review_id=272521">Expand</a></span>
            </div>
                            </div>
                                                        <div class="review_section review_actions ">
                                <ul class="review_actions">
                                                                            <li class="review_action review_helpful">
                                            <div class="review_helpful">
    <div class="rating_thumbs">
        			<div class="helpful_summary thumb_count">
				<a href="https://secure.metacritic.com/login">
				<span class="total_ups">0</span>
				of
				<span class="total_thumbs">0</span>
				users found this helpful
                </a>
			</div>
                <div style="clear:both;"></div>
    </div>
</div>
                                        </li>
                                                                                                                                            </ul>
                            </div>
                                                    </div>
                    </div></div></div></div>
                </li>
                                                                                    <li id="user_review_272530" class="review user_review">
                    <div class="review_btm review_btm_r"><div class="review_btm review_btm_l"><div class="review_top review_top_r"><div class="review_top review_top_l">
                        <div class="review_content">
                            <div class="review_section">
                                <div class="review_stats">
                                    <div class="review_critic">
                                        <div class="name">
                                                                                            <span>BretG.</span>
                                                                                                                                </div>
                                                                                    <div class="date">May 14, 2007</div>
                                                                            </div>

                                    <div class="review_grade">

<div class="metascore_w user medium movie mixed indiv">6</div>

                                    </div>
                                </div>
                                <div class="review_body">

                                        <span class="inline_expand_collapse inline_collapsed" id="review_blurb_272530"><span class="blurb blurb_collapsed"> While delivering what you expect from a Spiderman movie, the film fails to deliver as its predesessors did. The whole time it seems like waiting on Venom to arrive in the series is unbearable. Venom, being a large focal point in the trailers and what not, sees minimal time on the screen and needless to say, it doesnt look like hes going to be in any more Spiderman movies either. While it</span><span class="blurb blurb_expanded"> While delivering what you expect from a Spiderman movie, the film fails to deliver as its predesessors did. The whole time it seems like waiting on Venom to arrive in the series is unbearable. Venom, being a large focal point in the trailers and what not, sees minimal time on the screen and needless to say, it doesnt look like hes going to be in any more Spiderman movies either. While it may be the worst Spiderman movie its not the worst movie ever made. A 6. Lets hope that the Venom movie can make up for this, as long as Raimi isnt working on it.</span><span class="blurb_etc">…</span> <a rel="nofollow" class="toggle_expand_collapse toggle_expand" href="/movie/spider-man-3/user-reviews?page=1&amp;user_review_id=272530">Expand</a></span>
            </div>
                            </div>
                                                        <div class="review_section review_actions ">
                                <ul class="review_actions">
                                                                            <li class="review_action review_helpful">
                                            <div class="review_helpful">
    <div class="rating_thumbs">
        			<div class="helpful_summary thumb_count">
				<a href="https://secure.metacritic.com/login">
				<span class="total_ups">0</span>
				of
				<span class="total_thumbs">0</span>
				users found this helpful
                </a>
			</div>
                <div style="clear:both;"></div>
    </div>
</div>
                                        </li>
                                                                                                                                            </ul>
                            </div>
                                                    </div>
                    </div></div></div></div>
                </li>
                                                                                    <li id="user_review_272534" class="review user_review">
                    <div class="review_btm review_btm_r"><div class="review_btm review_btm_l"><div class="review_top review_top_r"><div class="review_top review_top_l">
                        <div class="review_content">
                            <div class="review_section">
                                <div class="review_stats">
                                    <div class="review_critic">
                                        <div class="name">
                                                                                            <span>MarcyT.</span>
                                                                                                                                </div>
                                                                                    <div class="date">May 14, 2007</div>
                                                                            </div>

                                    <div class="review_grade">

<div class="metascore_w user medium movie negative indiv">3</div>

                                    </div>
                                </div>
                                <div class="review_body">

                                        <span> Verdict from two parents and all three teenagers, 2 boys, 1 girl? It was bad. We were actually bored and wishing for it to end already so we could leave. The Sandman was interesting, but the director never decided if he was a bad guy or a good guy, so he seemed like a sidekick at best. After you see the Sandman born in the first half hour, you</span>
            </div>
                            </div>
                                                        <div class="review_section review_actions ">
                                <ul class="review_actions">
                                                                            <li class="review_action review_helpful">
                                            <div class="review_helpful">
    <div class="rating_thumbs">
        			<div class="helpful_summary thumb_count">
				<a href="https://secure.metacritic.com/login">
				<span class="total_ups">0</span>
				of
				<span class="total_thumbs">0</span>
				users found this helpful
                </a>
			</div>
                <div style="clear:both;"></div>
    </div>
</div>
                                        </li>
                                                                                                                                            </ul>
                            </div>
                                                    </div>
                    </div></div></div></div>
                </li>
                                                                                    <li id="user_review_272335" class="review user_review">
                    <div class="review_btm review_btm_r"><div class="review_btm review_btm_l"><div class="review_top review_top_r"><div class="review_top review_top_l">
                        <div class="review_content">
                            <div class="review_section">
                                <div class="review_stats">
                                    <div class="review_critic">
                                        <div class="name">
                                                                                            <span>IanH.</span>
                                                                                                                                </div>
                                                                                    <div class="date">May 10, 2007</div>
                                                                            </div>

                                    <div class="review_grade">

<div class="metascore_w user medium movie negative indiv">2</div>

                                    </div>
                                </div>
                                <div class="review_body">

                                        <span> The writing was horrible, and the action was mediocre -- not nearly good enough to make up for the unrealistic characters and dialogue.</span>
            </div>
                            </div>
                                                        <div class="review_section review_actions ">
                                <ul class="review_actions">
                                                                            <li class="review_action review_helpful">
                                            <div class="review_helpful">
    <div class="rating_thumbs">
        			<div class="helpful_summary thumb_count">
				<a href="https://secure.metacritic.com/login">
				<span class="total_ups">0</span>
				of
				<span class="total_thumbs">0</span>
				users found this helpful
                </a>
			</div>
                <div style="clear:both;"></div>
    </div>
</div>
                                        </li>
                                                                                                                                            </ul>
                            </div>
                                                    </div>
                    </div></div></div></div>
                </li>
                                                                                    <li id="user_review_90408" class="review user_review">
                    <div class="review_btm review_btm_r"><div class="review_btm review_btm_l"><div class="review_top review_top_r"><div class="review_top review_top_l">
                        <div class="review_content">
                            <div class="review_section">
                                <div class="review_stats">
                                    <div class="review_critic">
                                        <div class="name">
                                                                                            <span>julainmyles</span>
                                                                                                                                </div>
                                                                                    <div class="date">May 15, 2007</div>
                                                                            </div>

                                    <div class="review_grade">

<div class="metascore_w user medium movie mixed indiv">5</div>

                                    </div>
                                </div>
                                <div class="review_body">

                                        <span class="inline_expand_collapse inline_collapsed" id="review_blurb_90408"><span class="blurb blurb_collapsed">good but not as good as it could have been, to quote a friend 'spiderman 3 takes the other two movies and gobbles there balls', i dont feel that strongly against it, but i some of the scenes in the middle like the jazz bar? wtf? the over two films were sensational, this just got over the top emotionally, and the comic parker would never had done that top MJ, the film over all was</span><span class="blurb blurb_expanded">good but not as good as it could have been, to quote a friend 'spiderman 3 takes the other two movies and gobbles there balls', i dont feel that strongly against it, but i some of the scenes in the middle like the jazz bar? wtf? the over two films were sensational, this just got over the top emotionally, and the comic parker would never had done that top MJ, the film over all was alright, but nothing special, i was expecting much much better than that.</span><span class="blurb_etc">…</span> <a rel="nofollow" class="toggle_expand_collapse toggle_expand" href="/movie/spider-man-3/user-reviews?page=1&amp;user_review_id=90408">Expand</a></span>
            </div>
                            </div>
                                                        <div class="review_section review_actions ">
                                <ul class="review_actions">
                                                                            <li class="review_action review_helpful">
                                            <div class="review_helpful">
    <div class="rating_thumbs">
        			<div class="helpful_summary thumb_count">
				<a href="https://secure.metacritic.com/login">
				<span class="total_ups">0</span>
				of
				<span class="total_thumbs">0</span>
				users found this helpful
                </a>
			</div>
                <div style="clear:both;"></div>
    </div>
</div>
                                        </li>
                                                                                                                                            </ul>
                            </div>
                                                    </div>
                    </div></div></div></div>
                </li>
                                                                                    <li id="user_review_272623" class="review user_review">
                    <div class="review_btm review_btm_r"><div class="review_btm review_btm_l"><div class="review_top review_top_r"><div class="review_top review_top_l">
                        <div class="review_content">
                            <div class="review_section">
                                <div class="review_stats">
                                    <div class="review_critic">
                                        <div class="name">
                                                                                            <span>Brent</span>
                                                                                                                                </div>
                                                                                    <div class="date">May 17, 2007</div>
                                                                            </div>

                                    <div class="review_grade">

<div class="metascore_w user medium movie negative indiv">2</div>

                                    </div>
                                </div>
                                <div class="review_body">

                                        <span class="inline_expand_collapse inline_collapsed" id="review_blurb_272623"><span class="blurb blurb_collapsed"> Absolutely terrible. Venom deserved to be a movie unto himself, not one of three plot lines. They could have made the movie dark and sinister (see Batman Begins), but instead they made it cheesey and pathetic (see Batman Forever and Batman and Robin). Venom could have been aggressive and cool. Instead they tried to make him a cocky ladies man, but they were working with Toby Maguire and</span><span class="blurb blurb_expanded"> Absolutely terrible. Venom deserved to be a movie unto himself, not one of three plot lines. They could have made the movie dark and sinister (see Batman Begins), but instead they made it cheesey and pathetic (see Batman Forever and Batman and Robin). Venom could have been aggressive and cool. Instead they tried to make him a cocky ladies man, but they were working with Toby Maguire and Topher Gracen so needless to say, they failed miserably. It's the worst sequel I've seen since the second Matrix. I was literally laughing at times and covering my eyes at others because of how bad and awkward it was.</span><span class="blurb_etc">…</span> <a rel="nofollow" class="toggle_expand_collapse toggle_expand" href="/movie/spider-man-3/user-reviews?page=1&amp;user_review_id=272623">Expand</a></span>
            </div>
                            </div>
                                                        <div class="review_section review_actions ">
                                <ul class="review_actions">
                                                                            <li class="review_action review_helpful">
                                            <div class="review_helpful">
    <div class="rating_thumbs">
        			<div class="helpful_summary thumb_count">
				<a href="https://secure.metacritic.com/login">
				<span class="total_ups">0</span>
				of
				<span class="total_thumbs">0</span>
				users found this helpful
                </a>
			</div>
                <div style="clear:both;"></div>
    </div>
</div>
                                        </li>
                                                                                                                                            </ul>
                            </div>
                                                    </div>
                    </div></div></div></div>
                </li>
                                                                                    <li id="user_review_272746" class="review user_review">
                    <div class="review_btm review_btm_r"><div class="review_btm review_btm_l"><div class="review_top review_top_r"><div class="review_top review_top_l">
                        <div class="review_content">
                            <div class="review_section">
                                <div class="review_stats">
                                    <div class="review_critic">
                                        <div class="name">
                                                                                            <span>DanaM.</span>
                                                                                                                                </div>
                                                                                    <div class="date">May 21, 2007</div>
                                                                            </div>

                                    <div class="review_grade">

<div class="metascore_w user medium movie negative indiv">3</div>

                                    </div>
                                </div>
                                <div class="review_body">

                                        <span> Awful. I just can't see why the directors used Toby in the first place. Total miscast. The dance scene by Parker in the jazz club was hilarious, but I'm sure not intended. Embarrasing is more like it. Not worth the $10 to see the movie. Toby has got to go!</span>
            </div>
                            </div>
                                                        <div class="review_section review_actions ">
                                <ul class="review_actions">
                                                                            <li class="review_action review_helpful">
                                            <div class="review_helpful">
    <div class="rating_thumbs">
        			<div class="helpful_summary thumb_count">
				<a href="https://secure.metacritic.com/login">
				<span class="total_ups">0</span>
				of
				<span class="total_thumbs">0</span>
				users found this helpful
                </a>
			</div>
                <div style="clear:both;"></div>
    </div>
</div>
                                        </li>
                                                                                                                                            </ul>
                            </div>
                                                    </div>
                    </div></div></div></div>
                </li>
                                                                                    <li id="user_review_272804" class="review user_review">
                    <div class="review_btm review_btm_r"><div class="review_btm review_btm_l"><div class="review_top review_top_r"><div class="review_top review_top_l">
                        <div class="review_content">
                            <div class="review_section">
                                <div class="review_stats">
                                    <div class="review_critic">
                                        <div class="name">
                                                                                            <span>PaulI.</span>
                                                                                                                                </div>
                                                                                    <div class="date">May 23, 2007</div>
                                                                            </div>

                                    <div class="review_grade">

<div class="metascore_w user medium movie positive indiv">9</div>

                                    </div>
                                </div>
                                <div class="review_body">

                                        <span> Spider-Man is back! And in black? Anyways, this movie is extremely enjoyable with memorable villains, battle scenes and drama. But the movie, just like any other movie, has its downsides.</span>
            </div>
                            </div>
                                                        <div class="review_section review_actions ">
                                <ul class="review_actions">
                                                                            <li class="review_action review_helpful">
                                            <div class="review_helpful">
    <div class="rating_thumbs">
        			<div class="helpful_summary thumb_count">
				<a href="https://secure.metacritic.com/login">
				<span class="total_ups">0</span>
				of
				<span class="total_thumbs">0</span>
				users found this helpful
                </a>
			</div>
                <div style="clear:both;"></div>
    </div>
</div>
                                        </li>
                                                                                                                                            </ul>
                            </div>
                                                    </div>
                    </div></div></div></div>
                </li>
                                                                                    <li id="user_review_272850" class="review user_review">
                    <div class="review_btm review_btm_r"><div class="review_btm review_btm_l"><div class="review_top review_top_r"><div class="review_top review_top_l">
                        <div class="review_content">
                            <div class="review_section">
                                <div class="review_stats">
                                    <div class="review_critic">
                                        <div class="name">
                                                                                            <span>DLM</span>
                                                                                                                                </div>
                                                                                    <div class="date">May 24, 2007</div>
                                                                            </div>

                                    <div class="review_grade">

<div class="metascore_w user medium movie negative indiv">3</div>

                                    </div>
                                </div>
                                <div class="review_body">

                                        <span> Spider-Man 3 is to the web-slinger what Batman &amp; Robin was to the dark knight. It</span>
            </div>
                            </div>
                                                        <div class="review_section review_actions ">
                                <ul class="review_actions">
                                                                            <li class="review_action review_helpful">
                                            <div class="review_helpful">
    <div class="rating_thumbs">
        			<div class="helpful_summary thumb_count">
				<a href="https://secure.metacritic.com/login">
				<span class="total_ups">0</span>
				of
				<span class="total_thumbs">0</span>
				users found this helpful
                </a>
			</div>
                <div style="clear:both;"></div>
    </div>
</div>
                                        </li>
                                                                                                                                            </ul>
                            </div>
                                                    </div>
                    </div></div></div></div>
                </li>
                                                                                    <li id="user_review_272007" class="review user_review">
                    <div class="review_btm review_btm_r"><div class="review_btm review_btm_l"><div class="review_top review_top_r"><div class="review_top review_top_l">
                        <div class="review_content">
                            <div class="review_section">
                                <div class="review_stats">
                                    <div class="review_critic">
                                        <div class="name">
                                                                                            <span>MatthewK.</span>
                                                                                                                                </div>
                                                                                    <div class="date">May  4, 2007</div>
                                                                            </div>

                                    <div class="review_grade">

<div class="metascore_w user medium movie positive indiv">9</div>

                                    </div>
                                </div>
                                <div class="review_body">

                                        <span class="inline_expand_collapse inline_collapsed" id="review_blurb_272007"><span class="blurb blurb_collapsed">Actually i'd give it an 8.5 but whatever. this film was flawed, yes. but was by no means a bad movie, i have seen bad movies (fantastic 4, x-men: laststand, daredevil) and this is not a bad film at all. it's as good as part 1 if not a little better. not nearly as convulted as i had thought it's be. it's pacing was all wacky and wrong in the last 45 minutes but otherwise</span><span class="blurb blurb_expanded">Actually i'd give it an 8.5 but whatever. this film was flawed, yes. but was by no means a bad movie, i have seen bad movies (fantastic 4, x-men: laststand, daredevil) and this is not a bad film at all. it's as good as part 1 if not a little better. not nearly as convulted as i had thought it's be. it's pacing was all wacky and wrong in the last 45 minutes but otherwise it was insanely entertaining. amazing, amazing special effects. this is pretty much the return of the jedi of the trilogy; good but still has its problems.</span><span class="blurb_etc">…</span> <a rel="nofollow" class="toggle_expand_collapse toggle_expand" href="/movie/spider-man-3/user-reviews?page=1&amp;user_review_id=272007">Expand</a></span>
            </div>
                            </div>
                                                        <div class="review_section review_actions ">
                                <ul class="review_actions">
                                                                            <li class="review_action review_helpful">
                                            <div class="review_helpful">
    <div class="rating_thumbs">
        			<div class="helpful_summary thumb_count">
				<a href="https://secure.metacritic.com/login">
				<span class="total_ups">0</span>
				of
				<span class="total_thumbs">0</span>
				users found this helpful
                </a>
			</div>
                <div style="clear:both;"></div>
    </div>
</div>
                                        </li>
                                                                                                                                            </ul>
                            </div>
                                                    </div>
                    </div></div></div></div>
                </li>
                                                                                    <li id="user_review_272020" class="review user_review">
                    <div class="review_btm review_btm_r"><div class="review_btm review_btm_l"><div class="review_top review_top_r"><div class="review_top review_top_l">
                        <div class="review_content">
                            <div class="review_section">
                                <div class="review_stats">
                                    <div class="review_critic">
                                        <div class="name">
                                                                                            <span>FilmFella</span>
                                                                                                                                </div>
                                                                                    <div class="date">May  4, 2007</div>
                                                                            </div>

                                    <div class="review_grade">

<div class="metascore_w user medium movie positive indiv">8</div>

                                    </div>
                                </div>
                                <div class="review_body">

                                        <span> Though the movie is a bit long and a bit slow at times, this will easily be one of the best movies of the summer and most fun movies of the year. Smarter and Funnier than the previous movies help 3 find its niche in the Marvel Hall of Heros.</span>
            </div>
                            </div>
                                                        <div class="review_section review_actions ">
                                <ul class="review_actions">
                                                                            <li class="review_action review_helpful">
                                            <div class="review_helpful">
    <div class="rating_thumbs">
        			<div class="helpful_summary thumb_count">
				<a href="https://secure.metacritic.com/login">
				<span class="total_ups">0</span>
				of
				<span class="total_thumbs">0</span>
				users found this helpful
                </a>
			</div>
                <div style="clear:both;"></div>
    </div>
</div>
                                        </li>
                                                                                                                                            </ul>
                            </div>
                                                    </div>
                    </div></div></div></div>
                </li>
                                                                                    <li id="user_review_272008" class="review user_review">
                    <div class="review_btm review_btm_r"><div class="review_btm review_btm_l"><div class="review_top review_top_r"><div class="review_top review_top_l">
                        <div class="review_content">
                            <div class="review_section">
                                <div class="review_stats">
                                    <div class="review_critic">
                                        <div class="name">
                                                                                            <span>Andrewfidel1ty</span>
                                                                                                                                </div>
                                                                                    <div class="date">May  4, 2007</div>
                                                                            </div>

                                    <div class="review_grade">

<div class="metascore_w user medium movie positive indiv">7</div>

                                    </div>
                                </div>
                                <div class="review_body">

                                        <span> I enjoy this movie. It is interesting and cinematic.</span>
            </div>
                            </div>
                                                        <div class="review_section review_actions ">
                                <ul class="review_actions">
                                                                            <li class="review_action review_helpful">
                                            <div class="review_helpful">
    <div class="rating_thumbs">
        			<div class="helpful_summary thumb_count">
				<a href="https://secure.metacritic.com/login">
				<span class="total_ups">0</span>
				of
				<span class="total_thumbs">0</span>
				users found this helpful
                </a>
			</div>
                <div style="clear:both;"></div>
    </div>
</div>
                                        </li>
                                                                                                                                            </ul>
                            </div>
                                                    </div>
                    </div></div></div></div>
                </li>
                                                                                    <li id="user_review_271980" class="review user_review">
                    <div class="review_btm review_btm_r"><div class="review_btm review_btm_l"><div class="review_top review_top_r"><div class="review_top review_top_l">
                        <div class="review_content">
                            <div class="review_section">
                                <div class="review_stats">
                                    <div class="review_critic">
                                        <div class="name">
                                                                                            <span>BobS.</span>
                                                                                                                                </div>
                                                                                    <div class="date">May  4, 2007</div>
                                                                            </div>

                                    <div class="review_grade">

<div class="metascore_w user medium movie mixed indiv">5</div>

                                    </div>
                                </div>
                                <div class="review_body">

                                        <span>Special effects action is too fast to see and in your face (zoomed in). half the movie is an emotional soap opera and i only saw it because i saw 1 and 2</span>
            </div>
                            </div>
                                                        <div class="review_section review_actions ">
                                <ul class="review_actions">
                                                                            <li class="review_action review_helpful">
                                            <div class="review_helpful">
    <div class="rating_thumbs">
        			<div class="helpful_summary thumb_count">
				<a href="https://secure.metacritic.com/login">
				<span class="total_ups">0</span>
				of
				<span class="total_thumbs">0</span>
				users found this helpful
                </a>
			</div>
                <div style="clear:both;"></div>
    </div>
</div>
                                        </li>
                                                                                                                                            </ul>
                            </div>
                                                    </div>
                    </div></div></div></div>
                </li>
                                                                                    <li id="user_review_272009" class="review user_review">
                    <div class="review_btm review_btm_r"><div class="review_btm review_btm_l"><div class="review_top review_top_r"><div class="review_top review_top_l">
                        <div class="review_content">
                            <div class="review_section">
                                <div class="review_stats">
                                    <div class="review_critic">
                                        <div class="name">
                                                                                            <span>TheoC.</span>
                                                                                                                                </div>
                                                                                    <div class="date">May  4, 2007</div>
                                                                            </div>

                                    <div class="review_grade">

<div class="metascore_w user medium movie positive indiv">9</div>

                                    </div>
                                </div>
                                <div class="review_body">

                                        <span class="inline_expand_collapse inline_collapsed" id="review_blurb_272009"><span class="blurb blurb_collapsed"> Powerfully gripping, and touching film, and Harry Osborn was actually good in this film. Too bad the Eddie Brock character seemed inconsistent, and the plot seemed rushed. Haydn Church was great in the bit role as the down on his luck, the good-hearted but criminally Sandman, and this film was awesome. Venom was great in the two halves, and as Eddie Brock, but I didn't think they</span><span class="blurb blurb_expanded"> Powerfully gripping, and touching film, and Harry Osborn was actually good in this film. Too bad the Eddie Brock character seemed inconsistent, and the plot seemed rushed. Haydn Church was great in the bit role as the down on his luck, the good-hearted but criminally Sandman, and this film was awesome. Venom was great in the two halves, and as Eddie Brock, but I didn't think they linked up well together. Just my opinion. Good storyline, and buddy buddy film.</span><span class="blurb_etc">…</span> <a rel="nofollow" class="toggle_expand_collapse toggle_expand" href="/movie/spider-man-3/user-reviews?page=1&amp;user_review_id=272009">Expand</a></span>
            </div>
                            </div>
                                                        <div class="review_section review_actions ">
                                <ul class="review_actions">
                                                                            <li class="review_action review_helpful">
                                            <div class="review_helpful">
    <div class="rating_thumbs">
        			<div class="helpful_summary thumb_count">
				<a href="https://secure.metacritic.com/login">
				<span class="total_ups">0</span>
				of
				<span class="total_thumbs">0</span>
				users found this helpful
                </a>
			</div>
                <div style="clear:both;"></div>
    </div>
</div>
                                        </li>
                                                                                                                                            </ul>
                            </div>
                                                    </div>
                    </div></div></div></div>
                </li>
                                                                                    <li id="user_review_272026" class="review user_review">
                    <div class="review_btm review_btm_r"><div class="review_btm review_btm_l"><div class="review_top review_top_r"><div class="review_top review_top_l">
                        <div class="review_content">
                            <div class="review_section">
                                <div class="review_stats">
                                    <div class="review_critic">
                                        <div class="name">
                                                                                            <span>LeeF.</span>
                                                                                                                                </div>
                                                                                    <div class="date">May  4, 2007</div>
                                                                            </div>

                                    <div class="review_grade">

<div class="metascore_w user medium movie mixed indiv">4</div>

                                    </div>
                                </div>
                                <div class="review_body">

                                        <span> Mediocre and not enough payoff for sitting through the boring stuff.</span>
            </div>
                            </div>
                                                        <div class="review_section review_actions ">
                                <ul class="review_actions">
                                                                            <li class="review_action review_helpful">
                                            <div class="review_helpful">
    <div class="rating_thumbs">
        			<div class="helpful_summary thumb_count">
				<a href="https://secure.metacritic.com/login">
				<span class="total_ups">0</span>
				of
				<span class="total_thumbs">0</span>
				users found this helpful
                </a>
			</div>
                <div style="clear:both;"></div>
    </div>
</div>
                                        </li>
                                                                                                                                            </ul>
                            </div>
                                                    </div>
                    </div></div></div></div>
                </li>
                                                                                    <li id="user_review_272030" class="review user_review">
                    <div class="review_btm review_btm_r"><div class="review_btm review_btm_l"><div class="review_top review_top_r"><div class="review_top review_top_l">
                        <div class="review_content">
                            <div class="review_section">
                                <div class="review_stats">
                                    <div class="review_critic">
                                        <div class="name">
                                                                                            <span>JosephO.</span>
                                                                                                                                </div>
                                                                                    <div class="date">May  4, 2007</div>
                                                                            </div>

                                    <div class="review_grade">

<div class="metascore_w user medium movie positive indiv perfect">10</div>

                                    </div>
                                </div>
                                <div class="review_body">

                                        <span> The people who don't understand the brooding apparently didn't understand the mechanics of the material that came from the meteorite. It ENHANCES emotions/powers, so when he is in the black suit, ALL of his emotions are enhanced...</span>
            </div>
                            </div>
                                                        <div class="review_section review_actions ">
                                <ul class="review_actions">
                                                                            <li class="review_action review_helpful">
                                            <div class="review_helpful">
    <div class="rating_thumbs">
        			<div class="helpful_summary thumb_count">
				<a href="https://secure.metacritic.com/login">
				<span class="total_ups">0</span>
				of
				<span class="total_thumbs">0</span>
				users found this helpful
                </a>
			</div>
                <div style="clear:both;"></div>
    </div>
</div>
                                        </li>
                                                                                                                                            </ul>
                            </div>
                                                    </div>
                    </div></div></div></div>
                </li>
                                                                                    <li id="user_review_272031" class="review user_review">
                    <div class="review_btm review_btm_r"><div class="review_btm review_btm_l"><div class="review_top review_top_r"><div class="review_top review_top_l">
                        <div class="review_content">
                            <div class="review_section">
                                <div class="review_stats">
                                    <div class="review_critic">
                                        <div class="name">
                                                                                            <span>GregB.</span>
                                                                                                                                </div>
                                                                                    <div class="date">May  4, 2007</div>
                                                                            </div>

                                    <div class="review_grade">

<div class="metascore_w user medium movie negative indiv">2</div>

                                    </div>
                                </div>
                                <div class="review_body">

                                        <span class="inline_expand_collapse inline_collapsed" id="review_blurb_272031"><span class="blurb blurb_collapsed"> This movie has "Blockbuster" written all over it, but in this case that is a BAD thing. What I mean is that this was certainly CALCULATED to be a mega-blockbuster, and it looks like all anybody cared about was making a lot of money. I used to be a big Marvel comicbook fan. I am giddy with joy on the all-to-rare occasions when they get a super-hero movie right. The 1st 2 Superman's</span><span class="blurb blurb_expanded"> This movie has "Blockbuster" written all over it, but in this case that is a BAD thing. What I mean is that this was certainly CALCULATED to be a mega-blockbuster, and it looks like all anybody cared about was making a lot of money. I used to be a big Marvel comicbook fan. I am giddy with joy on the all-to-rare occasions when they get a super-hero movie right. The 1st 2 Superman's did it, the X-Men's got it very right, but there has been precious little besides those. I didn't care much for the 1st Spiderman. I appreciated that it was trying to be character driven, but a lot of the plot points used a bludgeon instead of a scalpal. So I didn't expect much from a continued series. But amazingly Spiderman 2 was a lot of fun. Alfred Molina really elevated the film as Doc Oc and there were other good things. But Spidey 3 was mostly painful to watch. I'd already read a lot of mixed reviews and I expected there would be problems, but I just wanted something that would be at least mildly fun. Some of the action MIGHT have been fun, in an otherwise decent film. But I was cringing at too many other factors. I WANTED very badly to find the redeeming qualities of this movie, but it was a useless hope. I am really baffled at all of the positive reviews. I really makes me question a lot of the sophmoric values that seem to be more and more prevalent in the society. It seems that people are losing track of what good film is about. On the other side it seems that lately there's been a lot of Nic Cage bashing in films that may not have been classics but that I found entertaining. National Treasure was a prime example of that. Sure, it wasn't the DaVinci Code (the book) but neither was the film version of that. And I found Nic Cage's new action sci-fi flick to be good fun. Those who didn't love the comics, please understand, if there are any good ideas in Spidey 3 they are Marvel's NOT Sam Raimi's. This film is just calculated to take in a lot of money. And for a time it may just succeed. When critics pick their worst films of the year they rarely really choose the absolute trash. They usually choose the films that had a lot of hype and were supposed to be major box office draws. In other words, the films that disappointed heightened expectations the most. Within that criteria, I would have the say that Spidey 3 is one of the worst movies of the year.</span><span class="blurb_etc">…</span> <a rel="nofollow" class="toggle_expand_collapse toggle_expand" href="/movie/spider-man-3/user-reviews?page=1&amp;user_review_id=272031">Expand</a></span>
            </div>
                            </div>
                                                        <div class="review_section review_actions ">
                                <ul class="review_actions">
                                                                            <li class="review_action review_helpful">
                                            <div class="review_helpful">
    <div class="rating_thumbs">
        			<div class="helpful_summary thumb_count">
				<a href="https://secure.metacritic.com/login">
				<span class="total_ups">0</span>
				of
				<span class="total_thumbs">0</span>
				users found this helpful
                </a>
			</div>
                <div style="clear:both;"></div>
    </div>
</div>
                                        </li>
                                                                                                                                            </ul>
                            </div>
                                                    </div>
                    </div></div></div></div>
                </li>
                                                                                    <li id="user_review_272039" class="review user_review">
                    <div class="review_btm review_btm_r"><div class="review_btm review_btm_l"><div class="review_top review_top_r"><div class="review_top review_top_l">
                        <div class="review_content">
                            <div class="review_section">
                                <div class="review_stats">
                                    <div class="review_critic">
                                        <div class="name">
                                                                                            <span>TomG.</span>
                                                                                                                                </div>
                                                                                    <div class="date">May  4, 2007</div>
                                                                            </div>

                                    <div class="review_grade">

<div class="metascore_w user medium movie mixed indiv">5</div>

                                    </div>
                                </div>
                                <div class="review_body">

                                        <span> This movie was basically all hype. The fight scenes were played very well, but the dialouge was horrible. Toby cant stop smiling can he? Even when he's crying. I really do not recommend this movie.</span>
            </div>
                            </div>
                                                        <div class="review_section review_actions ">
                                <ul class="review_actions">
                                                                            <li class="review_action review_helpful">
                                            <div class="review_helpful">
    <div class="rating_thumbs">
        			<div class="helpful_summary thumb_count">
				<a href="https://secure.metacritic.com/login">
				<span class="total_ups">0</span>
				of
				<span class="total_thumbs">0</span>
				users found this helpful
                </a>
			</div>
                <div style="clear:both;"></div>
    </div>
</div>
                                        </li>
                                                                                                                                            </ul>
                            </div>
                                                    </div>
                    </div></div></div></div>
                </li>
                                                                                    <li id="user_review_272049" class="review user_review">
                    <div class="review_btm review_btm_r"><div class="review_btm review_btm_l"><div class="review_top review_top_r"><div class="review_top review_top_l">
                        <div class="review_content">
                            <div class="review_section">
                                <div class="review_stats">
                                    <div class="review_critic">
                                        <div class="name">
                                                                                            <span>RonP.</span>
                                                                                                                                </div>
                                                                                    <div class="date">May  4, 2007</div>
                                                                            </div>

                                    <div class="review_grade">

<div class="metascore_w user medium movie negative indiv">1</div>

                                    </div>
                                </div>
                                <div class="review_body">

                                        <span class="inline_expand_collapse inline_collapsed" id="review_blurb_272049"><span class="blurb blurb_collapsed"> One of the worst films I have seen. Truly awful in literally every respect. If one more actor cried onscreen, I would have vomited on the row in front of me. Too convoluted, too unintentionally funny. I can't believe I won't get these 2.5 hours back. I can't even get my money back. I adored the first two films, but Raimi became too self-indulgent. Avoid at all costs, and</span><span class="blurb blurb_expanded"> One of the worst films I have seen. Truly awful in literally every respect. If one more actor cried onscreen, I would have vomited on the row in front of me. Too convoluted, too unintentionally funny. I can't believe I won't get these 2.5 hours back. I can't even get my money back. I adored the first two films, but Raimi became too self-indulgent. Avoid at all costs, and make up a resolution for yourself in your head. I guarantee it'll be better than this Hollywood tripe.</span><span class="blurb_etc">…</span> <a rel="nofollow" class="toggle_expand_collapse toggle_expand" href="/movie/spider-man-3/user-reviews?page=1&amp;user_review_id=272049">Expand</a></span>
            </div>
                            </div>
                                                        <div class="review_section review_actions ">
                                <ul class="review_actions">
                                                                            <li class="review_action review_helpful">
                                            <div class="review_helpful">
    <div class="rating_thumbs">
        			<div class="helpful_summary thumb_count">
				<a href="https://secure.metacritic.com/login">
				<span class="total_ups">0</span>
				of
				<span class="total_thumbs">0</span>
				users found this helpful
                </a>
			</div>
                <div style="clear:both;"></div>
    </div>
</div>
                                        </li>
                                                                                                                                            </ul>
                            </div>
                                                    </div>
                    </div></div></div></div>
                </li>
                                                                                    <li id="user_review_271982" class="review user_review">
                    <div class="review_btm review_btm_r"><div class="review_btm review_btm_l"><div class="review_top review_top_r"><div class="review_top review_top_l">
                        <div class="review_content">
                            <div class="review_section">
                                <div class="review_stats">
                                    <div class="review_critic">
                                        <div class="name">
                                                                                            <span>Ryencoke</span>
                                                                                                                                </div>
                                                                                    <div class="date">May  4, 2007</div>
                                                                            </div>

                                    <div class="review_grade">

<div class="metascore_w user medium movie negative indiv">1</div>

                                    </div>
                                </div>
                                <div class="review_body">

                                        <span class="inline_expand_collapse inline_collapsed" id="review_blurb_271982"><span class="blurb blurb_collapsed"> Where do I begin? This movie was possibly one of the worst sequels to a marvel movie. It was horrible. If you want to watch a love story for 2 hours of the movie, go see it. This movie wasn't Spider-man, it was "The Notebook" + "Fantastic 4". I am so furious on how horribly done this movie was. I was looking so forward to Venom, and they couldn't even do his character right.</span><span class="blurb blurb_expanded"> Where do I begin? This movie was possibly one of the worst sequels to a marvel movie. It was horrible. If you want to watch a love story for 2 hours of the movie, go see it. This movie wasn't Spider-man, it was "The Notebook" + "Fantastic 4". I am so furious on how horribly done this movie was. I was looking so forward to Venom, and they couldn't even do his character right. He's the same size as Spider-man if not smaller. And shoots the webs from the top of his hand. Sam Raimi you seriously screwed this one up.</span><span class="blurb_etc">…</span> <a rel="nofollow" class="toggle_expand_collapse toggle_expand" href="/movie/spider-man-3/user-reviews?page=1&amp;user_review_id=271982">Expand</a></span>
            </div>
                            </div>
                                                        <div class="review_section review_actions ">
                                <ul class="review_actions">
                                                                            <li class="review_action review_helpful">
                                            <div class="review_helpful">
    <div class="rating_thumbs">
        			<div class="helpful_summary thumb_count">
				<a href="https://secure.metacritic.com/login">
				<span class="total_ups">0</span>
				of
				<span class="total_thumbs">0</span>
				users found this helpful
                </a>
			</div>
                <div style="clear:both;"></div>
    </div>
</div>
                                        </li>
                                                                                                                                            </ul>
                            </div>
                                                    </div>
                    </div></div></div></div>
                </li>
                                                                                    <li id="user_review_272046" class="review user_review">
                    <div class="review_btm review_btm_r"><div class="review_btm review_btm_l"><div class="review_top review_top_r"><div class="review_top review_top_l">
                        <div class="review_content">
                            <div class="review_section">
                                <div class="review_stats">
                                    <div class="review_critic">
                                        <div class="name">
                                                                                            <span>MitchK.</span>
                                                                                                                                </div>
                                                                                    <div class="date">May  4, 2007</div>
                                                                            </div>

                                    <div class="review_grade">

<div class="metascore_w user medium movie mixed indiv">5</div>

                                    </div>
                                </div>
                                <div class="review_body">

                                        <span class="inline_expand_collapse inline_collapsed" id="review_blurb_272046"><span class="blurb blurb_collapsed">[ ***SPOILERS***]  If this movie was 1 and a half hours shorter with a new ending, less dialogue and struting/jazz dancing, it would have been great. Sandman's new, yet conceivable, backstory was a good addition to the film and somewhat faithful to the comics. Venom, however, was a little less faithful, although the church scene was very good. And Harry's death sequence was</span><span class="blurb blurb_expanded">[ ***SPOILERS***]  If this movie was 1 and a half hours shorter with a new ending, less dialogue and struting/jazz dancing, it would have been great. Sandman's new, yet conceivable, backstory was a good addition to the film and somewhat faithful to the comics. Venom, however, was a little less faithful, although the church scene was very good. And Harry's death sequence was actually pretty decent and, although it was under different circumstances, Raimi made it faithful to Lee's comics. As usual, Rosemary Harris is amazing as Parker's aunt and makes this ride a little less rocky. She and the incredible action sequences (what few of them there were) saved this movie from being a total abomination. No, what really made this movie bad was Spiderman himself, Tobey Maguire. The things Raimi made the dark, cocky Spiderman do were completely over-the-top. Just brutal! That jazz dancing scene in front of Mary-Jane was God awful. That and the dancing down the street that kept getting worse by the minute. That and the huge cliches at the end that totally ruined it made this one hard to watch all the way through. So, this is my suggestion: Keep the Sandman story, keep the battles between Harry and Peter, get rid of those damn French waitors and Pete's crazy attitude and the jazz dancing and make this a movie really worth watching. Sam Raimi's better than this, Spiderman 2 was awesome with Doc Oc! This one though, jeez. I say this as an average guy going to see an action flick: BRING YOUR GIRLFRIEND!!!! The 3-hour make-out session will be a hell of alot better than Spidey walking down the street giving the guns to the ladies. Seriously, lower your expectations before going in. There are some great effects and action sequences, but overall, I'd wait for the DVD.</span><span class="blurb_etc">…</span> <a rel="nofollow" class="toggle_expand_collapse toggle_expand" href="/movie/spider-man-3/user-reviews?page=1&amp;user_review_id=272046">Expand</a></span>
            </div>
                            </div>
                                                        <div class="review_section review_actions ">
                                <ul class="review_actions">
                                                                            <li class="review_action review_helpful">
                                            <div class="review_helpful">
    <div class="rating_thumbs">
        			<div class="helpful_summary thumb_count">
				<a href="https://secure.metacritic.com/login">
				<span class="total_ups">0</span>
				of
				<span class="total_thumbs">0</span>
				users found this helpful
                </a>
			</div>
                <div style="clear:both;"></div>
    </div>
</div>
                                        </li>
                                                                                                                                            </ul>
                            </div>
                                                    </div>
                    </div></div></div></div>
                </li>
                                                                                    <li id="user_review_271986" class="review user_review">
                    <div class="review_btm review_btm_r"><div class="review_btm review_btm_l"><div class="review_top review_top_r"><div class="review_top review_top_l">
                        <div class="review_content">
                            <div class="review_section">
                                <div class="review_stats">
                                    <div class="review_critic">
                                        <div class="name">
                                                                                            <span>JimA.</span>
                                                                                                                                </div>
                                                                                    <div class="date">May  4, 2007</div>
                                                                            </div>

                                    <div class="review_grade">

<div class="metascore_w user medium movie positive indiv">8</div>

                                    </div>
                                </div>
                                <div class="review_body">

                                        <span> I don't really know why critics rate this movie so low and I am totally opposed to that. The movie was good but it could be better if it had a much more better end!!</span>
            </div>
                            </div>
                                                        <div class="review_section review_actions ">
                                <ul class="review_actions">
                                                                            <li class="review_action review_helpful">
                                            <div class="review_helpful">
    <div class="rating_thumbs">
        			<div class="helpful_summary thumb_count">
				<a href="https://secure.metacritic.com/login">
				<span class="total_ups">0</span>
				of
				<span class="total_thumbs">0</span>
				users found this helpful
                </a>
			</div>
                <div style="clear:both;"></div>
    </div>
</div>
                                        </li>
                                                                                                                                            </ul>
                            </div>
                                                    </div>
                    </div></div></div></div>
                </li>
                                                                                    <li id="user_review_271989" class="review user_review">
                    <div class="review_btm review_btm_r"><div class="review_btm review_btm_l"><div class="review_top review_top_r"><div class="review_top review_top_l">
                        <div class="review_content">
                            <div class="review_section">
                                <div class="review_stats">
                                    <div class="review_critic">
                                        <div class="name">
                                                                                            <span>KarlB.</span>
                                                                                                                                </div>
                                                                                    <div class="date">May  4, 2007</div>
                                                                            </div>

                                    <div class="review_grade">

<div class="metascore_w user medium movie negative indiv">2</div>

                                    </div>
                                </div>
                                <div class="review_body">

                                        <span class="inline_expand_collapse inline_collapsed" id="review_blurb_271989"><span class="blurb blurb_collapsed"> Honestly TMNT was better, if you can imagine. This film is horrifying. The dialogue is trite, the acting wooden, the "plot" splintered, and boring. Even with 3 villians there isn't enough action. I laughed at the tender moments and cried at funny ones. I feel like I get Sam Raimi, but his work just doesn't play when spun out into a Summer Blockbuster. I know everyone will go see</span><span class="blurb blurb_expanded"> Honestly TMNT was better, if you can imagine. This film is horrifying. The dialogue is trite, the acting wooden, the "plot" splintered, and boring. Even with 3 villians there isn't enough action. I laughed at the tender moments and cried at funny ones. I feel like I get Sam Raimi, but his work just doesn't play when spun out into a Summer Blockbuster. I know everyone will go see this movie anyway, but I'm glad to be on the record saying, don't waste your time.</span><span class="blurb_etc">…</span> <a rel="nofollow" class="toggle_expand_collapse toggle_expand" href="/movie/spider-man-3/user-reviews?page=1&amp;user_review_id=271989">Expand</a></span>
            </div>
                            </div>
                                                        <div class="review_section review_actions ">
                                <ul class="review_actions">
                                                                            <li class="review_action review_helpful">
                                            <div class="review_helpful">
    <div class="rating_thumbs">
        			<div class="helpful_summary thumb_count">
				<a href="https://secure.metacritic.com/login">
				<span class="total_ups">0</span>
				of
				<span class="total_thumbs">0</span>
				users found this helpful
                </a>
			</div>
                <div style="clear:both;"></div>
    </div>
</div>
                                        </li>
                                                                                                                                            </ul>
                            </div>
                                                    </div>
                    </div></div></div></div>
                </li>
                                                                                    <li id="user_review_271994" class="review user_review">
                    <div class="review_btm review_btm_r"><div class="review_btm review_btm_l"><div class="review_top review_top_r"><div class="review_top review_top_l">
                        <div class="review_content">
                            <div class="review_section">
                                <div class="review_stats">
                                    <div class="review_critic">
                                        <div class="name">
                                                                                            <span>JimB.</span>
                                                                                                                                </div>
                                                                                    <div class="date">May  4, 2007</div>
                                                                            </div>

                                    <div class="review_grade">

<div class="metascore_w user medium movie negative indiv">3</div>

                                    </div>
                                </div>
                                <div class="review_body">

                                        <span> Was great until the second half, when Raimi decided to barrage us with every single cliche that exists in superhero movies, as well as a self-important fight between spider-man, a non-canon venom, and an enemy that to me resembled the stay-puft marshmallow man from Ghostbusters.</span>
            </div>
                            </div>
                                                        <div class="review_section review_actions ">
                                <ul class="review_actions">
                                                                            <li class="review_action review_helpful">
                                            <div class="review_helpful">
    <div class="rating_thumbs">
        			<div class="helpful_summary thumb_count">
				<a href="https://secure.metacritic.com/login">
				<span class="total_ups">0</span>
				of
				<span class="total_thumbs">0</span>
				users found this helpful
                </a>
			</div>
                <div style="clear:both;"></div>
    </div>
</div>
                                        </li>
                                                                                                                                            </ul>
                            </div>
                                                    </div>
                    </div></div></div></div>
                </li>
                                                                                    <li id="user_review_271997" class="review user_review">
                    <div class="review_btm review_btm_r"><div class="review_btm review_btm_l"><div class="review_top review_top_r"><div class="review_top review_top_l">
                        <div class="review_content">
                            <div class="review_section">
                                <div class="review_stats">
                                    <div class="review_critic">
                                        <div class="name">
                                                                                            <span>JoshuaS.</span>
                                                                                                                                </div>
                                                                                    <div class="date">May  4, 2007</div>
                                                                            </div>

                                    <div class="review_grade">

<div class="metascore_w user medium movie negative indiv">1</div>

                                    </div>
                                </div>
                                <div class="review_body">

                                        <span> It's so bad one wonders if Raimi didn't sabotage it on purpose. We're talking Batman &amp; Robin bad.</span>
            </div>
                            </div>
                                                        <div class="review_section review_actions ">
                                <ul class="review_actions">
                                                                            <li class="review_action review_helpful">
                                            <div class="review_helpful">
    <div class="rating_thumbs">
        			<div class="helpful_summary thumb_count">
				<a href="https://secure.metacritic.com/login">
				<span class="total_ups">0</span>
				of
				<span class="total_thumbs">0</span>
				users found this helpful
                </a>
			</div>
                <div style="clear:both;"></div>
    </div>
</div>
                                        </li>
                                                                                                                                            </ul>
                            </div>
                                                    </div>
                    </div></div></div></div>
                </li>
                                                                                    <li id="user_review_271999" class="review user_review">
                    <div class="review_btm review_btm_r"><div class="review_btm review_btm_l"><div class="review_top review_top_r"><div class="review_top review_top_l">
                        <div class="review_content">
                            <div class="review_section">
                                <div class="review_stats">
                                    <div class="review_critic">
                                        <div class="name">
                                                                                            <span>MikeH.</span>
                                                                                                                                </div>
                                                                                    <div class="date">May  4, 2007</div>
                                                                            </div>

                                    <div class="review_grade">

<div class="metascore_w user medium movie positive indiv">9</div>

                                    </div>
                                </div>
                                <div class="review_body">

                                        <span> this film is so much damn fun. very formulaic and cliche heavy, but when you have a budget in excess of 300 million, why the hell would you want to be edgy. almost anyone who walks into the cinema knows what they're going to get. don't expect to be challenged, just enjoy it.</span>
            </div>
                            </div>
                                                        <div class="review_section review_actions ">
                                <ul class="review_actions">
                                                                            <li class="review_action review_helpful">
                                            <div class="review_helpful">
    <div class="rating_thumbs">
        			<div class="helpful_summary thumb_count">
				<a href="https://secure.metacritic.com/login">
				<span class="total_ups">0</span>
				of
				<span class="total_thumbs">0</span>
				users found this helpful
                </a>
			</div>
                <div style="clear:both;"></div>
    </div>
</div>
                                        </li>
                                                                                                                                            </ul>
                            </div>
                                                    </div>
                    </div></div></div></div>
                </li>
                                                                                    <li id="user_review_272002" class="review user_review">
                    <div class="review_btm review_btm_r"><div class="review_btm review_btm_l"><div class="review_top review_top_r"><div class="review_top review_top_l">
                        <div class="review_content">
                            <div class="review_section">
                                <div class="review_stats">
                                    <div class="review_critic">
                                        <div class="name">
                                                                                            <span>DwightM.</span>
                                                                                                                                </div>
                                                                                    <div class="date">May  4, 2007</div>
                                                                            </div>

                                    <div class="review_grade">

<div class="metascore_w user medium movie positive indiv">7</div>

                                    </div>
                                </div>
                                <div class="review_body">

                                        <span> I give this a 7 because in grade-school, a 70 is a C for average. I felt that this movie was average when compared to what we've already seen from this franchise. I was expecting lots more but received even less. I am sorry to see these characters go like this. Alas.</span>
            </div>
                            </div>
                                                        <div class="review_section review_actions ">
                                <ul class="review_actions">
                                                                            <li class="review_action review_helpful">
                                            <div class="review_helpful">
    <div class="rating_thumbs">
        			<div class="helpful_summary thumb_count">
				<a href="https://secure.metacritic.com/login">
				<span class="total_ups">0</span>
				of
				<span class="total_thumbs">0</span>
				users found this helpful
                </a>
			</div>
                <div style="clear:both;"></div>
    </div>
</div>
                                        </li>
                                                                                                                                            </ul>
                            </div>
                                                    </div>
                    </div></div></div></div>
                </li>
                                                                                    <li id="user_review_272064" class="review user_review">
                    <div class="review_btm review_btm_r"><div class="review_btm review_btm_l"><div class="review_top review_top_r"><div class="review_top review_top_l">
                        <div class="review_content">
                            <div class="review_section">
                                <div class="review_stats">
                                    <div class="review_critic">
                                        <div class="name">
                                                                                            <span>RonJ.</span>
                                                                                                                                </div>
                                                                                    <div class="date">May  5, 2007</div>
                                                                            </div>

                                    <div class="review_grade">

<div class="metascore_w user medium movie positive indiv perfect">10</div>

                                    </div>
                                </div>
                                <div class="review_body">

                                        <span class="inline_expand_collapse inline_collapsed" id="review_blurb_272064"><span class="blurb blurb_collapsed"> Clever and unconvential, this sort of film applies to independent film students, college kids, but not your average elderly crowd or for the entire family. Still it provides raucous laughter, and despite this division, it is necessary because even though it creates controversy, it is needed to show that everyday people are not one-dimensional people, and that not everything is so</span><span class="blurb blurb_expanded"> Clever and unconvential, this sort of film applies to independent film students, college kids, but not your average elderly crowd or for the entire family. Still it provides raucous laughter, and despite this division, it is necessary because even though it creates controversy, it is needed to show that everyday people are not one-dimensional people, and that not everything is so cut-and-dry. Their message hits this home, and this is why this film is so powerful.</span><span class="blurb_etc">…</span> <a rel="nofollow" class="toggle_expand_collapse toggle_expand" href="/movie/spider-man-3/user-reviews?page=1&amp;user_review_id=272064">Expand</a></span>
            </div>
                            </div>
                                                        <div class="review_section review_actions ">
                                <ul class="review_actions">
                                                                            <li class="review_action review_helpful">
                                            <div class="review_helpful">
    <div class="rating_thumbs">
        			<div class="helpful_summary thumb_count">
				<a href="https://secure.metacritic.com/login">
				<span class="total_ups">0</span>
				of
				<span class="total_thumbs">0</span>
				users found this helpful
                </a>
			</div>
                <div style="clear:both;"></div>
    </div>
</div>
                                        </li>
                                                                                                                                            </ul>
                            </div>
                                                    </div>
                    </div></div></div></div>
                </li>
                                                                                    <li id="user_review_272102" class="review user_review">
                    <div class="review_btm review_btm_r"><div class="review_btm review_btm_l"><div class="review_top review_top_r"><div class="review_top review_top_l">
                        <div class="review_content">
                            <div class="review_section">
                                <div class="review_stats">
                                    <div class="review_critic">
                                        <div class="name">
                                                                                            <span>JohnB.</span>
                                                                                                                                </div>
                                                                                    <div class="date">May  5, 2007</div>
                                                                            </div>

                                    <div class="review_grade">

<div class="metascore_w user medium movie positive indiv perfect">10</div>

                                    </div>
                                </div>
                                <div class="review_body">

                                        <span> I went to the theater expecting to be entertained and I was. It has just as much "soul" as the others and actually pushes more boundaries than anyone could expect it to. One thing that was a little weird was Peter Parker's double chin. Oh well.</span>
            </div>
                            </div>
                                                        <div class="review_section review_actions ">
                                <ul class="review_actions">
                                                                            <li class="review_action review_helpful">
                                            <div class="review_helpful">
    <div class="rating_thumbs">
        			<div class="helpful_summary thumb_count">
				<a href="https://secure.metacritic.com/login">
				<span class="total_ups">0</span>
				of
				<span class="total_thumbs">0</span>
				users found this helpful
                </a>
			</div>
                <div style="clear:both;"></div>
    </div>
</div>
                                        </li>
                                                                                                                                            </ul>
                            </div>
                                                    </div>
                    </div></div></div></div>
                </li>
                                                                                    <li id="user_review_272103" class="review user_review">
                    <div class="review_btm review_btm_r"><div class="review_btm review_btm_l"><div class="review_top review_top_r"><div class="review_top review_top_l">
                        <div class="review_content">
                            <div class="review_section">
                                <div class="review_stats">
                                    <div class="review_critic">
                                        <div class="name">
                                                                                            <span>MatthewM.</span>
                                                                                                                                </div>
                                                                                    <div class="date">May  5, 2007</div>
                                                                            </div>

                                    <div class="review_grade">

<div class="metascore_w user medium movie positive indiv">9</div>

                                    </div>
                                </div>
                                <div class="review_body">

                                        <span>Sure its no Spider-man 1 or 2, but its nonetheless fantastic. CGI at a all time high. Acting most impressive. Definetly a must-see.</span>
            </div>
                            </div>
                                                        <div class="review_section review_actions ">
                                <ul class="review_actions">
                                                                            <li class="review_action review_helpful">
                                            <div class="review_helpful">
    <div class="rating_thumbs">
        			<div class="helpful_summary thumb_count">
				<a href="https://secure.metacritic.com/login">
				<span class="total_ups">0</span>
				of
				<span class="total_thumbs">0</span>
				users found this helpful
                </a>
			</div>
                <div style="clear:both;"></div>
    </div>
</div>
                                        </li>
                                                                                                                                            </ul>
                            </div>
                                                    </div>
                    </div></div></div></div>
                </li>
                                                                                    <li id="user_review_272065" class="review user_review">
                    <div class="review_btm review_btm_r"><div class="review_btm review_btm_l"><div class="review_top review_top_r"><div class="review_top review_top_l">
                        <div class="review_content">
                            <div class="review_section">
                                <div class="review_stats">
                                    <div class="review_critic">
                                        <div class="name">
                                                                                            <span>Patrick</span>
                                                                                                                                </div>
                                                                                    <div class="date">May  5, 2007</div>
                                                                            </div>

                                    <div class="review_grade">

<div class="metascore_w user medium movie negative indiv">0</div>

                                    </div>
                                </div>
                                <div class="review_body">

                                        <span> Awful movie from start to finish. It included every horrible movie cliche, and was far more chick flick than action film. The special effects were completely overdone and added nothing to terrible acting, dialogue, plot, etc. DO NOT SEE.</span>
            </div>
                            </div>
                                                        <div class="review_section review_actions ">
                                <ul class="review_actions">
                                                                            <li class="review_action review_helpful">
                                            <div class="review_helpful">
    <div class="rating_thumbs">
        			<div class="helpful_summary thumb_count">
				<a href="https://secure.metacritic.com/login">
				<span class="total_ups">0</span>
				of
				<span class="total_thumbs">0</span>
				users found this helpful
                </a>
			</div>
                <div style="clear:both;"></div>
    </div>
</div>
                                        </li>
                                                                                                                                            </ul>
                            </div>
                                                    </div>
                    </div></div></div></div>
                </li>
                                                                                    <li id="user_review_272068" class="review user_review">
                    <div class="review_btm review_btm_r"><div class="review_btm review_btm_l"><div class="review_top review_top_r"><div class="review_top review_top_l">
                        <div class="review_content">
                            <div class="review_section">
                                <div class="review_stats">
                                    <div class="review_critic">
                                        <div class="name">
                                                                                            <span>GeoffP.</span>
                                                                                                                                </div>
                                                                                    <div class="date">May  5, 2007</div>
                                                                            </div>

                                    <div class="review_grade">

<div class="metascore_w user medium movie positive indiv">8</div>

                                    </div>
                                </div>
                                <div class="review_body">

                                        <span> Cheesy plot and dialogue aside, the acting was very good, the humor was decent, and overall good enough action to keep me entertained.</span>
            </div>
                            </div>
                                                        <div class="review_section review_actions ">
                                <ul class="review_actions">
                                                                            <li class="review_action review_helpful">
                                            <div class="review_helpful">
    <div class="rating_thumbs">
        			<div class="helpful_summary thumb_count">
				<a href="https://secure.metacritic.com/login">
				<span class="total_ups">0</span>
				of
				<span class="total_thumbs">0</span>
				users found this helpful
                </a>
			</div>
                <div style="clear:both;"></div>
    </div>
</div>
                                        </li>
                                                                                                                                            </ul>
                            </div>
                                                    </div>
                    </div></div></div></div>
                </li>
                                                                                    <li id="user_review_272069" class="review user_review">
                    <div class="review_btm review_btm_r"><div class="review_btm review_btm_l"><div class="review_top review_top_r"><div class="review_top review_top_l">
                        <div class="review_content">
                            <div class="review_section">
                                <div class="review_stats">
                                    <div class="review_critic">
                                        <div class="name">
                                                                                            <span>LukeA.</span>
                                                                                                                                </div>
                                                                                    <div class="date">May  5, 2007</div>
                                                                            </div>

                                    <div class="review_grade">

<div class="metascore_w user medium movie positive indiv">9</div>

                                    </div>
                                </div>
                                <div class="review_body">

                                        <span> This is far from perfect, but it still is a fun and exciting installment into the spider-man franchise. It has plenty of action, laughs as well as serious moments. Its campy and cheesy at times but thats because its a comic book movie. Go in wanting to have fun and not to critique every little detail.</span>
            </div>
                            </div>
                                                        <div class="review_section review_actions ">
                                <ul class="review_actions">
                                                                            <li class="review_action review_helpful">
                                            <div class="review_helpful">
    <div class="rating_thumbs">
        			<div class="helpful_summary thumb_count">
				<a href="https://secure.metacritic.com/login">
				<span class="total_ups">0</span>
				of
				<span class="total_thumbs">0</span>
				users found this helpful
                </a>
			</div>
                <div style="clear:both;"></div>
    </div>
</div>
                                        </li>
                                                                                                                                            </ul>
                            </div>
                                                    </div>
                    </div></div></div></div>
                </li>
                                                                                    <li id="user_review_272070" class="review user_review">
                    <div class="review_btm review_btm_r"><div class="review_btm review_btm_l"><div class="review_top review_top_r"><div class="review_top review_top_l">
                        <div class="review_content">
                            <div class="review_section">
                                <div class="review_stats">
                                    <div class="review_critic">
                                        <div class="name">
                                                                                            <span>PerroD.</span>
                                                                                                                                </div>
                                                                                    <div class="date">May  5, 2007</div>
                                                                            </div>

                                    <div class="review_grade">

<div class="metascore_w user medium movie positive indiv">9</div>

                                    </div>
                                </div>
                                <div class="review_body">

                                        <span class="inline_expand_collapse inline_collapsed" id="review_blurb_272070"><span class="blurb blurb_collapsed"> I thought the movie was great. If you go in expecting it to be as great as the first sequel then you might be a bit dissapointed. there are some solid performances from the cast especially from Thomas Haydn Church as Marko Flint and from James Franco as Harry Osborn/The New Goblin. this one is also alot funnier than the other two movies with peter parker taking on a much more emo/goofy</span><span class="blurb blurb_expanded"> I thought the movie was great. If you go in expecting it to be as great as the first sequel then you might be a bit dissapointed. there are some solid performances from the cast especially from Thomas Haydn Church as Marko Flint and from James Franco as Harry Osborn/The New Goblin. this one is also alot funnier than the other two movies with peter parker taking on a much more emo/goofy persona at about halfway through the movie. the effects were better this time around and even provided for a few jumps out of my seat. my only beef with this installment is that the ending was kind of awkward and somber and left much to be desired. but besides that the movie was fantastic and will probably be the best movie of the season.</span><span class="blurb_etc">…</span> <a rel="nofollow" class="toggle_expand_collapse toggle_expand" href="/movie/spider-man-3/user-reviews?page=1&amp;user_review_id=272070">Expand</a></span>
            </div>
                            </div>
                                                        <div class="review_section review_actions ">
                                <ul class="review_actions">
                                                                            <li class="review_action review_helpful">
                                            <div class="review_helpful">
    <div class="rating_thumbs">
        			<div class="helpful_summary thumb_count">
				<a href="https://secure.metacritic.com/login">
				<span class="total_ups">0</span>
				of
				<span class="total_thumbs">0</span>
				users found this helpful
                </a>
			</div>
                <div style="clear:both;"></div>
    </div>
</div>
                                        </li>
                                                                                                                                            </ul>
                            </div>
                                                    </div>
                    </div></div></div></div>
                </li>
                                                                                    <li id="user_review_272071" class="review user_review">
                    <div class="review_btm review_btm_r"><div class="review_btm review_btm_l"><div class="review_top review_top_r"><div class="review_top review_top_l">
                        <div class="review_content">
                            <div class="review_section">
                                <div class="review_stats">
                                    <div class="review_critic">
                                        <div class="name">
                                                                                            <span>PeterRollingO.</span>
                                                                                                                                </div>
                                                                                    <div class="date">May  5, 2007</div>
                                                                            </div>

                                    <div class="review_grade">

<div class="metascore_w user medium movie positive indiv perfect">10</div>

                                    </div>
                                </div>
                                <div class="review_body">

                                        <span class="inline_expand_collapse inline_collapsed" id="review_blurb_272071"><span class="blurb blurb_collapsed"> In my opinion, the 2nd Spiderman was one of the best superhero movies ever made. It had the perfect balance of character development and action, and flowed smoothly. Because of that lasting impression, I went into the 3rd one with extremely high expectations - and therein lies the problem. If you took this movie by itself, and you had never seen the first two, you might think this was an</span><span class="blurb blurb_expanded"> In my opinion, the 2nd Spiderman was one of the best superhero movies ever made. It had the perfect balance of character development and action, and flowed smoothly. Because of that lasting impression, I went into the 3rd one with extremely high expectations - and therein lies the problem. If you took this movie by itself, and you had never seen the first two, you might think this was an incredible flick. And it is... when you compare it to most other comic-based films. But, rather annoyingly, there is a tendency to compare entries of a franchise with each other. In terms of what could have been better about it, it's not that the film is too long (I love long movies, like Lord of the Rings and Braveheart); it's that, in the time allotted, so much is being crammed that you kind of want the filmmakers to do one of two things: (1) either make this into two separate movies, or (2) make it 3 hours long and smooth out the rough edges. It seemed that a lot was left on the cutting room floor in an attempt to keep this under 3 hours. I told the guy sitting next to me that I could have sat another 30 minutes, because the best thing about this series is that the characters are so likeable. Sure, some scenes were dragged out a bit too long (e.g. when Parker has a 'bad'-itude and is strutting his stuff), but that really didn't bother me, because those scenes were funny (this is by far the funniest of the 3 movies). Like I said, it just seemed like the editor got a little "scissors-happy" and, as a result, the film seems choppy at times. Again, this could have been made into 2 phenomenal films or been turned into a "Return of the King-ish" guilty pleasure. Regardless, it was worth my money and I would like to see it again, just to determine if my opinion about it changes after a second helping. A masterpiece it is not, but it does make for a decent superhero movie, and I hope the 4th one gets made.</span><span class="blurb_etc">…</span> <a rel="nofollow" class="toggle_expand_collapse toggle_expand" href="/movie/spider-man-3/user-reviews?page=1&amp;user_review_id=272071">Expand</a></span>
            </div>
                            </div>
                                                        <div class="review_section review_actions ">
                                <ul class="review_actions">
                                                                            <li class="review_action review_helpful">
                                            <div class="review_helpful">
    <div class="rating_thumbs">
        			<div class="helpful_summary thumb_count">
				<a href="https://secure.metacritic.com/login">
				<span class="total_ups">0</span>
				of
				<span class="total_thumbs">0</span>
				users found this helpful
                </a>
			</div>
                <div style="clear:both;"></div>
    </div>
</div>
                                        </li>
                                                                                                                                            </ul>
                            </div>
                                                    </div>
                    </div></div></div></div>
                </li>
                                                                                    <li id="user_review_272072" class="review user_review">
                    <div class="review_btm review_btm_r"><div class="review_btm review_btm_l"><div class="review_top review_top_r"><div class="review_top review_top_l">
                        <div class="review_content">
                            <div class="review_section">
                                <div class="review_stats">
                                    <div class="review_critic">
                                        <div class="name">
                                                                                            <span>JohnnyP.</span>
                                                                                                                                </div>
                                                                                    <div class="date">May  5, 2007</div>
                                                                            </div>

                                    <div class="review_grade">

<div class="metascore_w user medium movie positive indiv">8</div>

                                    </div>
                                </div>
                                <div class="review_body">

                                        <span> A damn good film that exceeded my expectations. Reading from the reviews, I didn't expect much, but hey, it was well worth my time, and I say it's worth more than one viewing.</span>
            </div>
                            </div>
                                                        <div class="review_section review_actions ">
                                <ul class="review_actions">
                                                                            <li class="review_action review_helpful">
                                            <div class="review_helpful">
    <div class="rating_thumbs">
        			<div class="helpful_summary thumb_count">
				<a href="https://secure.metacritic.com/login">
				<span class="total_ups">0</span>
				of
				<span class="total_thumbs">0</span>
				users found this helpful
                </a>
			</div>
                <div style="clear:both;"></div>
    </div>
</div>
                                        </li>
                                                                                                                                            </ul>
                            </div>
                                                    </div>
                    </div></div></div></div>
                </li>
                                                                                    <li id="user_review_90258" class="review user_review">
                    <div class="review_btm review_btm_r"><div class="review_btm review_btm_l"><div class="review_top review_top_r"><div class="review_top review_top_l">
                        <div class="review_content">
                            <div class="review_section">
                                <div class="review_stats">
                                    <div class="review_critic">
                                        <div class="name">
                                                                                            <span>AnonymousMC</span>
                                                                                                                                </div>
                                                                                    <div class="date">May  5, 2007</div>
                                                                            </div>

                                    <div class="review_grade">

<div class="metascore_w user medium movie positive indiv">9</div>

                                    </div>
                                </div>
                                <div class="review_body">

                                        <span class="inline_expand_collapse inline_collapsed" id="review_blurb_90258"><span class="blurb blurb_collapsed">It really ashame the critics are really messing this up.The film has a dark side alot like the comic.  I'm so glad that this film doesn't put a warm and fuzzy in everyones heart.It's not suppose to ..A really under appreciated film..Maybe Fantastic 4 is more for the critics liking ....a really well crafted film..Nice to see the old Sam ways of story telling  ..Thank you Sam</span><span class="blurb blurb_expanded">It really ashame the critics are really messing this up.The film has a dark side alot like the comic.  I'm so glad that this film doesn't put a warm and fuzzy in everyones heart.It's not suppose to ..A really under appreciated film..Maybe Fantastic 4 is more for the critics liking ....a really well crafted film..Nice to see the old Sam ways of story telling  ..Thank you Sam Rami.......</span><span class="blurb_etc">…</span> <a rel="nofollow" class="toggle_expand_collapse toggle_expand" href="/movie/spider-man-3/user-reviews?page=1&amp;user_review_id=90258">Expand</a></span>
            </div>
                            </div>
                                                        <div class="review_section review_actions ">
                                <ul class="review_actions">
                                                                            <li class="review_action review_helpful">
                                            <div class="review_helpful">
    <div class="rating_thumbs">
        			<div class="helpful_summary thumb_count">
				<a href="https://secure.metacritic.com/login">
				<span class="total_ups">0</span>
				of
				<span class="total_thumbs">0</span>
				users found this helpful
                </a>
			</div>
                <div style="clear:both;"></div>
    </div>
</div>
                                        </li>
                                                                                                                                            </ul>
                            </div>
                                                    </div>
                    </div></div></div></div>
                </li>
                                                                                    <li id="user_review_272074" class="review user_review">
                    <div class="review_btm review_btm_r"><div class="review_btm review_btm_l"><div class="review_top review_top_r"><div class="review_top review_top_l">
                        <div class="review_content">
                            <div class="review_section">
                                <div class="review_stats">
                                    <div class="review_critic">
                                        <div class="name">
                                                                                            <span>LewisB.</span>
                                                                                                                                </div>
                                                                                    <div class="date">May  5, 2007</div>
                                                                            </div>

                                    <div class="review_grade">

<div class="metascore_w user medium movie positive indiv perfect">10</div>

                                    </div>
                                </div>
                                <div class="review_body">

                                        <span class="inline_expand_collapse inline_collapsed" id="review_blurb_272074"><span class="blurb blurb_collapsed"> Spider-Man 3 is the Lawrence Of Arabia of the superhero movies world. It is epic, sprawling, magnificent, meaningful, beautiful. Anyone who doesn't enjoy this movie must be a pretty spoilt brat or a cynical old misery. For near on three hours it envelops you in its world and makes you CARE about the characters. How's that for a special effects laden blockbuster, a movie with</span><span class="blurb blurb_expanded"> Spider-Man 3 is the Lawrence Of Arabia of the superhero movies world. It is epic, sprawling, magnificent, meaningful, beautiful. Anyone who doesn't enjoy this movie must be a pretty spoilt brat or a cynical old misery. For near on three hours it envelops you in its world and makes you CARE about the characters. How's that for a special effects laden blockbuster, a movie with characters that matter? The comedy works, the emotion works, the action works. Everything Raimi tries comes off. The set pieces are particularly astounding, ranging from an out of control crane to Spidey's numerous battles with the meaty villains on show. Like others, I think this is by far the best of the three (though I loved the first two as well). It's a modern-day classic, an enrapturing fantasy that exhibits all that's best in modern movie making. An experience not to be missed.</span><span class="blurb_etc">…</span> <a rel="nofollow" class="toggle_expand_collapse toggle_expand" href="/movie/spider-man-3/user-reviews?page=1&amp;user_review_id=272074">Expand</a></span>
            </div>
                            </div>
                                                        <div class="review_section review_actions ">
                                <ul class="review_actions">
                                                                            <li class="review_action review_helpful">
                                            <div class="review_helpful">
    <div class="rating_thumbs">
        			<div class="helpful_summary thumb_count">
				<a href="https://secure.metacritic.com/login">
				<span class="total_ups">0</span>
				of
				<span class="total_thumbs">0</span>
				users found this helpful
                </a>
			</div>
                <div style="clear:both;"></div>
    </div>
</div>
                                        </li>
                                                                                                                                            </ul>
                            </div>
                                                    </div>
                    </div></div></div></div>
                </li>
                                                                                    <li id="user_review_272119" class="review user_review">
                    <div class="review_btm review_btm_r"><div class="review_btm review_btm_l"><div class="review_top review_top_r"><div class="review_top review_top_l">
                        <div class="review_content">
                            <div class="review_section">
                                <div class="review_stats">
                                    <div class="review_critic">
                                        <div class="name">
                                                                                            <span>LeeS.</span>
                                                                                                                                </div>
                                                                                    <div class="date">May  5, 2007</div>
                                                                            </div>

                                    <div class="review_grade">

<div class="metascore_w user medium movie positive indiv">7</div>

                                    </div>
                                </div>
                                <div class="review_body">

                                        <span class="inline_expand_collapse inline_collapsed" id="review_blurb_272119"><span class="blurb blurb_collapsed"> Deeply flawed masterpeice. I think Sam Raimi didn't have the time needed to give this movie the edit that it needed. With a better cut Raimi could easily remove the worse scenes and improve the poorer and more contrived story elements. However it will never be as good as Spider-man 2, which was pretty much perfect. There are some really great scenes and amazing action sequences, and</span><span class="blurb blurb_expanded"> Deeply flawed masterpeice. I think Sam Raimi didn't have the time needed to give this movie the edit that it needed. With a better cut Raimi could easily remove the worse scenes and improve the poorer and more contrived story elements. However it will never be as good as Spider-man 2, which was pretty much perfect. There are some really great scenes and amazing action sequences, and the stellar cast help make the movie fun despite a few bad scenes, bad pacing and forced plot elements.</span><span class="blurb_etc">…</span> <a rel="nofollow" class="toggle_expand_collapse toggle_expand" href="/movie/spider-man-3/user-reviews?page=1&amp;user_review_id=272119">Expand</a></span>
            </div>
                            </div>
                                                        <div class="review_section review_actions ">
                                <ul class="review_actions">
                                                                            <li class="review_action review_helpful">
                                            <div class="review_helpful">
    <div class="rating_thumbs">
        			<div class="helpful_summary thumb_count">
				<a href="https://secure.metacritic.com/login">
				<span class="total_ups">0</span>
				of
				<span class="total_thumbs">0</span>
				users found this helpful
                </a>
			</div>
                <div style="clear:both;"></div>
    </div>
</div>
                                        </li>
                                                                                                                                            </ul>
                            </div>
                                                    </div>
                    </div></div></div></div>
                </li>
                                                                                    <li id="user_review_272127" class="review user_review">
                    <div class="review_btm review_btm_r"><div class="review_btm review_btm_l"><div class="review_top review_top_r"><div class="review_top review_top_l">
                        <div class="review_content">
                            <div class="review_section">
                                <div class="review_stats">
                                    <div class="review_critic">
                                        <div class="name">
                                                                                            <span>MicS.</span>
                                                                                                                                </div>
                                                                                    <div class="date">May  5, 2007</div>
                                                                            </div>

                                    <div class="review_grade">

<div class="metascore_w user medium movie positive indiv">7</div>

                                    </div>
                                </div>
                                <div class="review_body">

                                        <span> It was pretty good. Not as good as 2 and 1, and somewhat of a let down only because we've seen it all before. Venom did feel a tiny bit rushed and thrown in at the end. I think it would've benefitted from just having the Sandman. Harry could've stayed. Other than that, was cool.</span>
            </div>
                            </div>
                                                        <div class="review_section review_actions ">
                                <ul class="review_actions">
                                                                            <li class="review_action review_helpful">
                                            <div class="review_helpful">
    <div class="rating_thumbs">
        			<div class="helpful_summary thumb_count">
				<a href="https://secure.metacritic.com/login">
				<span class="total_ups">0</span>
				of
				<span class="total_thumbs">0</span>
				users found this helpful
                </a>
			</div>
                <div style="clear:both;"></div>
    </div>
</div>
                                        </li>
                                                                                                                                            </ul>
                            </div>
                                                    </div>
                    </div></div></div></div>
                </li>
                                                                                    <li id="user_review_272126" class="review user_review">
                    <div class="review_btm review_btm_r"><div class="review_btm review_btm_l"><div class="review_top review_top_r"><div class="review_top review_top_l">
                        <div class="review_content">
                            <div class="review_section">
                                <div class="review_stats">
                                    <div class="review_critic">
                                        <div class="name">
                                                                                            <span>Bill</span>
                                                                                                                                </div>
                                                                                    <div class="date">May  5, 2007</div>
                                                                            </div>

                                    <div class="review_grade">

<div class="metascore_w user medium movie mixed indiv">4</div>

                                    </div>
                                </div>
                                <div class="review_body">

                                        <span> Very disappointed, although I did like the emo Peter Parker, which my friend and I got a good laugh out of.</span>
            </div>
                            </div>
                                                        <div class="review_section review_actions ">
                                <ul class="review_actions">
                                                                            <li class="review_action review_helpful">
                                            <div class="review_helpful">
    <div class="rating_thumbs">
        			<div class="helpful_summary thumb_count">
				<a href="https://secure.metacritic.com/login">
				<span class="total_ups">0</span>
				of
				<span class="total_thumbs">0</span>
				users found this helpful
                </a>
			</div>
                <div style="clear:both;"></div>
    </div>
</div>
                                        </li>
                                                                                                                                            </ul>
                            </div>
                                                    </div>
                    </div></div></div></div>
                </li>
                                                                                    <li id="user_review_272135" class="review user_review">
                    <div class="review_btm review_btm_r"><div class="review_btm review_btm_l"><div class="review_top review_top_r"><div class="review_top review_top_l">
                        <div class="review_content">
                            <div class="review_section">
                                <div class="review_stats">
                                    <div class="review_critic">
                                        <div class="name">
                                                                                            <span>SteveA.</span>
                                                                                                                                </div>
                                                                                    <div class="date">May  5, 2007</div>
                                                                            </div>

                                    <div class="review_grade">

<div class="metascore_w user medium movie positive indiv">7</div>

                                    </div>
                                </div>
                                <div class="review_body">

                                        <span> There were a few flaws. However, this movie had too much heart to dislike. I can picture Raimi not being one of the cool kids in school (that was probably someone like Michael Bay or James Cameron). Instead, he was probably the sweet, goofy kid with a ton of talent and heart.</span>
            </div>
                            </div>
                                                        <div class="review_section review_actions ">
                                <ul class="review_actions">
                                                                            <li class="review_action review_helpful">
                                            <div class="review_helpful">
    <div class="rating_thumbs">
        			<div class="helpful_summary thumb_count">
				<a href="https://secure.metacritic.com/login">
				<span class="total_ups">0</span>
				of
				<span class="total_thumbs">0</span>
				users found this helpful
                </a>
			</div>
                <div style="clear:both;"></div>
    </div>
</div>
                                        </li>
                                                                                                                                            </ul>
                            </div>
                                                    </div>
                    </div></div></div></div>
                </li>
                                                                                    <li id="user_review_272149" class="review user_review">
                    <div class="review_btm review_btm_r"><div class="review_btm review_btm_l"><div class="review_top review_top_r"><div class="review_top review_top_l">
                        <div class="review_content">
                            <div class="review_section">
                                <div class="review_stats">
                                    <div class="review_critic">
                                        <div class="name">
                                                                                            <span>Willy</span>
                                                                                                                                </div>
                                                                                    <div class="date">May  5, 2007</div>
                                                                            </div>

                                    <div class="review_grade">

<div class="metascore_w user medium movie negative indiv">3</div>

                                    </div>
                                </div>
                                <div class="review_body">

                                        <span class="inline_expand_collapse inline_collapsed" id="review_blurb_272149"><span class="blurb blurb_collapsed"> Sorry, but this movie is insulting. Is it suppose to be okay that there is no character consistency and any old damn thing can happen as long as a fancy video game demo is thrown at us every forty minutes? To name only a few... he does the upsidedown kiss with the blond girl full on the mouth in front of MJ when he's getting along great with her, the neighbor girl who had a crush on</span><span class="blurb blurb_expanded"> Sorry, but this movie is insulting. Is it suppose to be okay that there is no character consistency and any old damn thing can happen as long as a fancy video game demo is thrown at us every forty minutes? To name only a few... he does the upsidedown kiss with the blond girl full on the mouth in front of MJ when he's getting along great with her, the neighbor girl who had a crush on him is thrilled that he and MJ are getting back together, Sandman robs banks violently and brutally tries to kill him, but says he was badgered into doing it (huh?), so he's really a nice guy; of all the people on earth that walking goo could have stuck to it happened to be Spiderman. Please. Let me know when you get back to filmmaking, Sam.</span><span class="blurb_etc">…</span> <a rel="nofollow" class="toggle_expand_collapse toggle_expand" href="/movie/spider-man-3/user-reviews?page=1&amp;user_review_id=272149">Expand</a></span>
            </div>
                            </div>
                                                        <div class="review_section review_actions ">
                                <ul class="review_actions">
                                                                            <li class="review_action review_helpful">
                                            <div class="review_helpful">
    <div class="rating_thumbs">
        			<div class="helpful_summary thumb_count">
				<a href="https://secure.metacritic.com/login">
				<span class="total_ups">0</span>
				of
				<span class="total_thumbs">0</span>
				users found this helpful
                </a>
			</div>
                <div style="clear:both;"></div>
    </div>
</div>
                                        </li>
                                                                                                                                            </ul>
                            </div>
                                                    </div>
                    </div></div></div></div>
                </li>
                                                                                    <li id="user_review_272139" class="review user_review">
                    <div class="review_btm review_btm_r"><div class="review_btm review_btm_l"><div class="review_top review_top_r"><div class="review_top review_top_l">
                        <div class="review_content">
                            <div class="review_section">
                                <div class="review_stats">
                                    <div class="review_critic">
                                        <div class="name">
                                                                                            <span>TylerDrainville</span>
                                                                                                                                </div>
                                                                                    <div class="date">May  5, 2007</div>
                                                                            </div>

                                    <div class="review_grade">

<div class="metascore_w user medium movie mixed indiv">5</div>

                                    </div>
                                </div>
                                <div class="review_body">

                                        <span> By far the worst Spider-Man film yet. They did a very poor job with Spidey's dark side and most of the villains here are shallow and pulled off quite badly. There were more laughs in the movie than "wow" moments, which was not what I was expecting. Very disappointed.</span>
            </div>
                            </div>
                                                        <div class="review_section review_actions ">
                                <ul class="review_actions">
                                                                            <li class="review_action review_helpful">
                                            <div class="review_helpful">
    <div class="rating_thumbs">
        			<div class="helpful_summary thumb_count">
				<a href="https://secure.metacritic.com/login">
				<span class="total_ups">0</span>
				of
				<span class="total_thumbs">0</span>
				users found this helpful
                </a>
			</div>
                <div style="clear:both;"></div>
    </div>
</div>
                                        </li>
                                                                                                                                            </ul>
                            </div>
                                                    </div>
                    </div></div></div></div>
                </li>
                                                                                    <li id="user_review_272140" class="review user_review">
                    <div class="review_btm review_btm_r"><div class="review_btm review_btm_l"><div class="review_top review_top_r"><div class="review_top review_top_l">
                        <div class="review_content">
                            <div class="review_section">
                                <div class="review_stats">
                                    <div class="review_critic">
                                        <div class="name">
                                                                                            <span>Beau</span>
                                                                                                                                </div>
                                                                                    <div class="date">May  5, 2007</div>
                                                                            </div>

                                    <div class="review_grade">

<div class="metascore_w user medium movie negative indiv">2</div>

                                    </div>
                                </div>
                                <div class="review_body">

                                        <span> There is a good movie that could have been made of Spider-Man vs Venom, New Goblin or Sandman, but putting all of them together in the same film means that each of them gets the barest of characterization and the action sequences become a mess. Kirsten Dunst has little to do but be mistreated throughout the film. Tobey Maguire is simply not believable as a bad boy. Skip this film.</span>
            </div>
                            </div>
                                                        <div class="review_section review_actions ">
                                <ul class="review_actions">
                                                                            <li class="review_action review_helpful">
                                            <div class="review_helpful">
    <div class="rating_thumbs">
        			<div class="helpful_summary thumb_count">
				<a href="https://secure.metacritic.com/login">
				<span class="total_ups">0</span>
				of
				<span class="total_thumbs">0</span>
				users found this helpful
                </a>
			</div>
                <div style="clear:both;"></div>
    </div>
</div>
                                        </li>
                                                                                                                                            </ul>
                            </div>
                                                    </div>
                    </div></div></div></div>
                </li>
                                                                                    <li id="user_review_272082" class="review user_review">
                    <div class="review_btm review_btm_r"><div class="review_btm review_btm_l"><div class="review_top review_top_r"><div class="review_top review_top_l">
                        <div class="review_content">
                            <div class="review_section">
                                <div class="review_stats">
                                    <div class="review_critic">
                                        <div class="name">
                                                                                            <span>TaylorP.</span>
                                                                                                                                </div>
                                                                                    <div class="date">May  5, 2007</div>
                                                                            </div>

                                    <div class="review_grade">

<div class="metascore_w user medium movie negative indiv">2</div>

                                    </div>
                                </div>
                                <div class="review_body">

                                        <span class="inline_expand_collapse inline_collapsed" id="review_blurb_272082"><span class="blurb blurb_collapsed"> Quite possibly one of the worst movies of the year- and I enjoyed the first two (more the first one). I simply thought that this film is a product of too much money, and too much greed for more money. The characters are shallow, especially in my mind Flint Marko one who is characterized as relatively bad throughout the film only to drastically change in the last ten minutes of the film</span><span class="blurb blurb_expanded"> Quite possibly one of the worst movies of the year- and I enjoyed the first two (more the first one). I simply thought that this film is a product of too much money, and too much greed for more money. The characters are shallow, especially in my mind Flint Marko one who is characterized as relatively bad throughout the film only to drastically change in the last ten minutes of the film with no warning. In addition to this some of the "dramatic" fight scenes were simply laughable. Overall very disappointing movie, and yes, I would like my money back.</span><span class="blurb_etc">…</span> <a rel="nofollow" class="toggle_expand_collapse toggle_expand" href="/movie/spider-man-3/user-reviews?page=1&amp;user_review_id=272082">Expand</a></span>
            </div>
                            </div>
                                                        <div class="review_section review_actions ">
                                <ul class="review_actions">
                                                                            <li class="review_action review_helpful">
                                            <div class="review_helpful">
    <div class="rating_thumbs">
        			<div class="helpful_summary thumb_count">
				<a href="https://secure.metacritic.com/login">
				<span class="total_ups">0</span>
				of
				<span class="total_thumbs">0</span>
				users found this helpful
                </a>
			</div>
                <div style="clear:both;"></div>
    </div>
</div>
                                        </li>
                                                                                                                                            </ul>
                            </div>
                                                    </div>
                    </div></div></div></div>
                </li>
                                                                                    <li id="user_review_272087" class="review user_review">
                    <div class="review_btm review_btm_r"><div class="review_btm review_btm_l"><div class="review_top review_top_r"><div class="review_top review_top_l">
                        <div class="review_content">
                            <div class="review_section">
                                <div class="review_stats">
                                    <div class="review_critic">
                                        <div class="name">
                                                                                            <span>ChesterJ&gt;</span>
                                                                                                                                </div>
                                                                                    <div class="date">May  5, 2007</div>
                                                                            </div>

                                    <div class="review_grade">

<div class="metascore_w user medium movie positive indiv">9</div>

                                    </div>
                                </div>
                                <div class="review_body">

                                        <span> The special effects are top-notch, absolutely, but it's the amazing camera works and the beautifully interwoven story that gives Spider-Man 3 it's infallible greatness.</span>
            </div>
                            </div>
                                                        <div class="review_section review_actions ">
                                <ul class="review_actions">
                                                                            <li class="review_action review_helpful">
                                            <div class="review_helpful">
    <div class="rating_thumbs">
        			<div class="helpful_summary thumb_count">
				<a href="https://secure.metacritic.com/login">
				<span class="total_ups">0</span>
				of
				<span class="total_thumbs">0</span>
				users found this helpful
                </a>
			</div>
                <div style="clear:both;"></div>
    </div>
</div>
                                        </li>
                                                                                                                                            </ul>
                            </div>
                                                    </div>
                    </div></div></div></div>
                </li>
                                                                                    <li id="user_review_272088" class="review user_review">
                    <div class="review_btm review_btm_r"><div class="review_btm review_btm_l"><div class="review_top review_top_r"><div class="review_top review_top_l">
                        <div class="review_content">
                            <div class="review_section">
                                <div class="review_stats">
                                    <div class="review_critic">
                                        <div class="name">
                                                                                            <span>HalB.</span>
                                                                                                                                </div>
                                                                                    <div class="date">May  5, 2007</div>
                                                                            </div>

                                    <div class="review_grade">

<div class="metascore_w user medium movie positive indiv">7</div>

                                    </div>
                                </div>
                                <div class="review_body">

                                        <span class="inline_expand_collapse inline_collapsed" id="review_blurb_272088"><span class="blurb blurb_collapsed"> More fun than I thought it would be. Yes, it focuses more on emotion than action at times, but what's wrong with that? There are a couple scenes that fall flat, but the overall story arc moves along nicely, the special effects are good (but don't dominate the film) and the acting is decent. People who give this anything below a 5 are way harsh. The cameo by Bruce Campbell is</span><span class="blurb blurb_expanded"> More fun than I thought it would be. Yes, it focuses more on emotion than action at times, but what's wrong with that? There are a couple scenes that fall flat, but the overall story arc moves along nicely, the special effects are good (but don't dominate the film) and the acting is decent. People who give this anything below a 5 are way harsh. The cameo by Bruce Campbell is excellent. And who knew that Dunst cold actually sing? or that Toby could dance a bit?</span><span class="blurb_etc">…</span> <a rel="nofollow" class="toggle_expand_collapse toggle_expand" href="/movie/spider-man-3/user-reviews?page=1&amp;user_review_id=272088">Expand</a></span>
            </div>
                            </div>
                                                        <div class="review_section review_actions ">
                                <ul class="review_actions">
                                                                            <li class="review_action review_helpful">
                                            <div class="review_helpful">
    <div class="rating_thumbs">
        			<div class="helpful_summary thumb_count">
				<a href="https://secure.metacritic.com/login">
				<span class="total_ups">0</span>
				of
				<span class="total_thumbs">0</span>
				users found this helpful
                </a>
			</div>
                <div style="clear:both;"></div>
    </div>
</div>
                                        </li>
                                                                                                                                            </ul>
                            </div>
                                                    </div>
                    </div></div></div></div>
                </li>
                                                                                    <li id="user_review_272089" class="review user_review">
                    <div class="review_btm review_btm_r"><div class="review_btm review_btm_l"><div class="review_top review_top_r"><div class="review_top review_top_l">
                        <div class="review_content">
                            <div class="review_section">
                                <div class="review_stats">
                                    <div class="review_critic">
                                        <div class="name">
                                                                                            <span>JoeAverage</span>
                                                                                                                                </div>
                                                                                    <div class="date">May  5, 2007</div>
                                                                            </div>

                                    <div class="review_grade">

<div class="metascore_w user medium movie mixed indiv">4</div>

                                    </div>
                                </div>
                                <div class="review_body">

                                        <span> ...Nice to see Topher Grace find some work...er, yeah...</span>
            </div>
                            </div>
                                                        <div class="review_section review_actions ">
                                <ul class="review_actions">
                                                                            <li class="review_action review_helpful">
                                            <div class="review_helpful">
    <div class="rating_thumbs">
        			<div class="helpful_summary thumb_count">
				<a href="https://secure.metacritic.com/login">
				<span class="total_ups">0</span>
				of
				<span class="total_thumbs">0</span>
				users found this helpful
                </a>
			</div>
                <div style="clear:both;"></div>
    </div>
</div>
                                        </li>
                                                                                                                                            </ul>
                            </div>
                                                    </div>
                    </div></div></div></div>
                </li>
                                                                                    <li id="user_review_272091" class="review user_review">
                    <div class="review_btm review_btm_r"><div class="review_btm review_btm_l"><div class="review_top review_top_r"><div class="review_top review_top_l">
                        <div class="review_content">
                            <div class="review_section">
                                <div class="review_stats">
                                    <div class="review_critic">
                                        <div class="name">
                                                                                            <span>Brian</span>
                                                                                                                                </div>
                                                                                    <div class="date">May  5, 2007</div>
                                                                            </div>

                                    <div class="review_grade">

<div class="metascore_w user medium movie negative indiv">1</div>

                                    </div>
                                </div>
                                <div class="review_body">

                                        <span> Quite simply, the most boring movie I really wanted to like. Topher Grace is a Horrible !!!! Edie Brock and an even worse Venom. Venom being my favorite Marvel character I refuse to watch this Abomination ever again if I can help it. This is such a disappointment and too long!</span>
            </div>
                            </div>
                                                        <div class="review_section review_actions ">
                                <ul class="review_actions">
                                                                            <li class="review_action review_helpful">
                                            <div class="review_helpful">
    <div class="rating_thumbs">
        			<div class="helpful_summary thumb_count">
				<a href="https://secure.metacritic.com/login">
				<span class="total_ups">0</span>
				of
				<span class="total_thumbs">0</span>
				users found this helpful
                </a>
			</div>
                <div style="clear:both;"></div>
    </div>
</div>
                                        </li>
                                                                                                                                            </ul>
                            </div>
                                                    </div>
                    </div></div></div></div>
                </li>
                                                                                    <li id="user_review_272093" class="review user_review last_review">
                    <div class="review_btm review_btm_r"><div class="review_btm review_btm_l"><div class="review_top review_top_r"><div class="review_top review_top_l">
                        <div class="review_content">
                            <div class="review_section">
                                <div class="review_stats">
                                    <div class="review_critic">
                                        <div class="name">
                                                                                            <span>AndrewC</span>
                                                                                                                                </div>
                                                                                    <div class="date">May  5, 2007</div>
                                                                            </div>

                                    <div class="review_grade">

<div class="metascore_w user medium movie positive indiv">9</div>

                                    </div>
                                </div>
                                <div class="review_body">

                                        <span class="inline_expand_collapse inline_collapsed" id="review_blurb_272093"><span class="blurb blurb_collapsed"> This Movie in my opinion is the best of the trilogy, It has new exciting villians which overpower the villians of the last two installments. There are however a few moments in the movie where you wonder why Raimi twists the story. Other than that, Spider Man gives off a new personality that pleased me throughout the movie. Overall, Spider Man 3 keeps you on the edge of your seat wanting</span><span class="blurb blurb_expanded"> This Movie in my opinion is the best of the trilogy, It has new exciting villians which overpower the villians of the last two installments. There are however a few moments in the movie where you wonder why Raimi twists the story. Other than that, Spider Man gives off a new personality that pleased me throughout the movie. Overall, Spider Man 3 keeps you on the edge of your seat wanting more from the from the screen, and hopefuly, more installments of the series from Sam Raimi.</span><span class="blurb_etc">…</span> <a rel="nofollow" class="toggle_expand_collapse toggle_expand" href="/movie/spider-man-3/user-reviews?page=1&amp;user_review_id=272093">Expand</a></span>
            </div>
                            </div>
                                                        <div class="review_section review_actions ">
                                <ul class="review_actions">
                                                                            <li class="review_action review_helpful">
                                            <div class="review_helpful">
    <div class="rating_thumbs">
        			<div class="helpful_summary thumb_count">
				<a href="https://secure.metacritic.com/login">
				<span class="total_ups">0</span>
				of
				<span class="total_thumbs">0</span>
				users found this helpful
                </a>
			</div>
                <div style="clear:both;"></div>
    </div>
</div>
                                        </li>
                                                                                                                                            </ul>
                            </div>
                                                    </div>
                    </div></div></div></div>
                </li>
                                            </ol>
                                                                    <div class="page_nav">
    <div class="page_nav_wrap">
        <div class="page_flipper">
                            <span class="flipper prev"><a class="action" rel="prev" href="/movie/spider-man-3/user-reviews?page=0"><span class="text">prev</span></a></span>
                                        <span class="flipper next"><a class="action" rel="next" href="/movie/spider-man-3/user-reviews?page=2"><span class="text">next</span></a></span>
                    </div>
        <div class="pages">
            <div class="label">Page:</div>
            <ul class="pages"><li class="page first_page"><a class="page_num" href="/movie/spider-man-3/user-reviews?page=0">1</a></li><li class="page active_page"><span class="page_num">2</span></li><li class="page"><a class="page_num" href="/movie/spider-man-3/user-reviews?page=2">3</a></li><li class="page"><a class="page_num" href="/movie/spider-man-3/user-reviews?page=3">4</a></li><li class="page last_page"><a class="page_num" href="/movie/spider-man-3/user-reviews?page=4">5</a></li></ul>
        </div>
    </div>
</div>
                        </div>
    </div>
</div>








        <div id="taboola-below-content-thumbnails" class=" trc_related_container trc_spotlight_widget trc_elastic trc_elastic_trc_83096 "><div class="trc_rbox_container" style="display: block;"><div><div id="trc_wrapper_83096" class="trc_rbox ab_alternating-thumbnails-a_abp-mode trc-content-sponsored " style="overflow: hidden; display: block;"><div id="trc_header_83096" class="trc_rbox_header trc_rbox_border_elm"><div class="trc_header_ext"><div class="logoDiv link-adc "><a class="trc_desktop_adc_link trc_attribution_position_top" rel="nofollow" href="http://popup.taboola.com/en/?template=colorbox&amp;taboola_utm_source=cbsinteractive-metacritic&amp;taboola_utm_medium=bytaboola&amp;taboola_utm_content=ab_alternating-thumbnails-a_abp-mode:desktop user_reviews Below Content Thumbnails:" target="_blank"><span class="trc_adc_wrapper"><span class="trc_adc_s_logo"></span>&nbsp;</span><span class="trc_logos_v_align">&nbsp;</span></a><a class="trc_mobile_adc_link trc_attribution_position_top" rel="nofollow" href="http://popup.taboola.com/en/?template=colorbox&amp;taboola_utm_source=cbsinteractive-metacritic&amp;taboola_utm_medium=bytaboola&amp;taboola_utm_content=ab_alternating-thumbnails-a_abp-mode:desktop user_reviews Below Content Thumbnails:" target="_blank"><span class="trc_adc_wrapper"><span class="trc_adc_s_logo"></span>&nbsp;</span><span class="trc_logos_v_align">&nbsp;</span></a></div><div class="logoDiv link-attribution "><a class="trc_desktop_attribution_link trc_attribution_position_top" rel="nofollow" href="http://popup.taboola.com/en/?template=colorbox&amp;taboola_utm_source=cbsinteractive-metacritic&amp;taboola_utm_medium=bytaboola&amp;taboola_utm_content=ab_alternating-thumbnails-a_abp-mode:desktop user_reviews Below Content Thumbnails:" target="_blank"><span>by Taboola</span><span class="trc_logos_v_align">&nbsp;</span></a><a class="trc_mobile_attribution_link trc_attribution_position_top" rel="nofollow" href="http://popup.taboola.com/en/?template=colorbox&amp;taboola_utm_source=cbsinteractive-metacritic&amp;taboola_utm_medium=bytaboola&amp;taboola_utm_content=ab_alternating-thumbnails-a_abp-mode:desktop user_reviews Below Content Thumbnails:" target="_blank"><span>by Taboola</span><span class="trc_logos_v_align">&nbsp;</span></a></div><div class="logoDiv link-disclosure  attribution-disclosure-link-sponsored"><a class="trc_desktop_disclosure_link trc_attribution_position_top" rel="nofollow" href="http://popup.taboola.com/en/?template=colorbox&amp;taboola_utm_source=cbsinteractive-metacritic&amp;taboola_utm_medium=bytaboola&amp;taboola_utm_content=ab_alternating-thumbnails-a_abp-mode:desktop user_reviews Below Content Thumbnails:" target="_blank"><span>Sponsored Links</span><span class="trc_logos_v_align">&nbsp;</span></a><a class="trc_mobile_disclosure_link trc_attribution_position_top" rel="nofollow" href="http://popup.taboola.com/en/?template=colorbox&amp;taboola_utm_source=cbsinteractive-metacritic&amp;taboola_utm_medium=bytaboola&amp;taboola_utm_content=ab_alternating-thumbnails-a_abp-mode:desktop user_reviews Below Content Thumbnails:" target="_blank"><span>Sponsored Links</span><span class="trc_logos_v_align">&nbsp;</span></a></div><div class="logoDiv link-disclosure  attribution-disclosure-link-hybrid"><a class="trc_desktop_disclosure_link trc_attribution_position_top" rel="nofollow" href="http://popup.taboola.com/en/?template=colorbox&amp;taboola_utm_source=cbsinteractive-metacritic&amp;taboola_utm_medium=bytaboola&amp;taboola_utm_content=ab_alternating-thumbnails-a_abp-mode:desktop user_reviews Below Content Thumbnails:" target="_blank"><span>Promoted Links</span><span class="trc_logos_v_align">&nbsp;</span></a><a class="trc_mobile_disclosure_link trc_attribution_position_top" rel="nofollow" href="http://popup.taboola.com/en/?template=colorbox&amp;taboola_utm_source=cbsinteractive-metacritic&amp;taboola_utm_medium=bytaboola&amp;taboola_utm_content=ab_alternating-thumbnails-a_abp-mode:desktop user_reviews Below Content Thumbnails:" target="_blank"><span>Promoted Links</span><span class="trc_logos_v_align">&nbsp;</span></a></div></div><span class="trc_rbox_header_span">From The Web</span></div><div id="outer_83096" class="trc_rbox_outer"><div id="rbox-o2m" class="trc_rbox_div trc_rbox_border_elm"><div id="internal_trc_83096"><div data-item-id="~~V1~~3523664523704351989~~ZpbVe6W9qCaTM85gTQ4zGQ1mRNi-6uOq-mUipAV2orqroxI4gj4mYltvAHkrZTd8DdeU8ba3ruU7lSYoOY4RpQ" data-item-title="“Shark Tank” Star’s Brilliant Advice For Paying Off Your Mortgage" data-item-thumb="https://console.brax-cdn.com/creatives/d788f8ea-3b8c-429b-b9db-a6aa697387c6/barbwhite_d571ba39e4032492ef637e18cbde5469.jpg" data-item-syndicated="true" class="videoCube trc_spotlight_item origin-default thumbnail_top syndicatedItem textItem videoCube_1_child trc-first-recommendation trc-spotlight-first-recommendation  trc_excludable "><a title="“Shark Tank” Star’s Brilliant Advice For Paying Off Your Mortgage" href="https://www.onesmartpenny.com/landers/pages/mortgage-refinance-shark-4.html?utm_term=barbwhite.jpg_1ecd9e_061316&amp;utm_source=taboola&amp;utm_adgroup=OSP_BC_IMG_RONxMSN_Desktop&amp;utm_medium=cbsinteractive-metacritic" rel="nofollow" target="_blank" class=" item-thumbnail-href "><div class="thumbBlock_holder"><span class="thumbBlock" style="background-image: url(&quot;http://images.taboola.com/taboola/image/fetch/f_jpg%2Cq_80%2Ch_145%2Cw_203%2Cc_fill%2Cg_faces%2Ce_sharpen/https%3A//console.brax-cdn.com/creatives/d788f8ea-3b8c-429b-b9db-a6aa697387c6/barbwhite_d571ba39e4032492ef637e18cbde5469.jpg&quot;);"><span class="thumbnail-overlay"></span><span class="branding">The Easy Loan Site</span><span class="static-text top-right"></span></span><div class="videoCube_aspect"></div></div></a><a title="“Shark Tank” Star’s Brilliant Advice For Paying Off Your Mortgage" href="https://www.onesmartpenny.com/landers/pages/mortgage-refinance-shark-4.html?utm_term=barbwhite.jpg_1ecd9e_061316&amp;utm_source=taboola&amp;utm_adgroup=OSP_BC_IMG_RONxMSN_Desktop&amp;utm_medium=cbsinteractive-metacritic" rel="nofollow" target="_blank" class=" item-label-href "><span class="video-label-box"><span class="video-label video-title trc_ellipsis " style="-webkit-line-clamp: 2;">“Shark Tank” Star’s Brilliant Advice For Paying Off Your Mortgage</span><span class="branding">The Easy Loan Site</span></span></a><div class=" trc_user_exclude_btn " title="Remove this item"></div><div class=" trc_exclude_overlay trc_fade "></div><div class=" trc_undo_btn ">Undo</div></div><div data-item-id="~~V1~~-4082193693269660077~~jdgxVNRz2M4WEPhjV2BJ_5cP646jYXmr5TNqtyO4Cy7ncqLhrdnGGMFmoKiIRgNLDdeU8ba3ruU7lSYoOY4RpQ" data-item-title="Sparta: The Strategy Game Phenomenon of 2016" data-item-thumb="https://console.brax-cdn.com/creatives/041ca465-399e-4bcf-9b7d-edb6b5c8d972/2a8aa835-11de-4cd2-951e-77b4cbc110e3.png" data-item-syndicated="true" class="videoCube trc_spotlight_item origin-default thumbnail_top syndicatedItem textItem videoCube_2_child trc_excludable "><a title="Sparta: The Strategy Game Phenomenon of 2016" href="http://plarium.com/play/en/sparta/017_armies_hybrid_anim_g?plid=83497&amp;pxl=taboola_fr&amp;utm_content=abd0007&amp;publisherID=cbsinteractive-metacritic" rel="nofollow" target="_blank" class=" item-thumbnail-href "><div class="thumbBlock_holder"><span class="thumbBlock" style="background-image: url(&quot;http://images.taboola.com/taboola/image/fetch/f_jpg%2Cq_80%2Ch_145%2Cw_203%2Cc_fill%2Cg_faces%2Ce_sharpen/https%3A//console.brax-cdn.com/creatives/041ca465-399e-4bcf-9b7d-edb6b5c8d972/2a8aa835-11de-4cd2-951e-77b4cbc110e3.png&quot;);"><span class="thumbnail-overlay"></span><span class="branding">Sparta - Free Online Game</span><span class="static-text top-right"></span></span><div class="videoCube_aspect"></div></div></a><a title="Sparta: The Strategy Game Phenomenon of 2016" href="http://plarium.com/play/en/sparta/017_armies_hybrid_anim_g?plid=83497&amp;pxl=taboola_fr&amp;utm_content=abd0007&amp;publisherID=cbsinteractive-metacritic" rel="nofollow" target="_blank" class=" item-label-href "><span class="video-label-box"><span class="video-label video-title trc_ellipsis " style="-webkit-line-clamp: 2;">Sparta: The Strategy Game Phenomenon of 2016</span><span class="branding">Sparta - Free Online Game</span></span></a><div class=" trc_user_exclude_btn " title="Remove this item"></div><div class=" trc_exclude_overlay trc_fade "></div><div class=" trc_undo_btn ">Undo</div></div><div data-item-id="~~V1~~-2475962748955690044~~m3hHddpGqzUZHsLUiHOcyJRo1UsfHf0-1O2i3xKxtb7-lYxK6Q0-ymztisPntpsvDdeU8ba3ruU7lSYoOY4RpQ" data-item-title="The Most Exciting MMORPG You&amp;#39;ve Ever Played! Don&amp;#39;t Miss This!" data-item-thumb="https://console.brax-cdn.com/creatives/041ca465-399e-4bcf-9b7d-edb6b5c8d972/c54967264baa0e0dff0525d1dda0783c_3743eb0c102ac285c8edc8fcfef29f9c.png" data-item-syndicated="true" class="videoCube trc_spotlight_item origin-default thumbnail_top syndicatedItem textItem videoCube_3_child trc_excludable "><a title="The Most Exciting MMORPG You've Ever Played! Don't Miss This!" href="http://plarium.com/play/en/stormfall/004_dragon_hybrid_anim?plid=85190&amp;pxl=taboola_fr&amp;&amp;publisherID=cbsinteractive-metacritic" rel="nofollow" target="_blank" class=" item-thumbnail-href "><div class="thumbBlock_holder"><span class="thumbBlock" style="background-image: url(&quot;http://images.taboola.com/taboola/image/fetch/f_jpg%2Cq_80%2Ch_145%2Cw_203%2Cc_fill%2Cg_faces%2Ce_sharpen/https%3A//console.brax-cdn.com/creatives/041ca465-399e-4bcf-9b7d-edb6b5c8d972/c54967264baa0e0dff0525d1dda0783c_3743eb0c102ac285c8edc8fcfef29f9c.png&quot;);"><span class="thumbnail-overlay"></span><span class="branding">Stormfall: Free Online Game</span><span class="static-text top-right"></span></span><div class="videoCube_aspect"></div></div></a><a title="The Most Exciting MMORPG You've Ever Played! Don't Miss This!" href="http://plarium.com/play/en/stormfall/004_dragon_hybrid_anim?plid=85190&amp;pxl=taboola_fr&amp;&amp;publisherID=cbsinteractive-metacritic" rel="nofollow" target="_blank" class=" item-label-href "><span class="video-label-box"><span class="video-label video-title trc_ellipsis " style="-webkit-line-clamp: 2;">The Most Exciting MMORPG You've Ever Played! Don't Miss This!</span><span class="branding">Stormfall: Free Online Game</span></span></a><div class=" trc_user_exclude_btn " title="Remove this item"></div><div class=" trc_exclude_overlay trc_fade "></div><div class=" trc_undo_btn ">Undo</div></div><div data-item-id="~~V1~~-7778055205621534399~~jw--fJuG7vhZxdC6zHYS9Kg1WJ_KeLT2Keli_siwgoDPRrc-3twzVX224nkWIeszDdeU8ba3ruU7lSYoOY4RpQ" data-item-title="I’m a Woman Who Joined Dollar Shave Club. Here’s What Happened..." data-item-thumb="http://cdn.taboolasyndication.com/libtrc/static/thumbnails/33ec4a5a4d82cd1dba275ca8327a37d3.png" data-item-syndicated="true" class="videoCube trc_spotlight_item origin-default thumbnail_top syndicatedItem textItem videoCube_4_child trc_excludable "><a title="I’m a Woman Who Joined Dollar Shave Club. Here’s What Happened..." href="http://try.dollarshaveclub.com/tab-desk-lifehack/?utm_medium=nat&amp;utm_source=tabo&amp;utm_campaign=femalelifehack-desktop&amp;utm_content=femalelifehack-desktop&amp;utm_term=I%E2%80%99m+a+Woman+Who+Joined+Dollar+Shave+Club.+Here%E2%80%99s+What+Happened..." rel="nofollow" target="_blank" class=" item-thumbnail-href "><div class="thumbBlock_holder"><span class="thumbBlock" style="background-image: url(&quot;http://images.taboola.com/taboola/image/fetch/f_jpg%2Cq_80%2Ch_145%2Cw_203%2Cc_fill%2Cg_faces%2Ce_sharpen/http%3A//cdn.taboolasyndication.com/libtrc/static/thumbnails/33ec4a5a4d82cd1dba275ca8327a37d3.png&quot;);"><span class="thumbnail-overlay"></span><span class="branding">Dollar Shave Club</span><span class="static-text top-right"></span></span><div class="videoCube_aspect"></div></div></a><a title="I’m a Woman Who Joined Dollar Shave Club. Here’s What Happened..." href="http://try.dollarshaveclub.com/tab-desk-lifehack/?utm_medium=nat&amp;utm_source=tabo&amp;utm_campaign=femalelifehack-desktop&amp;utm_content=femalelifehack-desktop&amp;utm_term=I%E2%80%99m+a+Woman+Who+Joined+Dollar+Shave+Club.+Here%E2%80%99s+What+Happened..." rel="nofollow" target="_blank" class=" item-label-href "><span class="video-label-box"><span class="video-label video-title">I’m a Woman Who Joined Dollar Shave Club. Here’s What Happened...</span><span class="branding">Dollar Shave Club</span></span></a><div class=" trc_user_exclude_btn " title="Remove this item"></div><div class=" trc_exclude_overlay trc_fade "></div><div class=" trc_undo_btn ">Undo</div></div><div data-item-id="~~V1~~-5558615715055156430~~QcTc8uen571xe6I9_3lhVAgIrTpT6rY3xu-NfoPw2LfnlCt6P0Yrtl47DRNO5TKYDdeU8ba3ruU7lSYoOY4RpQ" data-item-title="1 in 3 Pets Will Get Lost. Keep Yours Safe With This Device" data-item-thumb="http://dx4ncraaox0l3.cloudfront.net/whistle20/wagg-thumbnail.jpg" data-item-syndicated="true" class="videoCube trc_spotlight_item origin-default thumbnail_top syndicatedItem textItem videoCube_5_child trc_excludable "><a title="1 in 3 Pets Will Get Lost. Keep Yours Safe With This Device" href="http://www.whistle.com/?utm_source=taboola&amp;utm_medium=referral" rel="nofollow" target="_blank" class=" item-thumbnail-href "><div class="thumbBlock_holder"><span class="thumbBlock" style="background-image: url(&quot;http://images.taboola.com/taboola/image/fetch/f_jpg%2Cq_80%2Ch_145%2Cw_203%2Cc_fill%2Cg_faces%2Ce_sharpen/http%3A//dx4ncraaox0l3.cloudfront.net/whistle20/wagg-thumbnail.jpg&quot;);"><span class="thumbnail-overlay"></span><span class="branding">Whistle</span><span class="static-text top-right"></span></span><div class="videoCube_aspect"></div></div></a><a title="1 in 3 Pets Will Get Lost. Keep Yours Safe With This Device" href="http://www.whistle.com/?utm_source=taboola&amp;utm_medium=referral" rel="nofollow" target="_blank" class=" item-label-href "><span class="video-label-box"><span class="video-label video-title">1 in 3 Pets Will Get Lost. Keep Yours Safe With This Device</span><span class="branding">Whistle</span></span></a><div class=" trc_user_exclude_btn " title="Remove this item"></div><div class=" trc_exclude_overlay trc_fade "></div><div class=" trc_undo_btn ">Undo</div></div><div data-item-id="~~V1~~-8037926977397850505~~aPSn5BEVxLFPAKHq1kiFW024_cCh-zl-C3OzNwjQFx4KmXK3Gj4qu0G0HfPmc5fQDdeU8ba3ruU7lSYoOY4RpQ" data-item-title="Your 401(k) Isn&amp;#39;t Growing as Fast as It Should - Here&amp;#39;s Why" data-item-thumb="http://cdn.taboolasyndication.com/libtrc/static/thumbnails/3823fda16a61675b8b9599ac15ce360e.jpg" data-item-syndicated="true" class="videoCube trc_spotlight_item origin-default thumbnail_top syndicatedItem textItem videoCube_6_child trc_excludable "><a title="Your 401(k) Isn't Growing as Fast as It Should - Here's Why" href="http://ad.doubleclick.net/ddm/trackclk/N9515.1006845TABOOLA.COM/B8198435.111659378;dc_trk_aid=283445858;dc_trk_cid=58834128" rel="nofollow" target="_blank" class=" item-thumbnail-href "><div class="thumbBlock_holder"><span class="thumbBlock" style="background-image: url(&quot;http://images.taboola.com/taboola/image/fetch/f_jpg%2Cq_80%2Ch_145%2Cw_203%2Cc_fill%2Cg_faces%2Ce_sharpen/http%3A//cdn.taboolasyndication.com/libtrc/static/thumbnails/3823fda16a61675b8b9599ac15ce360e.jpg&quot;);"><span class="thumbnail-overlay"></span><span class="branding">Mint | Future Advisor</span><span class="static-text top-right"></span></span><div class="videoCube_aspect"></div></div></a><a title="Your 401(k) Isn't Growing as Fast as It Should - Here's Why" href="http://ad.doubleclick.net/ddm/trackclk/N9515.1006845TABOOLA.COM/B8198435.111659378;dc_trk_aid=283445858;dc_trk_cid=58834128" rel="nofollow" target="_blank" class=" item-label-href "><span class="video-label-box"><span class="video-label video-title">Your 401(k) Isn't Growing as Fast as It Should - Here's Why</span><span class="branding">Mint | Future Advisor</span></span></a><div class=" trc_user_exclude_btn " title="Remove this item"></div><div class=" trc_exclude_overlay trc_fade "></div><div class=" trc_undo_btn ">Undo</div></div></div></div></div><div class="trc_clearer"></div></div></div></div></div>

        <script type="text/javascript">
            var placement = 'desktop user_reviews Below Content Thumbnails';
            window.metac_tContentWidget.push(placement);
            window._taboola = window._taboola || [];
                _taboola.push({
                mode: 'alternating-thumbnails-a',
                container: 'taboola-below-content-thumbnails',
                placement: placement,
                target_type: 'mix'
            });
        </script>








                            </div>
                            <div id="side" class="col side_col">

        <div id="mpu_plus_top" class="ad_unit">

                            <script type="text/javascript">

                        googletag.cmd.push(function() {

                                                            window.metac_g_ad_mpu_plus_top = googletag.defineSlot("/8264/aw-metacritic/movies",[[300,250],[300,600]], "mpu_plus_top").addService(googletag.pubads()).setTargeting("pos", "top");


                        });


                        window.metac_ads_pushdisplay.push("mpu_plus_top");
                                    </script>
                            <div id="google_ads_iframe_/8264/aw-metacritic/movies_2__container__" style="border: 0pt none;"><iframe id="google_ads_iframe_/8264/aw-metacritic/movies_2" title="3rd party ad content" name="google_ads_iframe_/8264/aw-metacritic/movies_2" width="300" height="250" scrolling="no" marginwidth="0" marginheight="0" frameborder="0" src="javascript:&quot;<html><body style='background:transparent'></body></html>&quot;" style="border: 0px; vertical-align: bottom;"></iframe></div></div>




<div class="module list_rankings contain_module">
    <div class="head head_type_1"><div class="head_wrap"><h2 class="module_title">Awards &amp; Rankings</h2></div></div>
    <div class="body">
        <table class="rankings">







                <tbody><tr>
                    <td class="ranking_icon">
                                                    <a href="/browse/movies/score/metascore/discussed/filtered?sort=desc&amp;year_selected=2007">
                                                <i class="fa fa-trophy"></i>
                                                    </a>
                                            </td>
                    <td class="ranking_wrap">
                        <div class="ranking_title">

                                                                                        <a href="/browse/movies/score/metascore/discussed/filtered?sort=desc&amp;year_selected=2007">#5 Most Discussed Movie of 2007</a>


                                                    </div>
                    </td>
                </tr>







                <tr>
                    <td class="ranking_icon">
                                                    <a href="/browse/movies/score/metascore/shared/filtered?sort=desc&amp;year_selected=2007">
                                                <i class="fa fa-trophy"></i>
                                                    </a>
                                            </td>
                    <td class="ranking_wrap">
                        <div class="ranking_title">

                                                                                        <a href="/browse/movies/score/metascore/shared/filtered?sort=desc&amp;year_selected=2007">#2 Most Shared Movie of 2007</a>


                                                    </div>
                    </td>
                </tr>
                 </tbody></table>
    </div>
</div>


    <div class="module supplements_module" id="supplementary-nav">
    <div class="head head_type_1"><div class="head_wrap"><h2 class="module_title">Essential Links</h2></div></div>
    <div class="body">
        <div class="body_wrap">
                        <div id="supplementary-items" class="supplements supplement_links">
                <ol class="supplements supplement_links">
                                                                                                    <li class="supplement supplement_link">
                                <a class="section dw_tag {'tag':'supplementary-nav;item;1'}" href="http://www.metacritic.com/browse/movies/release-date/theaters/date">New Releases in Theaters</a>
                            </li>
                                                                                                                            <li class="supplement supplement_link">
                                <a class="section dw_tag {'tag':'supplementary-nav;item;2'}" href="http://www.metacritic.com/browse/movies/release-date/coming-soon/date?view=condensed">Coming Soon to Theaters</a>
                            </li>
                                                                                                                            <li class="supplement supplement_link">
                                <a class="section dw_tag {'tag':'supplementary-nav;item;3'}" href="http://www.metacritic.com/feature/now-streaming-on-amazon-instant-video">New on Amazon Instant Video</a>
                            </li>
                                                                                                                            <li class="supplement supplement_link">
                                <a class="section dw_tag {'tag':'supplementary-nav;item;4'}" href="http://www.metacritic.com/feature/now-streaming-on-netflix">New on Netflix</a>
                            </li>
                                                                                                                            <li class="supplement supplement_link">
                                <a class="section dw_tag {'tag':'supplementary-nav;item;5'}" href="http://www.metacritic.com/browse/dvds/release-date/new-releases/date">New on DVD/Blu-ray</a>
                            </li>
                                                                                                                            <li class="supplement supplement_link">
                                <a class="section dw_tag {'tag':'supplementary-nav;item;6'}" href="http://www.metacritic.com/feature/dvd-blu-ray-release-calendar-july-2016">Coming Soon to DVD/Blu-ray</a>
                            </li>
                                                                                                                            <li class="supplement supplement_link">
                                <a class="section dw_tag {'tag':'supplementary-nav;item;7'}" href="http://www.metacritic.com/browse/movies/score/metascore/all?sort=desc ">All-Time High Scores </a>
                            </li>
                                                                                                                            <li class="supplement supplement_link">
                                <a class="section dw_tag {'tag':'supplementary-nav;item;8'}" href="http://www.metacritic.com/browse/movies/score/metascore/year/filtered?sort=desc&amp;year_selected=2016">2016 High Scores</a>
                            </li>
                                                            </ol>
            </div>
                                    <div id="supplementary-articles" class="supplements supplement_articles">
                <ol class="supplements supplement_articles">
                                                                                                    <li class="supplement supplement_link">
                                <a class="dw_tag {'tag':'supplementary-nav;article;1'}" href="http://www.metacritic.com/pictures/july-2016-movie-preview">July Movie Preview</a>
                            </li>
                                                                                                                            <li class="supplement supplement_link">
                                <a class="dw_tag {'tag':'supplementary-nav;article;2'}" href="http://www.metacritic.com/feature/preview-of-this-weekends-new-movies">What Movie Should I See This Weekend?</a>
                            </li>
                                                                                                                            <li class="supplement supplement_link">
                                <a class="dw_tag {'tag':'supplementary-nav;article;3'}" href="http://www.metacritic.com/feature/summer-movie-metascore-predictions-2016">Metascore Predictions for 30 Summer Films</a>
                            </li>
                                                            </ol>
                <div class="more_supplements more_articles">

                    <a class="dw_tag {'tag':'supplementary-nav;more-articles'}" href="/feature">More articles »</a>
                </div>
            </div>
                    </div>
    </div>
</div>




    <div id="taboola-right-rail-thumbnails" class=" trc_related_container trc_spotlight_widget trc_elastic trc_elastic_trc_34597 "><div class="trc_rbox_container" style="display: block;"><div><div id="trc_wrapper_34597" class="trc_rbox ab_alternating-thumbnails-rr_abp-mode trc-content-sponsored " style="overflow: hidden; display: block;"><div id="trc_header_34597" class="trc_rbox_header trc_rbox_border_elm"><div class="trc_header_ext"><div class="logoDiv link-disclosure  attribution-disclosure-link-sponsored"><a class="trc_desktop_disclosure_link trc_attribution_position_top" rel="nofollow" href="http://popup.taboola.com/en/?template=colorbox&amp;taboola_utm_source=cbsinteractive-metacritic&amp;taboola_utm_medium=bytaboola&amp;taboola_utm_content=ab_alternating-thumbnails-rr_abp-mode:desktop user_reviews Right Rail Thumbnails:" target="_blank"><span>Sponsored Links</span><span class="trc_logos_v_align">&nbsp;</span></a><a class="trc_mobile_disclosure_link trc_attribution_position_top" rel="nofollow" href="http://popup.taboola.com/en/?template=colorbox&amp;taboola_utm_source=cbsinteractive-metacritic&amp;taboola_utm_medium=bytaboola&amp;taboola_utm_content=ab_alternating-thumbnails-rr_abp-mode:desktop user_reviews Right Rail Thumbnails:" target="_blank"><span>Sponsored Links</span><span class="trc_logos_v_align">&nbsp;</span></a></div><div class="logoDiv link-disclosure  attribution-disclosure-link-hybrid"><a class="trc_desktop_disclosure_link trc_attribution_position_top" rel="nofollow" href="http://popup.taboola.com/en/?template=colorbox&amp;taboola_utm_source=cbsinteractive-metacritic&amp;taboola_utm_medium=bytaboola&amp;taboola_utm_content=ab_alternating-thumbnails-rr_abp-mode:desktop user_reviews Right Rail Thumbnails:" target="_blank"><span>Promoted Links</span><span class="trc_logos_v_align">&nbsp;</span></a><a class="trc_mobile_disclosure_link trc_attribution_position_top" rel="nofollow" href="http://popup.taboola.com/en/?template=colorbox&amp;taboola_utm_source=cbsinteractive-metacritic&amp;taboola_utm_medium=bytaboola&amp;taboola_utm_content=ab_alternating-thumbnails-rr_abp-mode:desktop user_reviews Right Rail Thumbnails:" target="_blank"><span>Promoted Links</span><span class="trc_logos_v_align">&nbsp;</span></a></div></div><span class="trc_rbox_header_span">Recommended</span></div><div id="outer_34597" class="trc_rbox_outer"><div id="rbox-o2m" class="trc_rbox_div trc_rbox_border_elm"><div id="internal_trc_34597"><div data-item-id="~~V1~~-4082193693269660077~~jdgxVNRz2M4WEPhjV2BJ_5cP646jYXmr5TNqtyO4Cy7sBxIeYKC_jpMSMGAeWdwJpaplo213-RuxUXSUrzOFNA" data-item-title="Sparta: The Strategy Game Phenomenon of 2016" data-item-thumb="https://console.brax-cdn.com/creatives/041ca465-399e-4bcf-9b7d-edb6b5c8d972/2a8aa835-11de-4cd2-951e-77b4cbc110e3.png" data-item-syndicated="true" class="videoCube trc_spotlight_item origin-default thumbnail_top syndicatedItem textItem videoCube_1_child trc-first-recommendation trc-spotlight-first-recommendation  trc_excludable "><a title="Sparta: The Strategy Game Phenomenon of 2016" href="http://plarium.com/play/en/sparta/017_armies_hybrid_anim_g?plid=83497&amp;pxl=taboola_fr&amp;utm_content=abd0007&amp;publisherID=cbsinteractive-metacritic" rel="nofollow" target="_blank" class=" item-thumbnail-href "><div class="thumbBlock_holder"><span class="thumbBlock" style="background-image: url(&quot;http://images.taboola.com/taboola/image/fetch/f_jpg%2Cq_80%2Ch_142%2Cw_284%2Cc_fill%2Cg_faces%2Ce_sharpen/https%3A//console.brax-cdn.com/creatives/041ca465-399e-4bcf-9b7d-edb6b5c8d972/2a8aa835-11de-4cd2-951e-77b4cbc110e3.png&quot;);"><span class="thumbnail-overlay"></span><span class="branding">Sparta - Free Online Game</span><span class="static-text top-right"></span></span><div class="videoCube_aspect"></div></div></a><a title="Sparta: The Strategy Game Phenomenon of 2016" href="http://plarium.com/play/en/sparta/017_armies_hybrid_anim_g?plid=83497&amp;pxl=taboola_fr&amp;utm_content=abd0007&amp;publisherID=cbsinteractive-metacritic" rel="nofollow" target="_blank" class=" item-label-href "><span class="video-label-box"><span class="video-label video-title trc_ellipsis " style="-webkit-line-clamp: 2;">Sparta: The Strategy Game Phenomenon of 2016</span><span class="branding">Sparta - Free Online Game</span></span></a><div class=" trc_user_exclude_btn " title="Remove this item"></div><div class=" trc_exclude_overlay trc_fade "></div><div class=" trc_undo_btn ">Undo</div></div><div data-item-id="~~V1~~-2475962748955690044~~m3hHddpGqzUZHsLUiHOcyJRo1UsfHf0-1O2i3xKxtb6TLmAL-VpKWSEJMZDbmcjWpaplo213-RuxUXSUrzOFNA" data-item-title="The Most Exciting MMORPG You&amp;#39;ve Ever Played! Don&amp;#39;t Miss This!" data-item-thumb="https://console.brax-cdn.com/creatives/041ca465-399e-4bcf-9b7d-edb6b5c8d972/c54967264baa0e0dff0525d1dda0783c_3743eb0c102ac285c8edc8fcfef29f9c.png" data-item-syndicated="true" class="videoCube trc_spotlight_item origin-default thumbnail_top syndicatedItem textItem videoCube_2_child trc_excludable "><a title="The Most Exciting MMORPG You've Ever Played! Don't Miss This!" href="http://plarium.com/play/en/stormfall/004_dragon_hybrid_anim?plid=85190&amp;pxl=taboola_fr&amp;&amp;publisherID=cbsinteractive-metacritic" rel="nofollow" target="_blank" class=" item-thumbnail-href "><div class="thumbBlock_holder"><span class="thumbBlock" style="background-image: url(&quot;http://images.taboola.com/taboola/image/fetch/f_jpg%2Cq_80%2Ch_142%2Cw_284%2Cc_fill%2Cg_faces%2Ce_sharpen/https%3A//console.brax-cdn.com/creatives/041ca465-399e-4bcf-9b7d-edb6b5c8d972/c54967264baa0e0dff0525d1dda0783c_3743eb0c102ac285c8edc8fcfef29f9c.png&quot;);"><span class="thumbnail-overlay"></span><span class="branding">Stormfall: Free Online Game</span><span class="static-text top-right"></span></span><div class="videoCube_aspect"></div></div></a><a title="The Most Exciting MMORPG You've Ever Played! Don't Miss This!" href="http://plarium.com/play/en/stormfall/004_dragon_hybrid_anim?plid=85190&amp;pxl=taboola_fr&amp;&amp;publisherID=cbsinteractive-metacritic" rel="nofollow" target="_blank" class=" item-label-href "><span class="video-label-box"><span class="video-label video-title trc_ellipsis " style="-webkit-line-clamp: 2;">The Most Exciting MMORPG You've Ever Played! Don't Miss This!</span><span class="branding">Stormfall: Free Online Game</span></span></a><div class=" trc_user_exclude_btn " title="Remove this item"></div><div class=" trc_exclude_overlay trc_fade "></div><div class=" trc_undo_btn ">Undo</div></div><div data-item-id="~~V1~~-7778055205621534399~~jw--fJuG7vhZxdC6zHYS9Kg1WJ_KeLT2Keli_siwgoDmw8EK7J7MiIhXTT0y10fwpaplo213-RuxUXSUrzOFNA" data-item-title="I’m a Woman Who Joined Dollar Shave Club. Here’s What Happened..." data-item-thumb="http://cdn.taboolasyndication.com/libtrc/static/thumbnails/33ec4a5a4d82cd1dba275ca8327a37d3.png" data-item-syndicated="true" class="videoCube trc_spotlight_item origin-default thumbnail_top syndicatedItem textItem videoCube_3_child trc_excludable "><a title="I’m a Woman Who Joined Dollar Shave Club. Here’s What Happened..." href="http://try.dollarshaveclub.com/tab-desk-lifehack/?utm_medium=nat&amp;utm_source=tabo&amp;utm_campaign=femalelifehack-desktop&amp;utm_content=femalelifehack-desktop&amp;utm_term=I%E2%80%99m+a+Woman+Who+Joined+Dollar+Shave+Club.+Here%E2%80%99s+What+Happened..." rel="nofollow" target="_blank" class=" item-thumbnail-href "><div class="thumbBlock_holder"><span class="thumbBlock" style="background-image: url(&quot;http://images.taboola.com/taboola/image/fetch/f_jpg%2Cq_80%2Ch_142%2Cw_284%2Cc_fill%2Cg_faces%2Ce_sharpen/http%3A//cdn.taboolasyndication.com/libtrc/static/thumbnails/33ec4a5a4d82cd1dba275ca8327a37d3.png&quot;);"><span class="thumbnail-overlay"></span><span class="branding">Dollar Shave Club</span><span class="static-text top-right"></span></span><div class="videoCube_aspect"></div></div></a><a title="I’m a Woman Who Joined Dollar Shave Club. Here’s What Happened..." href="http://try.dollarshaveclub.com/tab-desk-lifehack/?utm_medium=nat&amp;utm_source=tabo&amp;utm_campaign=femalelifehack-desktop&amp;utm_content=femalelifehack-desktop&amp;utm_term=I%E2%80%99m+a+Woman+Who+Joined+Dollar+Shave+Club.+Here%E2%80%99s+What+Happened..." rel="nofollow" target="_blank" class=" item-label-href "><span class="video-label-box"><span class="video-label video-title">I’m a Woman Who Joined Dollar Shave Club. Here’s What Happened...</span><span class="branding">Dollar Shave Club</span></span></a><div class=" trc_user_exclude_btn " title="Remove this item"></div><div class=" trc_exclude_overlay trc_fade "></div><div class=" trc_undo_btn ">Undo</div></div><div data-item-id="~~V1~~-5558615715055156430~~QcTc8uen571xe6I9_3lhVAgIrTpT6rY3xu-NfoPw2LfgCv9nLWD1rvzBRY97cGRkpaplo213-RuxUXSUrzOFNA" data-item-title="1 in 3 Pets Will Get Lost. Keep Yours Safe With This Device" data-item-thumb="http://dx4ncraaox0l3.cloudfront.net/whistle20/wagg-thumbnail.jpg" data-item-syndicated="true" class="videoCube trc_spotlight_item origin-default thumbnail_top syndicatedItem textItem videoCube_4_child trc_excludable "><a title="1 in 3 Pets Will Get Lost. Keep Yours Safe With This Device" href="http://www.whistle.com/?utm_source=taboola&amp;utm_medium=referral" rel="nofollow" target="_blank" class=" item-thumbnail-href "><div class="thumbBlock_holder"><span class="thumbBlock" style="background-image: url(&quot;http://images.taboola.com/taboola/image/fetch/f_jpg%2Cq_80%2Ch_142%2Cw_284%2Cc_fill%2Cg_faces%2Ce_sharpen/http%3A//dx4ncraaox0l3.cloudfront.net/whistle20/wagg-thumbnail.jpg&quot;);"><span class="thumbnail-overlay"></span><span class="branding">Whistle</span><span class="static-text top-right"></span></span><div class="videoCube_aspect"></div></div></a><a title="1 in 3 Pets Will Get Lost. Keep Yours Safe With This Device" href="http://www.whistle.com/?utm_source=taboola&amp;utm_medium=referral" rel="nofollow" target="_blank" class=" item-label-href "><span class="video-label-box"><span class="video-label video-title">1 in 3 Pets Will Get Lost. Keep Yours Safe With This Device</span><span class="branding">Whistle</span></span></a><div class=" trc_user_exclude_btn " title="Remove this item"></div><div class=" trc_exclude_overlay trc_fade "></div><div class=" trc_undo_btn ">Undo</div></div></div></div></div><div class="trc-widget-footer"><div class="logoDiv link-adc "><a class="trc_desktop_adc_link trc_attribution_position_bottom" rel="nofollow" href="http://popup.taboola.com/en/?template=colorbox&amp;taboola_utm_source=cbsinteractive-metacritic&amp;taboola_utm_medium=bytaboola&amp;taboola_utm_content=ab_alternating-thumbnails-rr_abp-mode:desktop user_reviews Right Rail Thumbnails:" target="_blank"><span class="trc_adc_wrapper"><span class="trc_adc_s_logo"></span>&nbsp;</span><span class="trc_logos_v_align">&nbsp;</span></a><a class="trc_mobile_adc_link trc_attribution_position_bottom" rel="nofollow" href="http://popup.taboola.com/en/?template=colorbox&amp;taboola_utm_source=cbsinteractive-metacritic&amp;taboola_utm_medium=bytaboola&amp;taboola_utm_content=ab_alternating-thumbnails-rr_abp-mode:desktop user_reviews Right Rail Thumbnails:" target="_blank"><span class="trc_adc_wrapper"><span class="trc_adc_s_logo"></span>&nbsp;</span><span class="trc_logos_v_align">&nbsp;</span></a></div><div class="logoDiv link-attribution "><a class="trc_desktop_attribution_link trc_attribution_position_bottom" rel="nofollow" href="http://popup.taboola.com/en/?template=colorbox&amp;taboola_utm_source=cbsinteractive-metacritic&amp;taboola_utm_medium=bytaboola&amp;taboola_utm_content=ab_alternating-thumbnails-rr_abp-mode:desktop user_reviews Right Rail Thumbnails:" target="_blank"><span>by Taboola</span><span class="trc_logos_v_align">&nbsp;</span></a><a class="trc_mobile_attribution_link trc_attribution_position_bottom" rel="nofollow" href="http://popup.taboola.com/en/?template=colorbox&amp;taboola_utm_source=cbsinteractive-metacritic&amp;taboola_utm_medium=bytaboola&amp;taboola_utm_content=ab_alternating-thumbnails-rr_abp-mode:desktop user_reviews Right Rail Thumbnails:" target="_blank"><span>by Taboola</span><span class="trc_logos_v_align">&nbsp;</span></a></div></div><div class="trc_clearer"></div></div></div></div></div>

    <script type="text/javascript">
        if ( window._taboola ) {
                        var placement = 'desktop user_reviews Right Rail Thumbnails';
            window.metac_tContentWidget.push(placement);
            _taboola.push({
                mode: 'alternating-thumbnails-rr',
                container: 'taboola-right-rail-thumbnails',
                placement: placement,
                target_type: 'mix'
            });
                    }
    </script>







<div class="module reviews_module critic_reviews_module contain_module">


            <div class="head head_type_1"><div class="head_wrap"><h2 class="module_title"><a href="/movie/spider-man-3/critic-reviews">Critic Reviews</a></h2><div class="more"><span class="more_item more_all_reviews"><a href="/movie/spider-man-3/critic-reviews">All reviews »</a></span></div></div></div>
<div class="body">
                                <div class="score_details metascore_details">

<div class="score_summary metascore_summary">
    <div class="metascore_wrap">
        <div class="label">Metascore</div>




    <a class="metascore_anchor" href="/movie/spider-man-3/critic-reviews">
<div class="metascore_w medium movie mixed"><meta itemprop="bestRating" content="100"><span itemprop="ratingValue">59</span></div>
    </a>



                <div class="summary">
            <p>
                <span class="desc">
                                            Mixed or average reviews
                                    </span>
						<span class="count">
				<span class="separator"> - </span>
                <span class="based">based on</span>
									<a href="/movie/spider-man-3/critic-reviews">
                                                    <span>
                                40
                            </span> Critics                                            </a>
							</span>
			                                            </p>
        </div>
    </div>
</div>
    <div class="score_distribution">
    <div class="distribution_wrap">
        <div class="distribution_title">Critic score distribution:</div>
        <ol class="score_counts">
                        <li class="score_count">
                <div class="count_wrap">
                    <span class="label">Positive:</span>
                    <span class="data">
                        <a href="/movie/spider-man-3/critic-reviews?dist=positive">                            <span class="total" style="width:100%;">
                                <span class="count">25</span>
                                <span class="distribution positive"> out of 40</span>
                            </span>
                        </a>                    </span>
                </div>
            </li>
                        <li class="score_count">
                <div class="count_wrap">
                    <span class="label">Mixed:</span>
                    <span class="data">
                        <a href="/movie/spider-man-3/critic-reviews?dist=neutral">                            <span class="total" style="width:52%;">
                                <span class="count">13</span>
                                <span class="distribution mixed"> out of 40</span>
                            </span>
                        </a>                    </span>
                </div>
            </li>
                        <li class="score_count">
                <div class="count_wrap">
                    <span class="label">Negative:</span>
                    <span class="data">
                        <a href="/movie/spider-man-3/critic-reviews?dist=negative">                            <span class="total" style="width:8%;">
                                <span class="count">2</span>
                                <span class="distribution negative"> out of 40</span>
                            </span>
                        </a>                    </span>
                </div>
            </li>
                    </ol>
		    </div>
</div>

</div>

                            <ol class="reviews critic_reviews">            <li class="review critic_review first_review">
                <div class="review_btm review_btm_r"><div class="review_btm review_btm_l"><div class="review_top review_top_r"><div class="review_top review_top_l">
                    <div class="review_content">
                        <div class="review_section">
                            <div class="review_stats">


                                <div class="review_critic has_author"><div class="source"><a rel="popup:external" href="http://www.hollywoodreporter.com/hr/film/reviews/article_display.jsp?JSESSIONID=S0Q3GrqL9WzMn0TySlK7JTh8tNVcfgLg1fVTvBB7r8mJDsMz7VGL!1444377788&amp;&amp;rid=9075" target="_blank">The Hollywood Reporter</a></div><div class="author"><span class="label"><span class="text">Reviewed by:</span>&nbsp;</span><a rel="popup:external" class="external" href="http://www.hollywoodreporter.com/hr/film/reviews/article_display.jsp?JSESSIONID=S0Q3GrqL9WzMn0TySlK7JTh8tNVcfgLg1fVTvBB7r8mJDsMz7VGL!1444377788&amp;&amp;rid=9075" target="_blank">Michael Rechtshaffen</a></div></div>

                                <div class="review_grade has_author">



<div class="metascore_w medium movie positive indiv">80</div>

                                </div>
                            </div>
                            <div class="review_body">
                                The wow factor works overtime with state-of-the-art effects sequences that often are as beautiful as they are astonishing.
                            </div>
                        </div>
                                                    <div class="review_section review_actions">
                                                                                                    <div class="review_action full_review"><a rel="popup:external" class="external" href="http://www.hollywoodreporter.com/hr/film/reviews/article_display.jsp?JSESSIONID=S0Q3GrqL9WzMn0TySlK7JTh8tNVcfgLg1fVTvBB7r8mJDsMz7VGL!1444377788&amp;&amp;rid=9075" target="_blank">Read full review</a></div>
                                                            </div>
                                            </div>
                </div></div></div></div>
            </li>
                                                        <li class="review critic_review">
                <div class="review_btm review_btm_r"><div class="review_btm review_btm_l"><div class="review_top review_top_r"><div class="review_top review_top_l">
                    <div class="review_content">
                        <div class="review_section">
                            <div class="review_stats">


                                <div class="review_critic has_author"><div class="source"><a rel="popup:external" href="http://www.variety.com/review/VE1117933393.html?categoryid=31&amp;cs=1" target="_blank">Variety</a></div><div class="author"><span class="label"><span class="text">Reviewed by:</span>&nbsp;</span><a rel="popup:external" class="external" href="http://www.variety.com/review/VE1117933393.html?categoryid=31&amp;cs=1" target="_blank">Todd McCarthy</a></div></div>

                                <div class="review_grade has_author">



<div class="metascore_w medium movie mixed indiv">50</div>

                                </div>
                            </div>
                            <div class="review_body">
                                A sense of strain envelops the proceedings this time around. One can feel the effort required to suit up one more time, come up with fresh variations on a winning formula and inject urgency into a format that basically needs to be repeated and, due to audience expectations, can't be toyed with or deepened very much.
                            </div>
                        </div>
                                                    <div class="review_section review_actions">
                                                                                                    <div class="review_action full_review"><a rel="popup:external" class="external" href="http://www.variety.com/review/VE1117933393.html?categoryid=31&amp;cs=1" target="_blank">Read full review</a></div>
                                                            </div>
                                            </div>
                </div></div></div></div>
            </li>
                                                        <li class="review critic_review last_review">
                <div class="review_btm review_btm_r"><div class="review_btm review_btm_l"><div class="review_top review_top_r"><div class="review_top review_top_l">
                    <div class="review_content">
                        <div class="review_section">
                            <div class="review_stats">


                                <div class="review_critic has_author"><div class="source"><a rel="popup:external" href="http://www.nypost.com/seven/04242007/entertainment/movies/spidey_works_black_magic_in_3_movies_lou_lumenick.htm" target="_blank">New York Post</a></div><div class="author"><span class="label"><span class="text">Reviewed by:</span>&nbsp;</span><a rel="popup:external" class="external" href="http://www.nypost.com/seven/04242007/entertainment/movies/spidey_works_black_magic_in_3_movies_lou_lumenick.htm" target="_blank">Lou Lumenick</a></div></div>

                                <div class="review_grade has_author">



<div class="metascore_w medium movie positive indiv">75</div>

                                </div>
                            </div>
                            <div class="review_body">
                                Overly long and complicated, it's packed with crowd-pleasing moments and satisfactorily wraps up the trilogy - without quite capturing the magic of the first two installments.
                            </div>
                        </div>
                                                    <div class="review_section review_actions">
                                                                                                    <div class="review_action full_review"><a rel="popup:external" class="external" href="http://www.nypost.com/seven/04242007/entertainment/movies/spidey_works_black_magic_in_3_movies_lou_lumenick.htm" target="_blank">Read full review</a></div>
                                                            </div>
                                            </div>
                </div></div></div></div>
            </li>
                                        </ol>
                        </div>




                <div class="foot">
        <div class="foot_wrap">

            <div class="more">
                <span class="more_item more_all_reviews"><a href="/movie/spider-man-3/critic-reviews">See all critic reviews »</a></span>
            </div>
                </div>
    </div>

    </div>



        <div id="mpu_bottom" class="ad_unit">

                            <script type="text/javascript">

                        googletag.cmd.push(function() {

                                                            window.metac_g_ad_mpu_bottom = googletag.defineSlot("/8264/aw-metacritic/movies",[300,250], "mpu_bottom").addService(googletag.pubads()).setTargeting("pos", "bottom");


                        });


                        window.metac_ads_pushdisplay.push("mpu_bottom");
                                    </script>
                            <div id="google_ads_iframe_/8264/aw-metacritic/movies_3__container__" style="border: 0pt none;"><iframe id="google_ads_iframe_/8264/aw-metacritic/movies_3" title="3rd party ad content" name="google_ads_iframe_/8264/aw-metacritic/movies_3" width="300" height="250" scrolling="no" marginwidth="0" marginheight="0" frameborder="0" src="javascript:&quot;<html><body style='background:transparent'></body></html>&quot;" style="border: 0px; vertical-align: bottom;"></iframe></div></div>


                </div>
                    </div>
    </div>
        </div>
                    </div>
                </div>
            </div>
        </div>

        <div id="leader_bottom" class="ad_unit"><div id="google_ads_iframe_/8264/aw-metacritic/movies_4__container__" style="border: 0pt none;"><iframe id="google_ads_iframe_/8264/aw-metacritic/movies_4" title="3rd party ad content" name="google_ads_iframe_/8264/aw-metacritic/movies_4" width="728" height="90" scrolling="no" marginwidth="0" marginheight="0" frameborder="0" src="javascript:&quot;<html><body style='background:transparent'></body></html>&quot;" style="border: 0px; vertical-align: bottom;"></iframe></div><iframe id="google_ads_iframe_/8264/aw-metacritic/movies_4__hidden__" title="" name="google_ads_iframe_/8264/aw-metacritic/movies_4__hidden__" width="0" height="0" scrolling="no" marginwidth="0" marginheight="0" frameborder="0" src="javascript:&quot;<html><body style='background:transparent'></body></html>&quot;" style="border: 0px; vertical-align: bottom; visibility: hidden; display: none;"></iframe></div>



            </div>

        <div id="skin" class="ad_unit">

                            <script type="text/javascript">

                        googletag.cmd.push(function() {

                                                            window.metac_g_ad_skin = googletag.defineSlot("/8264/aw-metacritic/movies",[1600,1000], "skin").addService(googletag.pubads()).setTargeting("pos", "top");


                        });


                        window.metac_ads_pushdisplay.push("skin");
                                    </script>
                            <div id="google_ads_iframe_/8264/aw-metacritic/movies_5__container__" style="border: 0pt none;"><iframe id="google_ads_iframe_/8264/aw-metacritic/movies_5" title="3rd party ad content" name="google_ads_iframe_/8264/aw-metacritic/movies_5" width="1600" height="1000" scrolling="no" marginwidth="0" marginheight="0" frameborder="0" src="javascript:&quot;<html><body style='background:transparent'></body></html>&quot;" style="border: 0px; vertical-align: bottom;"></iframe></div></div>



                            </div>


        <div id="intromercial" class="ad_unit">

                            <script type="text/javascript">

                        googletag.cmd.push(function() {

                                                            window.metac_g_ad_intromercial = googletag.defineOutOfPageSlot("/8264/aw-metacritic/movies",
                                    "intromercial").addService(googletag.pubads());


                        });


                        window.metac_ads_pushdisplay.push("intromercial");
                                    </script>
                            <div id="google_ads_iframe_/8264/aw-metacritic/movies_6__container__" style="border: 0pt none;"><iframe id="google_ads_iframe_/8264/aw-metacritic/movies_6" title="3rd party ad content" name="google_ads_iframe_/8264/aw-metacritic/movies_6" width="1" height="1" scrolling="no" marginwidth="0" marginheight="0" frameborder="0" src="javascript:&quot;<html><body style='background:transparent'></body></html>&quot;" style="border: 0px; vertical-align: bottom;"></iframe></div></div>





    <div id="mastfoot">

        <div id="site_footer" class="mastfoot_section">
    <div class="mastfoot_wrap">


         <div class="about_metacritic_nav"></div>



		<div id="providers">
	<a href="http://www.allmusic.com">Music title data, credits, and images provided by <span>AMG</span></a>
	<span class="link_divider">|</span><a href="http://www.imdb.com">Movie title data, credits, and poster art provided by <span>IMDb</span></a>
	<span class="link_divider">|</span><a href="http://www.internetvideoarchive.com">Video and Images provided by <span>IVA</span></a>
    <div id="trademark">
        We Deal With Criticism<sup>®</sup>&nbsp;
	</div>
</div>

		<div class="soc_med_gms">
		<div class="page_title">

            <img src="/images/layout/mc_logo_inverted.png">
        </div>




		    <div class="links social_media_nav">
        <div class="links_label">Metacritic on:</div>                                                                            <ul class="links social_media_nav">
                                                    <li class="link_item link_twitter first_link">
                <span class="link_item">
                    <span class="link_item_wrap">
                                                    <a class="twitter" href="http://twitter.com/metacritic">
                                <span class="link_text">Twitter</span>
                            </a>
                                            </span>
                </span>
            </li>
                                                        <li class="link_item link_facebook last_link">
                <span class="link_item">
                    <span class="link_item_wrap">
                                                    <a class="facebook" href="http://www.facebook.com/Metacritic">
                                <span class="link_text">Facebook</span>
                            </a>
                                            </span>
                </span>
            </li>
                            </ul>
                        </div>

		</div>


		    <div class="links site_nav">
                                                                                    <ul class="links site_nav">
                                                    <li class="link_item link_movies first_link">
                <span class="link_item">
                    <span class="link_item_wrap">
                                                    <a class="movies" href="http://www.metacritic.com/movie">
                                <span class="link_text">Movies</span>
                            </a>
                                            </span>
                </span>
            </li>
                                                        <li class="link_item link_tv">
                <span class="link_item">
                    <span class="link_item_wrap">
                                                    <a class="tv" href="http://www.metacritic.com/tv">
                                <span class="link_text">TV</span>
                            </a>
                                            </span>
                </span>
            </li>
                                                        <li class="link_item link_music">
                <span class="link_item">
                    <span class="link_item_wrap">
                                                    <a class="music" href="http://www.metacritic.com/music">
                                <span class="link_text">Music</span>
                            </a>
                                            </span>
                </span>
            </li>
                                                        <li class="link_item link_ps4">
                <span class="link_item">
                    <span class="link_item_wrap">
                                                    <a class="ps4" href="http://www.metacritic.com/game/playstation-4">
                                <span class="link_text">PS4</span>
                            </a>
                                            </span>
                </span>
            </li>
                                                        <li class="link_item link_ps3">
                <span class="link_item">
                    <span class="link_item_wrap">
                                                    <a class="ps3" href="http://www.metacritic.com/game/playstation-3">
                                <span class="link_text">PS3</span>
                            </a>
                                            </span>
                </span>
            </li>
                                                        <li class="link_item link_xboxone">
                <span class="link_item">
                    <span class="link_item_wrap">
                                                    <a class="xboxone" href="http://www.metacritic.com/game/xbox-one">
                                <span class="link_text">XboxOne</span>
                            </a>
                                            </span>
                </span>
            </li>
                                                        <li class="link_item link_xbox360">
                <span class="link_item">
                    <span class="link_item_wrap">
                                                    <a class="xbox360" href="http://www.metacritic.com/game/xbox-360">
                                <span class="link_text">Xbox360</span>
                            </a>
                                            </span>
                </span>
            </li>
                                                        <li class="link_item link_pc">
                <span class="link_item">
                    <span class="link_item_wrap">
                                                    <a class="pc" href="http://www.metacritic.com/game/pc">
                                <span class="link_text">PC</span>
                            </a>
                                            </span>
                </span>
            </li>
                                                        <li class="link_item link_wii_u">
                <span class="link_item">
                    <span class="link_item_wrap">
                                                    <a class="wii_u" href="http://www.metacritic.com/game/wii-u">
                                <span class="link_text">WiiU</span>
                            </a>
                                            </span>
                </span>
            </li>
                                                        <li class="link_item link_3ds">
                <span class="link_item">
                    <span class="link_item_wrap">
                                                    <a class="3ds" href="http://www.metacritic.com/game/3ds">
                                <span class="link_text">3DS</span>
                            </a>
                                            </span>
                </span>
            </li>
                                                        <li class="link_item link_vita">
                <span class="link_item">
                    <span class="link_item_wrap">
                                                    <a class="vita" href="http://www.metacritic.com/game/playstation-vita">
                                <span class="link_text">PS Vita</span>
                            </a>
                                            </span>
                </span>
            </li>
                                                        <li class="link_item link_ios">
                <span class="link_item">
                    <span class="link_item_wrap">
                                                    <a class="ios" href="http://www.metacritic.com/game/ios">
                                <span class="link_text">iOS</span>
                            </a>
                                            </span>
                </span>
            </li>
                                                        <li class="link_item link_features">
                <span class="link_item">
                    <span class="link_item_wrap">
                                                    <a class="features" href="http://www.metacritic.com/feature">
                                <span class="link_text">Features</span>
                            </a>
                                            </span>
                </span>
            </li>
                                                        <li class="link_item link_rss_feeds last_link">
                <span class="link_item">
                    <span class="link_item_wrap">
                                                    <a class="rss_feeds" href="http://www.metacritic.com/rss">
                                <span class="link_text">RSS Feeds</span>
                            </a>
                                            </span>
                </span>
            </li>
                            </ul>
                        </div>

    </div>
</div>
        <div id="corporate_footer" class="mastfoot_section">
    <div class="mastfoot_wrap">


            <form id="cbs_related_sites_form" class="related_sites" action="">
                <fieldset>
                    <legend>Other CBS Interactive Sites</legend>
                    <label for="cbsi_footer_menu">Visit other CBS Interactive Sites</label>
                    <select id="cbsi_footer_menu">
                        <option value="">Select Site</option>
                                                    <option value="http://www.cbscares.com">CBS Cares</option>
                                                    <option value="http://www.cbsfilms.com">CBS Films</option>
                                                    <option value="http://www.cbsradio.com">CBS Radio</option>
                                                    <option value="http://www.cbs.com">CBS.com</option>
                                                    <option value="http://www.cbsinteractive.com">CBSInteractive</option>
                                                    <option value="http://www.cbsnews.com">CBSNews.com</option>
                                                    <option value="http://www.cbssports.com">CBSSports.com</option>
                                                    <option value="http://www.chowhound.com">Chowhound</option>
                                                    <option value="http://www.cnet.com">CNET</option>
                                                    <option value="http://www.gamespot.com">GameSpot</option>
                                                    <option value="http://www.help.com">Help.com</option>
                                                    <option value="http://www.last.fm">Last.fm</option>
                                                    <option value="http://www.maxpreps.com">MaxPreps</option>
                                                    <option value="http://www.metacritic.com">Metacritic</option>
                                                    <option value="http://moneywatch.bnet.com">Moneywatch</option>
                                                    <option value="http://www.mysimon.com">mySimon</option>
                                                    <option value="http://www.radio.com">Radio.com</option>
                                                    <option value="http://www.search.com">Search.com</option>
                                                    <option value="http://www.shopper.com">Shopper.com</option>
                                                    <option value="http://www.sho.com">Showtime</option>
                                                    <option value="http://www.smartplanet.com">SmartPlanet</option>
                                                    <option value="http://www.techrepublic.com">TechRepublic</option>
                                                    <option value="http://www.tv.com">TV.com</option>
                                                    <option value="http://www.urbanbaby.com">UrbanBaby.com</option>
                                                    <option value="http://www.zdnet.com">ZDNet</option>
                                                    <option value="http://collegenetwork.cbssports.com">College Network</option>
                                                    <option value="http://www.metrolyrics.com">MetroLyrics</option>
                                                    <option value="http://www.tvguide.com/">TvGuide.com</option>
                                            </select>
                    <input type="button" value="Go" onclick="window.location=document.getElementById('cbsi_footer_menu').options[document.getElementById('cbsi_footer_menu').selectedIndex].value;">
                </fieldset>
            </form>
                <div class="about_cbs">
            <p id="footer_about_links">
                <a class="first" href="http://www.cbsinteractive.com">About CBS Interactive</a>
                | <a href="http://www.cbsinteractive.com/careers/">Jobs</a>
                | <a href="http://www.cbsinteractive.com/advertise/">Advertise</a>
                | <a href="http://www.metacritic.com/faq">FAQ</a>
                | <a href="http://www.metacritic.com/about-metacritic">About Metacritic</a>
                | <a href="http://www.metacritic.com/contact-us">Contact</a>
            </p>
            <p id="footer_rights">
                © 2016 CBS Interactive Inc. All rights reserved.
                <span id="footer_privacy">| <a href="http://legalterms.cbsinteractive.com/privacy">Privacy Policy</a></span>
                <span id="footer_terms">| <a href="https://cbsi.secure.force.com/CBSi/articles/FAQ/CBSi-Terms-of-Use?template=template_tougl&amp;referer=tougl.com&amp;data=&amp;cfs=default">Terms of Use</a></span>
            </p>
        </div>
    </div>
</div>
    </div>
</div>

<div id="site_scripts" class="dw_tracking">

<script type="text/javascript" src="/js/omniture/uuid.js"></script>
<script type="text/javascript">
    var MC_UUID = uuid.v1();
</script>




<script type="text/javascript">


    googletag.cmd.push(function() {

                    googletag.pubads().setTargeting("ptype", "user_reviews");

                            googletag.pubads().setTargeting("movieId", "movie-500252");
                            googletag.pubads().setTargeting("movie", "spider-man-3");
                            googletag.pubads().setTargeting("score", "59");

        googletag.pubads().setTargeting("vguid", MC_UUID);
        googletag.pubads().setTargeting("env", "prod");
                        var parts = window.location.hash.split("=");
        if ( parts.length > 1 && parts[0] == '#ftag' ) {
            googletag.pubads().setTargeting("ftag",parts[1]);
        }
                googletag.pubads().enableAsyncRendering();
        googletag.pubads().enableSingleRequest();
        googletag.pubads().collapseEmptyDivs();
        googletag.enableServices();
    });


</script>







        <script type="text/JavaScript" src="http://cn.cbsimg.net/cnwk.1d/Aud/javascript/urs.js"></script>


    <script type="text/javascript">
        if ( window.MetaC && MetaC.URS ) {
            MetaC.URS.config(227, false);
        }
    </script>



<script language="JavaScript" type="text/javascript">

    var utag_data = {
        isDev:0,
                            siteType:"desktop web",
                deviceType:"desktop",
                siteSection:"movies",
                pageType:"user_reviews",
                pageFindingMethod:"Internal",
                userId:null,userState:"not authenticated",userType:"anon",movieId:"mc-movie-500252",movieTitle:"Spider-Man 3",bkPath:"/8264/aw-metacritic/movies",pageViewGuid:MC_UUID
    };



            window.om_lead_media = {
                mediaType: "Movie",
                mediaId: "mc-movie-500252",
                mediaTitle: "Spider-Man 3"
            };




    if ( window.eventAmazonBuyView ) {
        // omdata.context.eventAmazonBuyView = 1;
        utag_data.eventAmazonBuyView = 1;
    }
    if ( window.eventAmazonPivView ) {
        // omdata.context.eventAmazonPivView = 1;
        utag_data.eventAmazonPivView = 1;
    }



    if ( window.metac_tContentWidget && window.metac_tContentWidget.length > 0 ) {
        utag_data.contentWidget = window.metac_tContentWidget.join('|');;
    }



</script>




<script type="text/javascript">
    (function(a,b,c,d){
    a='//tags.tiqcdn.com/utag/cbsi/metacriticsite/prod/utag.js';
    b=document;c='script';d=b.createElement(c);d.src=a;d.type='text/java'+c;d.async=true;
    a=b.getElementsByTagName(c)[0];a.parentNode.insertBefore(d,a);
    })();
</script>



<!-- Adobe Marketing Cloud Tag Loader Code-->






    <script type="text/javascript">
        // amc.on('load', function (event, data) {
        $(document).ready(function(){
            setTimeout(function(){
                MetaC.checkOmniEvents();
            }, 300);
        });
        // });
    </script>






<script type="text/javascript">

    dwVars = {"siteId":"50","onId":"12456","ptId":"6045","ctype":"entitytype;entityid","cval":"movie;500252"};
    if (typeof DW == "object"){
        DW.pageParams = dwVars;
        DW.regSilo = '12';
        DW.clear();
    }
</script>




<script>
    var cbsiApexGlobal = {
        'SITE': dwVars.siteId,
        'NODE': dwVars.onId,
        'PTYPE':dwVars.ptId
    };
</script>






<script>
    var _gaq = _gaq || [];
    _gaq.push(['_setAccount', 'UA-22577913-5']);
    _gaq.push(['_setCustomVar',1,'PageType',dwVars.ptId,3]);
    _gaq.push(['_trackPageview']);
    _gaq.push(['_trackPageLoadTime']);
    _gaq.push(['_setAllowLinker', true]);
    _gaq.push(['nT._setAccount', 'UA-27653683-1']);
    _gaq.push(['nT._setAllowLinker', true]);
    _gaq.push(['nT._setSampleRate', '1']);
    _gaq.push(['nT._trackPageview']);

    (function() {
        var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
        ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
        var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
    })();
</script>



<div id="fb-root" class=" fb_reset"><div style="position: absolute; top: -10000px; height: 0px; width: 0px;"><div><iframe name="fb_xdm_frame_http" frameborder="0" allowtransparency="true" allowfullscreen="true" scrolling="no" id="fb_xdm_frame_http" aria-hidden="true" title="Facebook Cross Domain Communication Frame" tabindex="-1" src="http://staticxx.facebook.com/connect/xd_arbiter/r/bz-D0tzmBsw.js?version=42#channel=f654a175f6b1d&amp;origin=http%3A%2F%2Fwww.metacritic.com" style="border: none;"></iframe><iframe name="fb_xdm_frame_https" frameborder="0" allowtransparency="true" allowfullscreen="true" scrolling="no" id="fb_xdm_frame_https" aria-hidden="true" title="Facebook Cross Domain Communication Frame" tabindex="-1" src="https://staticxx.facebook.com/connect/xd_arbiter/r/bz-D0tzmBsw.js?version=42#channel=f654a175f6b1d&amp;origin=http%3A%2F%2Fwww.metacritic.com" style="border: none;"></iframe></div></div><div style="position: absolute; top: -10000px; height: 0px; width: 0px;"><div></div></div></div>
<script>
    window.fbAsyncInit = function() {
        FB.init({
            appId      : '123113677890173',
            version    : 'v2.6',
            channelUrl : 'http://www.metacritic.com/static/fbchannel.html',
            status     : true,
            xfbml      : true,
            cookie     : true
            });
         MetaC.FB.initialized();
        };

    (function(d, s, id){
        var js, fjs = d.getElementsByTagName(s)[0];
        if (d.getElementById(id)) {return;}
        js = d.createElement(s); js.id = id;
        js.src = "//connect.facebook.net/en_US/sdk.js";
        fjs.parentNode.insertBefore(js, fjs);
    }(document, 'script', 'facebook-jssdk'));

</script>



<script>
    window.twttr = (function (d,s,id) {
      var t, js, fjs = d.getElementsByTagName(s)[0];
      if (d.getElementById(id)) return; js=d.createElement(s); js.id=id;
      js.src="https://platform.twitter.com/widgets.js"; fjs.parentNode.insertBefore(js, fjs);
      return window.twttr || (t = { _e: [], ready: function(f){ t._e.push(f) } });
    }(document, "script", "twitter-wjs"));

    twttr.ready(function (twttr) {
        MetaC.Twitter.initialized();
    });
</script>






<script>
    /* display the google ads now that the html is finished processing */
    googletag.cmd.push(function(){
        MetaC.displayAds();
    });
</script>



<script>


    if ( window._taboola && window.mcwait_taboola == null ) {
        _taboola.push({flush: true});
    }

</script>





    <script>
    	if (typeof cbsiLoadOffer == "function"){
                cbsiLoadOffer(cbsiApexGlobal,1000);
        }
    </script>

</div>

<script type="text/javascript">window.NREUM||(NREUM={});NREUM.info={"beacon":"bam.nr-data.net","licenseKey":"860f7644b8","applicationID":"2033002","transactionName":"MgQEZ0dYCxEAVRBbDQtOJUZGTQoPTnsLRAsAMRRcUUwGFlsMMUEHFzMDRVxcEhE=","queueTime":0,"applicationTime":1535,"atts":"HkMTEQ9CGE5DV0YIGRgc","errorBeacon":"bam.nr-data.net","agent":""}</script>


<div id="tbl-aug-kbpbv7" class="trc_popover_aug_container"><div id="tbl-aug-qnhk7e" class="trc_popover_aug_container"><div id="tbl-aug-u0wme" class="trc_popover_aug_container"><div class=" trc_popover trc_popover_fade trc_bottom "><div class=" trc_popover_arrow "></div><iframe frameborder="0" scrolling="no" src="javascript:void(0)" style="width: 100%;"></iframe></div></div></div></div><script type="text/javascript" src="//secure-us.imrworldwide.com/v60.js"></script><div id="ZN_3V23D21MC1uQcLj"></div><div id="hover_div" class="hover_div" style="display: none;"><div class="hover_arrow"></div><div class="hover_content"></div></div><form class="trc-hidden" target="tb-trc-transportFrame-8566" method="post" action="http://trc.taboola.com/cbsinteractive-metacritic/log/3/available" style="display: none;"><input name="ri" type="hidden" value="fed60bf57c9997da6056ccf7f4aca6d5"><input name="sd" type="hidden" value="v2_3ceee8f23a711aa3d30165e2ac39c1c7_8c0ecf1c-f135-4f0e-82c4-1ed2e146c0d9_1468819274_1468819532_CIi3jgYQysw_GKuP6OPfKiAO"><input name="ui" type="hidden" value="8c0ecf1c-f135-4f0e-82c4-1ed2e146c0d9"><input name="pi" type="hidden" value="/movie/spider-man-3/user-reviews"><input name="wi" type="hidden" value="5670515232554658479"><input name="pt" type="hidden" value="other"><input name="vi" type="hidden" value="1468819703723"><input name="li" type="hidden" value="rbox-o2m"><input name="utm" type="hidden" value="15,2571,2657,4159"><input name="df" type="hidden" value="1"><input name="ppb" type="hidden" value="CO0D"><input name="cpb" type="hidden" value="EhgyMTgtMS1SRUxFQVNFLSR7dmVyc2lvbn0YlQ0gACoZaGsudGFib29sYXN5bmRpY2F0aW9uLmNvbTIId2F0ZXI2MDc"><input name="tim" type="hidden" value="13:28:26.076"><input name="id" type="hidden" value="8566"><input name="llvl" type="hidden" value="1"><input name="cv" type="hidden" value="218-1-RELEASE-${version}"><input name="fil" type="hidden" value="[{&quot;tii&quot;:&quot;~~V1~~3523664523704351989~~ZpbVe6W9qCaTM85gTQ4zGQ1mRNi-6uOq-mUipAV2orqroxI4gj4mYltvAHkrZTd8DdeU8ba3ruU7lSYoOY4RpQ&quot;,&quot;tipt&quot;:&quot;SP&quot;,&quot;tit&quot;:&quot;text&quot;,&quot;tids&quot;:&quot;a&quot;},{&quot;tii&quot;:&quot;~~V1~~-4082193693269660077~~jdgxVNRz2M4WEPhjV2BJ_5cP646jYXmr5TNqtyO4Cy7ncqLhrdnGGMFmoKiIRgNLDdeU8ba3ruU7lSYoOY4RpQ&quot;,&quot;tipt&quot;:&quot;SP&quot;,&quot;tit&quot;:&quot;text&quot;,&quot;tids&quot;:&quot;a&quot;},{&quot;tii&quot;:&quot;~~V1~~-2475962748955690044~~m3hHddpGqzUZHsLUiHOcyJRo1UsfHf0-1O2i3xKxtb7-lYxK6Q0-ymztisPntpsvDdeU8ba3ruU7lSYoOY4RpQ&quot;,&quot;tipt&quot;:&quot;SP&quot;,&quot;tit&quot;:&quot;text&quot;,&quot;tids&quot;:&quot;a&quot;},{&quot;tii&quot;:&quot;~~V1~~-7778055205621534399~~jw--fJuG7vhZxdC6zHYS9Kg1WJ_KeLT2Keli_siwgoDPRrc-3twzVX224nkWIeszDdeU8ba3ruU7lSYoOY4RpQ&quot;,&quot;tipt&quot;:&quot;SP&quot;,&quot;tit&quot;:&quot;text&quot;,&quot;tids&quot;:&quot;a&quot;},{&quot;tii&quot;:&quot;~~V1~~-5558615715055156430~~QcTc8uen571xe6I9_3lhVAgIrTpT6rY3xu-NfoPw2LfnlCt6P0Yrtl47DRNO5TKYDdeU8ba3ruU7lSYoOY4RpQ&quot;,&quot;tipt&quot;:&quot;SP&quot;,&quot;tit&quot;:&quot;text&quot;,&quot;tids&quot;:&quot;a&quot;},{&quot;tii&quot;:&quot;~~V1~~-8037926977397850505~~aPSn5BEVxLFPAKHq1kiFW024_cCh-zl-C3OzNwjQFx4KmXK3Gj4qu0G0HfPmc5fQDdeU8ba3ruU7lSYoOY4RpQ&quot;,&quot;tipt&quot;:&quot;SP&quot;,&quot;tit&quot;:&quot;text&quot;,&quot;tids&quot;:&quot;a&quot;}]"></form><span><iframe class="trc-hidden" id="tb-trc-transportFrame-8566" name="tb-trc-transportFrame-8566" width="0" height="0" style="display:none"></iframe></span><form class="trc-hidden" target="tb-trc-transportFrame-7235" method="post" action="http://trc.taboola.com/cbsinteractive-metacritic/log/3/available" style="display: none;"><input name="ri" type="hidden" value="7780110117524079ad9066e5a7e4b2d4"><input name="sd" type="hidden" value="v2_3ceee8f23a711aa3d30165e2ac39c1c7_8c0ecf1c-f135-4f0e-82c4-1ed2e146c0d9_1468819274_1468819532_CIi3jgYQysw_GKuP6OPfKiAO"><input name="ui" type="hidden" value="8c0ecf1c-f135-4f0e-82c4-1ed2e146c0d9"><input name="pi" type="hidden" value="/movie/spider-man-3/user-reviews"><input name="wi" type="hidden" value="5670515232554658479"><input name="pt" type="hidden" value="other"><input name="vi" type="hidden" value="1468819703723"><input name="li" type="hidden" value="rbox-o2m"><input name="utm" type="hidden" value="15,2571,2657,4159"><input name="df" type="hidden" value="1"><input name="ppb" type="hidden" value="CMQG"><input name="cpb" type="hidden" value="EhgyMTgtMS1SRUxFQVNFLSR7dmVyc2lvbn0YlQ0gACoZaGsudGFib29sYXN5bmRpY2F0aW9uLmNvbTIId2F0ZXI2MDc"><input name="tim" type="hidden" value="13:28:26.278"><input name="id" type="hidden" value="7235"><input name="llvl" type="hidden" value="1"><input name="cv" type="hidden" value="218-1-RELEASE-${version}"><input name="fil" type="hidden" value="[{&quot;tii&quot;:&quot;~~V1~~-4082193693269660077~~jdgxVNRz2M4WEPhjV2BJ_5cP646jYXmr5TNqtyO4Cy7sBxIeYKC_jpMSMGAeWdwJpaplo213-RuxUXSUrzOFNA&quot;,&quot;tipt&quot;:&quot;SP&quot;,&quot;tit&quot;:&quot;text&quot;,&quot;tids&quot;:&quot;a&quot;},{&quot;tii&quot;:&quot;~~V1~~-2475962748955690044~~m3hHddpGqzUZHsLUiHOcyJRo1UsfHf0-1O2i3xKxtb6TLmAL-VpKWSEJMZDbmcjWpaplo213-RuxUXSUrzOFNA&quot;,&quot;tipt&quot;:&quot;SP&quot;,&quot;tit&quot;:&quot;text&quot;,&quot;tids&quot;:&quot;a&quot;},{&quot;tii&quot;:&quot;~~V1~~-7778055205621534399~~jw--fJuG7vhZxdC6zHYS9Kg1WJ_KeLT2Keli_siwgoDmw8EK7J7MiIhXTT0y10fwpaplo213-RuxUXSUrzOFNA&quot;,&quot;tipt&quot;:&quot;SP&quot;,&quot;tit&quot;:&quot;text&quot;,&quot;tids&quot;:&quot;a&quot;},{&quot;tii&quot;:&quot;~~V1~~-5558615715055156430~~QcTc8uen571xe6I9_3lhVAgIrTpT6rY3xu-NfoPw2LfgCv9nLWD1rvzBRY97cGRkpaplo213-RuxUXSUrzOFNA&quot;,&quot;tipt&quot;:&quot;SP&quot;,&quot;tit&quot;:&quot;text&quot;,&quot;tids&quot;:&quot;a&quot;}]"></form><span><iframe class="trc-hidden" id="tb-trc-transportFrame-7235" name="tb-trc-transportFrame-7235" width="0" height="0" style="display:none"></iframe></span><div class="YAD-INSTR yad-empty" style="display:none !important"><iframe frameborder="0" width="100%" height="0" style="display: none;" src="https://s.yimg.com/uq/syndication/yad-iframe.b5896bc.html" allowtransparency="true"></iframe></div><iframe id="rufous-sandbox" scrolling="no" frameborder="0" allowtransparency="true" allowfullscreen="true" style="position: absolute; visibility: hidden; display: none; width: 0px; height: 0px; padding: 0px; border: none;"></iframe><iframe id="destination_publishing_iframe_cbsi_0" src="http://fast.cbsi.demdex.net/dest5.html?d_nsid=0#http%3A%2F%2Fwww.metacritic.com%2Fmovie%2Fspider-man-3%2Fuser-reviews%3Fpage%3D1" style="display: none; width: 0px; height: 0px;" class="aamIframeLoaded"></iframe><form class="trc-hidden" target="tb-trc-transportFrame-5857" method="post" action="http://trc.taboola.com/cbsinteractive-metacritic/log/3/visible" style="display: none;"><input name="ri" type="hidden" value="fed60bf57c9997da6056ccf7f4aca6d5"><input name="sd" type="hidden" value="v2_3ceee8f23a711aa3d30165e2ac39c1c7_8c0ecf1c-f135-4f0e-82c4-1ed2e146c0d9_1468819274_1468819532_CIi3jgYQysw_GKuP6OPfKiAO"><input name="ui" type="hidden" value="8c0ecf1c-f135-4f0e-82c4-1ed2e146c0d9"><input name="pi" type="hidden" value="/movie/spider-man-3/user-reviews"><input name="wi" type="hidden" value="5670515232554658479"><input name="pt" type="hidden" value="other"><input name="vi" type="hidden" value="1468819703723"><input name="li" type="hidden" value="rbox-o2m"><input name="il" type="hidden" value=""><input name="sil" type="hidden" value="~~V1~~3523664523704351989~~ZpbVe6W9qCaTM85gTQ4zGQ1mRNi-6uOq-mUipAV2orqroxI4gj4mYltvAHkrZTd8DdeU8ba3ruU7lSYoOY4RpQ,~~V1~~-4082193693269660077~~jdgxVNRz2M4WEPhjV2BJ_5cP646jYXmr5TNqtyO4Cy7ncqLhrdnGGMFmoKiIRgNLDdeU8ba3ruU7lSYoOY4RpQ,~~V1~~-2475962748955690044~~m3hHddpGqzUZHsLUiHOcyJRo1UsfHf0-1O2i3xKxtb7-lYxK6Q0-ymztisPntpsvDdeU8ba3ruU7lSYoOY4RpQ"><input name="ilt" type="hidden" value=""><input name="navil" type="hidden" value=""><input name="silt" type="hidden" value="text,text,text"><input name="ntil" type="hidden" value=""><input name="ntilt" type="hidden" value=""><input name="navilt" type="hidden" value=""><input name="niltp" type="hidden" value=""><input name="siltp" type="hidden" value="bills-blog,plariumspartaensc,stormfall-en-sc"><input name="naviltp" type="hidden" value=""><input name="ppb" type="hidden" value="CO0D"><input name="cpb" type="hidden" value="EhgyMTgtMS1SRUxFQVNFLSR7dmVyc2lvbn0YlQ0gACoZaGsudGFib29sYXN5bmRpY2F0aW9uLmNvbTIId2F0ZXI2MDc"><input name="tim" type="hidden" value="13:28:30.447"><input name="id" type="hidden" value="5857"><input name="llvl" type="hidden" value="1"><input name="cv" type="hidden" value="218-1-RELEASE-${version}"><input name="fil" type="hidden" value="[{&quot;tii&quot;:&quot;~~V1~~3523664523704351989~~ZpbVe6W9qCaTM85gTQ4zGQ1mRNi-6uOq-mUipAV2orqroxI4gj4mYltvAHkrZTd8DdeU8ba3ruU7lSYoOY4RpQ&quot;,&quot;tipt&quot;:&quot;SP&quot;,&quot;tit&quot;:&quot;text&quot;,&quot;tids&quot;:&quot;vp&quot;},{&quot;tii&quot;:&quot;~~V1~~-4082193693269660077~~jdgxVNRz2M4WEPhjV2BJ_5cP646jYXmr5TNqtyO4Cy7ncqLhrdnGGMFmoKiIRgNLDdeU8ba3ruU7lSYoOY4RpQ&quot;,&quot;tipt&quot;:&quot;SP&quot;,&quot;tit&quot;:&quot;text&quot;,&quot;tids&quot;:&quot;vp&quot;},{&quot;tii&quot;:&quot;~~V1~~-2475962748955690044~~m3hHddpGqzUZHsLUiHOcyJRo1UsfHf0-1O2i3xKxtb7-lYxK6Q0-ymztisPntpsvDdeU8ba3ruU7lSYoOY4RpQ&quot;,&quot;tipt&quot;:&quot;SP&quot;,&quot;tit&quot;:&quot;text&quot;,&quot;tids&quot;:&quot;vp&quot;},{&quot;tii&quot;:&quot;~~V1~~-7778055205621534399~~jw--fJuG7vhZxdC6zHYS9Kg1WJ_KeLT2Keli_siwgoDPRrc-3twzVX224nkWIeszDdeU8ba3ruU7lSYoOY4RpQ&quot;,&quot;tipt&quot;:&quot;SP&quot;,&quot;tit&quot;:&quot;text&quot;,&quot;tids&quot;:&quot;nvp&quot;},{&quot;tii&quot;:&quot;~~V1~~-5558615715055156430~~QcTc8uen571xe6I9_3lhVAgIrTpT6rY3xu-NfoPw2LfnlCt6P0Yrtl47DRNO5TKYDdeU8ba3ruU7lSYoOY4RpQ&quot;,&quot;tipt&quot;:&quot;SP&quot;,&quot;tit&quot;:&quot;text&quot;,&quot;tids&quot;:&quot;nvp&quot;},{&quot;tii&quot;:&quot;~~V1~~-8037926977397850505~~aPSn5BEVxLFPAKHq1kiFW024_cCh-zl-C3OzNwjQFx4KmXK3Gj4qu0G0HfPmc5fQDdeU8ba3ruU7lSYoOY4RpQ&quot;,&quot;tipt&quot;:&quot;SP&quot;,&quot;tit&quot;:&quot;text&quot;,&quot;tids&quot;:&quot;nvp&quot;}]"></form><span><iframe class="trc-hidden" id="tb-trc-transportFrame-5857" name="tb-trc-transportFrame-5857" width="0" height="0" style="display:none"></iframe></span></body>"""


soup = BeautifulSoup(html,'html.parser',from_encoding='utf-8')
links = soup.find_all('a', class_='page_num', href=re.compile(r"user-reviews\?page=\d$"))
for link in links:
    print link['href']

names = soup.select(".name > span")
scores = soup.select(".review_grade > .user")
dates = soup.select(".review_critic > .date")
user_reviews = []
html_user_reviews = soup.select(".review_body > span")
for review in html_user_reviews:
    user_reviews.append( review.select(".blurb_expanded")[0].string if review.string == None else review.string )
page_claws = []
for n,s,d,rw in zip(names, scores, dates, user_reviews):
    page_claws.append([n.string, s.string, d.string, rw])

for claw in page_claws:
    print claw