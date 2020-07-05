#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 22:10:42 2020

@author: cpprhtn
"""


'''

X-ray 예측결과가 암일 경우

requests로 html을 확인했으나 
크롤링 해야하는 논문은
특정 주소로 이어지기때문에
사용불가 라는 결론이 나옴


selenium을 사용해서 다시 만들어볼 예정
'''
import requests 
urlF = "https://journals.sagepub.com/action/doSearch?AllField=" #front

Prediction = "cancer"

urlB = "&access=18" #back



url = urlF + Prediction + urlB

rs = requests.post(url) 

rs_code = rs.status_code 

if int(rs_code) == 200 :
    print("Okay") 
    rs_text = rs.text 
    print(rs_text) 
    
else : 
    print(rs_code) 
    print("Fail")​
    
'''
<!DOCTYPE html>
<html lang="en" class="pb-page" data-request-id="bfc67bc2-e585-4aa2-98a8-1c4c6de38c3c"><head data-pb-dropzone="head">

<script>
    var dataLayer = dataLayer ||[];
    dataLayer.push({"site":{"environment":"live","platform":"responsive-web"},"page":{"title":"","type":"advanced-search"},"user":{"action":"doSearch","type":[],"loginStatus":false,"authentication":false,"authenticationType":"[]","institutionType":"[]","institution":[]}});
</script>
<script>(function (w, d, s, l, i) {
            w[l] = w[l] || [];
            w[l].push(
                    {'gtm.start': new Date().getTime(), event: 'gtm.js'}
            );
            var f = d.getElementsByTagName(s)[0],
                    j = d.createElement(s), dl = l != 'dataLayer' ? '&l=' + l : '';
            j.async = true;
            j.src =
                    '//www.googletagmanager.com/gtm.js?id=' + i + dl;
            f.parentNode.insertBefore(j, f);
        })(window, document, 'script', 'dataLayer', 'GTM-5M58KS');</script>

<meta name="pbContext" content=";website:website:sage;wgroup:string:SAGE Publication Websites;pageGroup:string:Search Flow;page:string:Advanced Search" />
<meta name="twitter:card" content="summary_large_image">
<meta property="og:locale" content="en_US">
<meta charset="UTF-8">
<meta name="robots" content="noarchive" />
<meta name="pb-robots-disabled">
<meta property="og:title" content="Advanced Search: SAGE Journals" />
<meta property="og:type" content="article">
<meta property="og:url" content="https://journals.sagepub.com/action/doSearch?prg140729=d2e0b346-99b3-4538-8243-2fbb08871bd0" />
<meta property="og:image:width" content="600" />
<meta property="og:image:height" content="900" />
<meta property="og:site_name" content="SAGE Journals" />
<meta property="og:description" content="Use advanced filters to search SAGE Journals by title, abstract, keyword, date, author, affiliation, journal and citation." />
<title>Advanced Search: SAGE Journals</title>
<meta name="description" content="Use advanced filters to search SAGE Journals by title, abstract, keyword, date, author, affiliation, journal and citation.">
<link rel="stylesheet" type="text/css" href="/wro/iwvr~product.css"><link rel="stylesheet" type="text/css" href="/pb/css/t1591703075933-v1590560150000/head_1_6_7.css" id="pb-css" data-pb-css-id="t1591703075933-v1590560150000/head_1_6_7.css" />
<script type="text/javascript">
    if (window.location.hash && window.location.hash == '#_=_') {
        window.location.hash = '';
    }
</script>
<script type="text/javascript" src="/wro/iwvr~product.js"></script>
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<link rel="preload" type="text/css" href="/pb-assets/CSS/global-1592217535473.css" as="style">
<link rel="preload" type="text/css" href="//widgets.sagepub.com/bookshelf/css/all.css" as="style" crossorigin>
<link rel="preload" type="text/javascript" href="/pb-assets/JS/xhrCatch-1564476093570.js" as="script">
<link rel="preload" type="text/javascript" href="/pb-assets/JS/js.cookie.min-1517227616353.js" as="script">
<link rel="preload" type="text/javascript" href="/pb-assets/ads/insticator-ads-1593113482667.js" as="script">
<link rel="preload" type="text/javascript" href="/pb-assets/JS/jquery.actual.min-1513079278967.js" as="script">
<link rel="preload" type="text/javascript" href="/pb-assets/JS/imagesloaded.pkgd.min-1523539547607.js" as="script">
<link rel="preload" type="text/javascript" href="/pb-assets/JS/listExpander-1580296423817.js" as="script">
<link rel="preload" type="text/javascript" href="/pb-assets/JS/listExpander-ie-1580296424420.js" as="script">
<link rel="preload" type="text/javascript" href="/pb-assets/JS/societiesModal-1560270859740.js" as="script">
<link rel="preload" type="text/javascript" href="/pb-assets/JS/sj-utils-1587639260120.js" as="script">
<link rel="preload" type="text/javascript" href="/pb-assets/JS/portalAutomation-1593092752157.js" as="script">
<link rel="preload" type="text/javascript" href="/pb-assets/JS/authorsPatch-1542815689637.js" as="script">
<link rel="preload" type="text/javascript" href="/pb-assets/microsite/lib/microsite-dfp-1592463885070.js" as="script">
<link rel="preload" type="text/javascript" href="/pb-assets/JS/dfp-1593528806513.js" as="script">
<link rel="preconnect" href="//stats.g.doubleclick.net" crossorgin>
<link rel="preconnect" href="//tpc.googlesyndication.com" crossorgin>
<link rel="preconnect" href="//pagead2.googlesyndication.com" crossorgin>
<link rel="preconnect" href="//securepubads.g.doubleclick.net" crossorgin>
<link rel="preconnect" href="//cdn.ampproject.org" crossorgin>
<link rel="preconnect" href="//api.altmetric.com" crossorgin>
<link rel="preconnect" href="//s7.addthis.com" crossorgin>
<link rel="preconnect" href="//m.addthis.com" crossorgin>
<link rel="preconnect" href="//www.deepdyve.com" crossorgin>
<link rel="preconnect" href="//sage.msgfocus.com" crossorgin>
<link rel="preconnect" href="//widgets.sagepub.com" crossorgin>
<link rel="preconnect" href="//www.medtargetsystem.com" crossorgin>
<link rel="preconnect" href="//api.rlcdn.com" crossorgin>
<link rel="preconnect" href="//match.adsrvr.org" crossorigin>
<link rel="preconnect" href="//scholar.google.com" crossorigin>
<link rel="preconnect" href="//googleads.g.doubleclick.net" crossorigin>
<link rel="preconnect" href="//snap.licdn.com" crossorigin>
<link rel="preconnect" href="//remote.captcha.com" crossorigin>
<link rel="preconnect" href="//static.hotjar.com" crossorigin>
<link rel="preconnect" href="//z.moatads.com" crossorigin>
<link rel="preconnect" href="//www.google-analytics.com" crossorigin>
<link rel="preconnect" href="//www.googleadservices.com" crossorigin>
<link rel="preconnect" href="//adservice.google.com" crossorigin>
<link rel="preconnect" href="//cdnjs.cloudflare.com" crossorigin>
<link rel="preconnect" href="//dr15zo9o33078.cloudfront.net" crossorigin>
<link rel="dns-prefetch" href="//sadmin.brightcove.com">
<link rel="dns-prefetch" href="//w.usabilla.com">
<link rel="dns-prefetch" href="//rum-static.pingdom.net">
<link rel="dns-prefetch" href="//rum-collector-2.pingdom.net">
<link rel="dns-prefetch" href="//crossmark-cdn.crossref.org">
<script>
if (typeof jQuery==='undefined') {
	document.write(unescape('\x3Clink rel="stylesheet" type="text/css" href="/wro/ih5o/product.css"\x3E'));
	document.write(unescape('\x3Cscript src="/wro/ih5o/product.js"\x3E\x3C/script\x3E'));
}
</script>
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" type="text/css" href="/pb-assets/CSS/global-1592217535473.css">
<link rel="stylesheet" type="text/css" href="/pb-assets/CSS/temp-1592217435280.css">
<link rel="prefetch" type="text/css" href="/pb-assets/CSS/ecomm-1575892228040.css" as="style">
<link rel="prefetch" type="text/css" href="/pb-assets/CSS/browse-1517329929647.css" as="style">
<link rel="prefetch" type="text/css" href="/pb-assets/CSS/profile-pages-1545148174810.css" as="style">
<link rel="apple-touch-icon" href="/pb-assets/Icons/sj-apple-touch-1513073710420.png">
<meta property="og:image" content="/pb-assets/Images/SJ_Twitter_Card-1557144152440.jpg">
<meta name="google-site-verification" content="6b_U8gTbwxPAJSSIOBxO9mKsWVht9WAMuijMWNDwNCs" />
<script>
//if ($('meta[property="og:image"]').length===0)
//	$('meta[property="fallback:image"]').attr('property','og:image');
// Remove HTML tag-items from the page tile
//document.title=document.title.replace(/<\/?[^>]+(>|$)/g, "");
function CM8ShowAd(ph) {} // fallback function "masking" CM8
var googletag = googletag || {};
googletag.cmd = googletag.cmd || [];
var dfpSlotsReady=false;
var globalAdParams={
portal: {
	name: 'Portal',
	slot: 'portal_site.home',
	code: '1530873931903'
},
search: {
	name: 'Search',
	slot: 'portal_site.search',
	code: '1530874010820'
},
browse: {
	name: 'Browse',
	slot: 'portal_site.browse',
	code: '1530874064610'
}
};
var journalAdParams = {
	serviceName: '',
	dfp_slot: '',
	alpha_code: '',
	alt_code: ''
};
var insticatorAdsEnabled=false;
var hcpContext;
</script>
<script src='//dr15zo9o33078.cloudfront.net/script/render-header.js'></script>
<script src="/pb-assets/JS/xhrCatch-1564476093570.js"></script>
<script src="/pb-assets/JS/js.cookie.min-1517227616353.js"></script>
<script src="/pb-assets/ads/insticator-ads-1593113482667.js"></script>
<script src="/pb-assets/ads/doceree-ads-1593077689363.js"></script>
<script data-cfasync="false" src="/pb-assets/JS/jquery.actual.min-1513079278967.js"></script>
<script data-cfasync="false" src="/pb-assets/JS/imagesloaded.pkgd.min-1523539547607.js"></script>
<script data-cfasync="false" src="/pb-assets/JS/listExpander-1580296423817.js"></script>
<script data-cfasync="false" src="/pb-assets/JS/listExpander-ie-1580296424420.js"></script>
<script data-cfasync="false" src="/pb-assets/JS/societiesModal-1560270859740.js"></script>
<script data-cfasync="false" src="/pb-assets/JS/sj-utils-1587639260120.js"></script>
<script data-cfasync="false" src="/pb-assets/JS/portalAutomation-1593092752157.js"></script>
<script src="/pb-assets/JS/authorsPatch-1542815689637.js"></script>
<script src="/pb-assets/microsite/lib/microsite-dfp-1592463885070.js"></script>
<script src="/pb-assets/JS/dfp-1593528806513.js"></script>
<script>
if (inJournalScope()) 
	initJournalDfp();
else if (inMicrositeScope()) 
	initMicrositeDfp();
else 
	initGlobalDfp();
</script>
<link rel="canonical" href="https://journals.sagepub.com/action/doSearch?prg140729=d2e0b346-99b3-4538-8243-2fbb08871bd0">
<script>var _prum=[['id','5847762c1e20722da47b23c6'],['mark','firstbyte',(new Date()).getTime()]];(function(){var s=document.getElementsByTagName('script')[0],p=document.createElement('script');p.async='async';p.src='//rum-static.pingdom.net/prum.min.js';s.parentNode.insertBefore(p,s);})();</script></head>
<body class="pb-ui">
<div class="totoplink">
<a id="skiptocontent" class="skiptocontent" href="#" tabindex="1" title="Skip to Content" aria-live="polite">Skip to main content</a>
</div>
<noscript>
    <iframe src="//www.googletagmanager.com/ns.html?id=GTM-5M58KS"
            height="0" width="0" style="display:none;visibility:hidden"></iframe>
</noscript>
<script type="text/javascript">


        function initSelector(element){
            $('.skiptocontent').removeAttr("href");
            $( element ).parent().before( "<a id=\"top\"></a>" );
            window.location.hash = '#top';
            $(window).scrollTop($("#top").offset().top-100);
            history.pushState("", document.title, window.location.pathname + window.location.search);
        }


        $('#skiptocontent').click(function (e) {

            var code;
            try {
                code = (window.event) ? window.event.keyCode : event.which;
            }
            catch(err) {
                code = e.keyCode || e.which;
            }

            //click Enter

                    var mainPageId=$("#main-page-content").text();
                if(mainPageId){
                    initSelector('#main-page-content');
                }else{

                    var firstH1=$('h1:first').text();
                    if(firstH1){
                        initSelector('h1:first');
                    }else{
                       $('#skiptocontent').css('display','none');
                    }
                }


        });


</script>
<div id="pb-page-content" data-ng-non-bindable>
<div data-pb-dropzone="main" data-pb-dropzone-name="Main">

<div class="widget page-main-content none  widget-none  widget-compact-all" id="dea397f8-1087-4823-917e-a9dd6b971630">
<div class="wrapped ">
<div class="widget-body body body-none  body-compact-all"><main role="main" data-pb-dropzone="contents">
<div class="widget pageHeader none  widget-none  widget-compact-all" id="c44c1c4b-af27-4df5-9ca6-c88cc63f1286">
<div class="wrapped ">
<div class="widget-body body body-none  body-compact-all"><header class="page-header">
<div data-pb-dropzone="main">
<div class="widget literatumAd alignCenter headerLeaderBoard widget-none  widget-compact-all" id="99656816-01bb-403c-8664-49e0ec22c457">
<div class="wrapped ">
<div class="widget-body body body-none  body-compact-all"><div class="pb-ad">
<script>showDfpAd(0)</script>
</div></div>
</div>
</div>
<div class="widget responsive-layout none portalHeaderMobile stick-it-mobile widget-none  widget-compact-all" id="919864a0-5dfa-48e3-b495-8a34f8caf8d6">
<div class="wrapped " id='portalHeaderMobileID'>
<div class="widget-body body body-none  body-compact-all"><div class="container-fluid">
<div class="row row-md  ">
<div class="col-md-1-1 ">
<div class="contents" data-pb-dropzone="contents0">

<div class="widget cookiePolicy none mobileOnly widget-none  widget-compact-all" id="29f0cfde-3430-44a6-a30f-6148b86c754f">
<div class="wrapped ">
<div class="widget-body body body-none  body-compact-all"><div id="cookieBannerMobile" class="cookieBanner">
<h4 class="b-header">Cookies Notification</h4>
<div class="b-body" tabindex="0" style="padding-bottom: 5px;">
This site uses cookies. By continuing to browse
the site you are agreeing to our use of cookies.
<a href="/page/cookie-policy" title="Learn more about cookies">Find out more.</a>
<br>
<input id="accept-cookie-policy-mobile" type="button" title="Dismiss cookie message" value="Accept" />
</div>
</div>
<script>
$('.page-main-content').addClass('with-mobile-cookie-banner');
$('#accept-cookie-policy-mobile').click(function(){
    $('.page-main-content').removeClass('with-mobile-cookie-banner');
});
</script>
<script type="text/javascript">
    $("#accept-cookie-policy-mobile").click(function() {
        $.get('/action/cookiePolicy?response=accept', function(data) {
            $(".cookiePolicy").remove();
        });

    });
</script></div>
</div>
</div>
<div class="widget general-html-asset none  widget-none  widget-compact-all" id="74dc980e-de8a-4463-9a84-61f907f1e1ab">
<div class="wrapped ">
<div class="widget-body body body-none  body-compact-all"><div class="burgerContainer" onclick="portalMobileMenusDisplay(); return false;">
<a href="#">
<img src="/pb-assets/Images/hamburger-menu-1513073728590.svg" alt="Menus" title="Menus">
</a>
</div>
<div class="mobileHeader">
<div class="leftAlignement">
</div>
<div class="smallSAGELogoContainer">
<a href="/">
<img src="/pb-assets/Images/SJ-logo-1513073727423.svg" alt="SAGE Journals">
</a>
</div>
<div class="profileContainerMobile" onclick="portalMobileLoginDisplay(); return false;">
<a href="#"><img src="/pb-assets/Images/profile-1513073726673.svg" alt="Profile" title="Profile"><img class="loggedInArrow" src="/pb-assets/Images/Arrow-down-red-small-1498649694847.png" alt="logged-in"></a>
</div>
<div id="mobileSearchButton" tabindex="0" class="searchContainerMobile" onclick="portalMobileSearchDisplay(); return false;">
<a href="#">
<img src="/pb-assets/Images/search-1513073726663.svg" alt="Search" title="Search">
</a>
</div>
</div>
<div id="portalMobileMenusOverlay" onclick="portalMobileMenusDisplay(); return false;"></div></div>
</div>
</div>
<div class="widget layout-frame none  widget-none  widget-compact-all" id="c1522079-3ecc-4088-be29-67e60b4693d6">
<div class="wrapped " id='portalMobileMenus'>
<div class="widget-body body body-none  body-compact-all"><div data-pb-dropzone="contents">
<div class="widget general-html-asset none portalMenus widget-none  widget-compact-all" id="6e98bd07-3ab6-4563-b1ba-857cc8a7ddfc">
<div class="wrapped ">
<h4 class="widget-header header-none  header-compact-all">MENU</h4>
<div class="widget-body body body-none  body-compact-all"><div class="menuXml">
<nav>
<ul class="shadow primaryNav">
<li class="searchButton">
<a href="#" role="button" tabindex="0" onclick="toggleSearchDialog('.portalHeaderContainer .searchButton'); return false;">Search
<img src="/pb-assets/Images/search-1513073726663.svg" alt="search-icon" title="">
</a>
</li>
<li class="">
<a id="portalBrowseLink" href="/action/showPublications">Browse</a>
</li>
<li class="">
<a class="expander" href="#">Resources</a>
<ul>
<li class="">
<a href="https://sagepub.com/journal-author-gateway">Authors</a>
</li>
<li class="">
<a href="https://journalssolutions.sagepub.com/support/home">Librarians</a>
</li>
<li class="">
<a href="https://sagepub.com/journal-editor-gateway">Editors</a>
</li>
<li class="">
<a href="/page/resources/societies">Societies</a>
</li>
</ul>
</li>
<li class="advancedSearchPortal">
<a href="/search/advanced">Advanced Search</a>
</li>
</ul>
</nav>
</div></div>
</div>
</div>
</div></div>
</div>
</div>
</div>
</div>
</div>
</div></div>
</div>
</div>
<div class="widget layout-frame none portalHeaderContainer  stick-it-header widget-none  widget-compact-all" id="da2dfa63-a90d-4940-a652-36aa0f55e2b5">
<div class="wrapped ">
<div class="widget-body body body-none  body-compact-all"><div data-pb-dropzone="contents">
<div class="widget responsive-layout none portalHeader widget-none  widget-compact-all" id="e00da0da-a7b9-4046-ac29-04b0a9b67218">
<div class="wrapped ">
<div class="widget-body body body-none  body-compact-all"><div class="container-fluid">
<div class="row row-md  ">
<div class="col-md-1-1 ">
<div class="contents" data-pb-dropzone="contents0">
<div class="widget general-image none sageLogo widget-none  widget-compact-all" id="26d3e1a0-8c43-4c47-9c58-988e63152cc8">
<div class="wrapped ">
<div class="widget-body body body-none  body-compact-all"><a href="/" title="SAGE Journals">
<img src="/pb-assets/Images/SJ-LOGO-1513073727437.png" alt="SAGE Journals" />
</a></div>
</div>
</div>
<div class="widget general-html-asset none portalMenus widget-none  widget-compact-all" id="342dde64-c493-4c7d-b859-3597e6f52c86">
<div class="wrapped ">
<div class="widget-body body body-none  body-compact-all"><div class="menuXml">
<nav>
<ul class="shadow primaryNav">
<li class="searchButton">
<a href="#" role="button" tabindex="0" onclick="toggleSearchDialog('.portalHeaderContainer .searchButton'); return false;">Search
<img src="/pb-assets/Images/search-1513073726663.svg" alt="search-icon" title="">
</a>
</li>
<li class="">
<a id="portalBrowseLink" href="/action/showPublications">Browse</a>
</li>
<li class="">
<a class="expander" href="#">Resources</a>
<ul>
<li class="">
<a href="https://sagepub.com/journal-author-gateway">Authors</a>
</li>
<li class="">
<a href="https://journalssolutions.sagepub.com/support/home">Librarians</a>
</li>
<li class="">
<a href="https://sagepub.com/journal-editor-gateway">Editors</a>
</li>
<li class="">
<a href="/page/resources/societies">Societies</a>
</li>
</ul>
</li>
<li class="advancedSearchPortal">
<a href="/search/advanced">Advanced Search</a>
</li>
</ul>
</nav>
</div></div>
</div>
</div>
<div data-widget-def="layout-frame" data-widget-id="921d6e4c-dde7-4a4a-940e-e61bceec84b0" class="inlineBlock" data-module-name="login-box" aria-label="Click here to sign in">
<div class="widget layout-frame none portalLoginContainer widget-none  widget-compact-all" id="921d6e4c-dde7-4a4a-940e-e61bceec84b0">
<div class="wrapped " id='portalMobileLogin'>
<div class="widget-body body body-none  body-compact-all"><div data-pb-dropzone="contents">
<div class="widget general-html-asset none  widget-none  widget-compact-all" id="66fe8e60-9b5c-42dc-b5da-3aff92108756">
<div class="wrapped ">
<div class="widget-body body body-none  body-compact-all"><div id="portalMobileLoginOverlay"></div></div>
</div>
</div>
<div class="widget layout-frame none individualLoginContainer widget-none  widget-compact-all" id="8d34d6ab-387d-46cb-a6f8-54b88fb03a37">
<div class="wrapped ">
<div class="widget-body body body-none  body-compact-all"><div data-pb-dropzone="contents">
<div class="widget literatumNavigationLoginBar none portalLoginBar widget-none  widget-compact-all" id="25793432-627d-46a1-8b30-1007ede2e8c2">
<div class="wrapped " id='portalLoginBar'>
<div class="widget-body body body-none  body-compact-all"><div class="sage-login-widget">
<div class="my-profile-col id-person-deactivated" name="">
<img class="user-logo my-profile-logo deactivated" src="/templates/jsp/_style2/_sage/images/Profile.svg" />
<div class="myprofile-label">Sign In</div>
</div>
<div class="institution-col id-institution-deactivated" name="">
<img class="user-logo institution-logo deactivated" src="/templates/jsp/_style2/_sage/images/Institution.svg" title="You are not signed in via an institution" />
<div class="institutionLabel">Institution</div>
</div>
<div class="society-col id-society-deactivated" name="">
<img class="user-logo society-logo deactivated" src="/templates/jsp/_style2/_sage/images/Societies.svg" title="You are not signed in via an societyName" />
<div class="societyLabel">Society</div>
</div>
</div></div>
</div>
</div>
<div class="widget layout-frame none  widget-none  widget-compact-all" id="5c2ac0ea-bc85-4b38-bf75-eae5d52087fa">
<div class="wrapped " id='enhancedLoginPanel'>
<div class="widget-body body body-none  body-compact-all"><div data-pb-dropzone="contents">
<div class="widget general-html-asset none  widget-none  widget-compact-all" id="a49810ce-97fc-49b7-8ada-ec03b1ee007d">
<div class="wrapped ">
<div class="widget-body body body-none  body-compact-all"><script>
function initLoginBox() {
	if (hasPersonIdentity())
		$('.profileContainerMobile img.loggedInArrow').show();
	else {
		$('.profileContainerMobile img.loggedInArrow').hide();
		//$('.myprofile-label').text("Sign In");
	};
	$('#portalLoginBar .sage-login-widget').attr('tabindex', '0');
	$('#portalLoginBar .sage-login-widget').prepend('<span aria-hidden="true" style="min-width:105px;padding-top:15px;">Access Options:</span>');
	$('.sage-login-widget img.user-logo').each(function(){
		//console.log($(this).attr('src'));
		if($(this).attr('src').indexOf('templates')===-1)
			$(this).addClass('bannerImage');
		else
			$(this).removeClass('bannerImage');
	});

	$('div.myprofile-label, div.institutionLabel, div.societyLabel, span.institutionBannerLogo, .lean-library-text img').attr('aria-hidden', 'true');
	
	initMyProfileInfo();
	initInstitutionInfo();
	initSocietyInfo();

	if (inPbEditorMode())
		$('.sage-login-widget').attr('onclick', 'toggleLoginPopup(true);return false;');

	if (isIE()) {
		$("img.user-logo").each(function () {
			let imgUrl = $(this).prop("src");
			if (imgUrl) {
				$(this).css("backgroundImage", 'url(' + imgUrl + ')').addClass("ie-object-fit");
				$(this).prop("src","");
			}
		});
	}
}
</script>
<div id="login-popup" tabindex="0" aria-label="Access Options" role="dialog" aria-modal="true">
<div id="loginbox-header">
<div class="widget general-rich-text none  widget-none  widget-compact-all" id="ab5cfb99-0d5f-4648-abeb-189fc1e5d9e8">
<div class="wrapped ">
<div class="widget-body body body-none  body-compact-all"><div id="rich-text-ab5cfb99-0d5f-4648-abeb-189fc1e5d9e8" class="pb-rich-text">
<h2 style="text-align: center;"><strong><span style="font-family: arial, helvetica, sans-serif; font-size: large;">Access Options</span></strong></h2>
<p style="text-align: center;"><span style="font-family: arial, helvetica, sans-serif; font-size: medium;">You can be signed in via any or all of the methods shown below at the same time.</span></p>
</div></div>
</div>
</div>
</div>
<div id="loginbox-body">
<div class="widget responsive-layout none loginColumns widget-none  widget-compact-all" id="eadd9cf1-2ff3-492f-bd4a-be73f504ad42">
<div class="wrapped ">
<div class="widget-body body body-none  body-compact-all"><div class="container-fluid">
<div class="row row-md  ">
<div class="col-md-1-3 ">
<div class="contents" data-pb-dropzone="contents0">
<div class="widget general-html-asset none login-column widget-none  widget-compact-all" id="fc732953-7d6e-42ae-8639-288f284c5293">
<div class="wrapped ">
<div class="widget-body body body-none  body-compact-all"><h3 class="login-profile" aria-describedby="info-profile">My Profile<span class="login-expander"></span></h3>
<div class="midSection">
<div id="user-login-form">
<div class="login-info" id="info-profile">
<p>Sign in here to access free tools such as favourites and alerts, or to access personal subscriptions</p>
</div>
<div class="mobile-expand">
<div class="widget literatumLoginWidget none  widget-none  widget-compact-all" id="058f11ae-cce1-45d8-9a12-b8a2cc664af7">
<div class="wrapped ">
<div class="widget-body body body-none  body-compact-all"><div class="loginWidget">
<div class="loginDropZone1" data-pb-dropzone="loginDropZone1">
</div>
<div id="login_left">
<form action="/action/doLogin" id="frmLogin" name="frmLogin" method="post"><input type="hidden" name="loginFormId" value="058f11ae-cce1-45d8-9a12-b8a2cc664af7" /><input type="hidden" name="loginUri" value="/action/doSearch?prg140729=d2e0b346-99b3-4538-8243-2fbb08871bd0" /><input type="hidden" name="redirectUri" value="/action/doSearch?prg140729=d2e0b346-99b3-4538-8243-2fbb08871bd0" /><input type="hidden" name="submitViaAJAX" value="true" />
<p>
</p>
<table class="loginForm" summary="">
<tr>
<td role="region" class="error" aria-live="polite">
<span role="alert" class="useAJAX_error" style="display: none;">The email address and/or password entered does not match our records, please check and try again.</span></td>
</tr>
<tr>
<th><label for="login" class="userNameLoginLabel">Email <span class="required-field">(required)</span></label></th>
<td><input id="login" class="textInput" type="text" name="login" value="" size="15" required="true" /></td>
</tr>
<tr>
<th><label for="password" class="passwordLoginLabel">Password <span class="required-field">(required)</span></label></th>
<td><input id="password" class="textInput" type="password" name="password" value="" autocomplete="off" required="true" /></td>
</tr>
<tr>
<td colspan="2"><input id="savePassword" type="checkbox" name="savePassword" value="1" checked="checked" /><label for="savePassword">Remember me</label></td>
</tr>
</table>
<input class="formbutton defButton" role="button" type="submit" name="submit" value="Sign in" tabindex="0" data-item-name="sign-in" aria-label="Sign In" /><br />
<br />
<div id="passwordReminder"><a href="/action/requestResetPassword?redirectUri=">Forgotten your password?</a></div></form>
<script type="text/javascript"><!-- //
function runSearchSetup(){_tmp=document.forms['frmLogin'];if(_tmp){_tmp=_tmp['login'];}};window.onload = runSearchSetup; 
// -->
</script>
</div>
<div id="login_right">
<div class="loginDropZone" data-pb-dropzone="loginDropZone">
</div>
</div>
<div style="clear:both"></div>
</div></div>
</div>
</div>
<div class="register-section topSeparator">
<p style="text-align:left;margin:5px 0">I don't have a profile</p>
<div class="blueGrayButton smallButton">
<a class="register-link" data-item-name="create-profile" role="button" aria-label="Register new account" href="/action/registration">Create Profile</a>
</div>
</div>
</div>
</div>
<div id="user-info">
<div class="bottomSeparator">
<p class="signed-as">I am signed in as:</p>
</div>
<div class="mobile-expand">
<div id="avatar-image">
</div>
<div id="user-name">
</div>
<div id="view-my-account">
<a data-item-name="view-my-account" href="/action/showPreferences?menuTab=AccountInfo">View My Account</a>
</div>
<br>
<div class="logout-section blueGrayButton smallButton topSeparator">
<a class="register-link logOut" data-item-name="logout" href="/action/doLogout?redirectUri=#" role="button" aria-label="Sign out" id="ru-user">Logout</a>
</div>
<br>
</div>
</div>
</div>
<script>
function initMyProfileInfo() {
	$('.id-person-activated>img.user-logo').attr('title', 'You are signed in to your personal profile');
	$('.id-person-deactivated>img.user-logo').attr('title', 'You are not signed in to your personal profile');
	$('form[name="frmLogin"] br').hide();
	$('#user-login-form #passwordReminder').insertBefore('#user-login-form form[name="frmLogin"] tr:last-child');
	$('#ru-user').attr('href', '/action/doLogout?redirectUri='+window.location.href);
	$('#user-login-form input[type="submit"]').attr('aria-label','Sign In to my profile');

	if (hasPersonIdentity()) {
		$('#user-info').show();
		$('#user-login-form').hide();
	}
	else {
		$('#user-info').hide();
		$('#user-login-form').show();
	}

	if ($('#user-name p').length===0){
		let $user=$('#portalLoginBar .my-profile-col.id-person-activated');
		if ($user && $user.attr('name') && $user.attr('name').length>0) {
			$('<p>'+$user.attr('name')+'</p>').appendTo('#user-name');
		}
	}
}
$('#frmLogin input[type="submit"]').click(function() {
	$(this).closest('#frmLogin').find('.loginForm .useAJAX_error').hide();
});
</script></div>
</div>
</div>
<div class="widget general-rich-text none login-instructions widget-none  widget-compact-all widget-border-toggle" id="e9322ee9-2ba1-4166-8ae3-b6dfde7ae567">
<div class="wrapped ">
<div class="widget-body body body-none  body-compact-all body-border-toggle"><div id="rich-text-e9322ee9-2ba1-4166-8ae3-b6dfde7ae567" class="pb-rich-text">
<p>With my free profile I can:</p>
<ul>
<li>Set up&nbsp;<a href="/action/showPreferences?menuTab=favorites">favourite journals</a>&nbsp;and register for&nbsp;<a href="/action/showPreferences?menuTab=Alerts">email alerts</a></li>
<li>List&nbsp;<a href="/search/saved">saved searches</a></li>
<li><a href="/action/showPreferences?menuTab=AccountInfo">Edit account details</a></li>
<li><a href="/action/showPreferences?menuTab=society">Activate personal subscriptions</a>&nbsp;and&nbsp;<a href="/action/showPreferences?menuTab=licenses">access content</a></li>
</ul>
</div></div>
</div>
</div>
</div>
</div>
<div class="col-md-1-3 ">
<div class="contents" data-pb-dropzone="contents1">


<div class="widget general-html-asset none login-column widget-none  widget-compact-all" id="414e61c7-547d-4bd7-b101-7b6264ef1b26">
<div class="wrapped ">
<div class="widget-body body body-none  body-compact-all"><h3 class="login-institution" aria-describedby="info-inst">Institution<span class="login-expander"></span></h3>
<div class="midSection">
<div id="institution-login-form">
<div class="login-info" id="info-inst">
<p>If you have access to journal content via a university, library or employer, sign in here</p>
</div>
<div class="mobile-expand">
<br>
<div class="smallButton redButton shibbolethButton">
<a data-item-name="shibboleth" href="/action/ssostart?redirectUri=" role="button" aria-label="Shibboleth sign in" class="Shibboleth">Shibboleth</a>
</div>
<div class="smallButton redButton athensButton">
<a data-item-name="open-athens" href="/action/ssostart?idp=https%3A%2F%2Fidp.eduserv.org.uk%2Fopenathens&amp;redirectUri=" role="button" aria-label="Open Athens sign in" class="OpenAthens">Open Athens</a>
</div>
<div class="widget graphQueryWidget none  widget-none  widget-compact-all" id="6b408c52-cc1f-48e1-b2f8-2895dd1efa58">
<div class="wrapped ">
<div class="widget-body body body-none  body-compact-all"><div id="denialLeanLibrary-unsubscribed"><div class="lean-library-text unsubscribed"><img src="/pb-assets/Icons/lean-library-1560270847197.svg"><p style="text-align:left">Research off-campus without worrying about access issues. Find out about Lean Library <a target="_blank" rel="noopener" href="https://www.leanlibrary.com/recommend-lean-library/" title="Find out about Lean Library">here</a></p></div></div></div>
</div>
</div>
</div>
</div>
<div id="institution-info">
<div class="bottomSeparator">
<p class="signed-as">I am signed in via:</p>
</div>
<div class="mobile-expand">
<div class="widget literatumInstitutionBanner none  widget-none  widget-compact-all" id="8e68a7e6-e521-477d-a8eb-8029f71977c4">
<div class="wrapped ">
<div class="widget-body body body-none  body-compact-all"><div class="welcome">
<div class="portalInsitutionalButton"><a href="#" onclick="panelToggle('portalInstitutionalLogin', 'myAccountLoginPanel'); return false;">Institution</a></div>
</div></div>
</div>
</div>
<p></p>
<div id="inst-login-status">
</div>
<div class="widget graphQueryWidget none  widget-none  widget-compact-all" id="6b408c52-cc1f-48e1-b2f8-2895dd1efa58">
<div class="wrapped ">
<div class="widget-body body body-none  body-compact-all"><div id="denialLeanLibrary-unsubscribed"><div class="lean-library-text unsubscribed"><img src="/pb-assets/Icons/lean-library-1560270847197.svg"><p style="text-align:left">Research off-campus without worrying about access issues. Find out about Lean Library <a target="_blank" rel="noopener" href="https://www.leanlibrary.com/recommend-lean-library/" title="Find out about Lean Library">here</a></p></div></div></div>
</div>
</div>
</div>
</div>
</div>
<script>
function setInstitutionLoginStatus() {
	if ($('#inst-login-status p').length) return;
	let samlExists=($('.access-via-samel').length)>0;
	let appendTag='';
	if (samlExists) {
		appendTag+='<p>Signed in via: <b>a federated identity</b></p>';
	}
	else {
		appendTag+='<p>Sign in via: <a data-item-name="shibboleth" href="/action/ssostart?redirectUri=" class="Shibboleth">Shibboleth</a></p>';
		appendTag+='<p>Sign in via: <a data-item-name="open-athens" href="/action/ssostart?idp=https%3A%2F%2Fidp.eduserv.org.uk%2Fopenathens&amp;redirectUri=" class="OpenAthens">Open Athens</a></p>';
	}
	$('#inst-login-status').append(appendTag);
}
function setRedirectUrl() {
	let currentUrl = window.location.pathname;
	$('.Shibboleth').attr("href", $('.Shibboleth').attr('href') + currentUrl);
	$('.OpenAthens').attr("href", $('.OpenAthens').attr('href') + currentUrl);
}
function initInstitutionInfo() {
	setInstitutionLoginStatus();
	setRedirectUrl();
	let instName=$('.id-institution-activated').attr('name') || 'your institution';
	if ($('.id-institution-activated>img.user-logo').attr('title')===undefined)
		$('.id-institution-activated>img.user-logo').attr('title', 'You are authenticated via '+instName);
	else 
		$('.id-institution-activated>img.user-logo').attr('title', $('.id-institution-activated>img.user-logo').attr('title').replace('signed in', 'authenticated').replace('your institution', instName));
	$('.id-institution-deactivated>img.user-logo').attr('title', 'You are not authenticated via an institution');
	$('#institution-info .portalInsitutionalButton').after('<div><p style="font-size: 16px">my institutional subscription</p></div>');

	//if ($('#institution-info .portalInsitutionalButton a').length) $('#institution-info .portalInsitutionalButton a').text();

	if (hasInstitutionIdentity()) {
		$('#institution-info').show();
		$('#institution-login-form').hide();
	}
	else {
		$('#institution-info').hide();
		$('#institution-login-form').show();
	}
}
</script></div>
</div>
</div>

<div class="widget general-rich-text none login-instructions widget-none  widget-compact-all widget-border-toggle" id="b7fef331-bd43-4ab1-955f-ecd337b88646">
<div class="wrapped ">
<div class="widget-body body body-none  body-compact-all body-border-toggle"><div id="rich-text-b7fef331-bd43-4ab1-955f-ecd337b88646" class="pb-rich-text">
<p>With institutional access I can:</p>
<ul>
<li>View or download all content the institution has subscribed to.</li>
</ul>
</div></div>
</div>
</div>
</div>
</div>
<div class="col-md-1-3 ">
<div class="contents" data-pb-dropzone="contents2">
<div class="widget general-html-asset none login-column widget-none  widget-compact-all" id="3490cd13-4dff-4c77-9221-72e8b508ebbc">
<div class="wrapped ">
<div class="widget-body body body-none  body-compact-all"><h3 class="login-society" aria-describedby="info-society">Society <span class="login-expander"></span></h3>
<div class="midSection">
<div id="society-login-form">
<div class="login-info" id="info-society">
<p>If you have access to journal via a society or associations, read the instructions below</p>
</div>
<div class="mobile-expand">
<div class="widget ssoLoginWidget none ym-sso-login widget-none  widget-compact-all" id="f2fc11e2-1981-45c8-a8b9-54b2f83b9a3c">
<div class="wrapped " id='society-login-ym'>
<div class="widget-body body body-none  body-compact-all"><div class="sage-sso-doLogin">
<form action="/action/ymDoLogin" id="frmYMDoLogin" name="frmYMDoLogin" method="post"><div class="sage-sso-label">Members of _ can log in with their society credentials below</div>
<div class="richTextDropZone" data-pb-dropzone="richTextDropZone">
</div>
<table class="loginForm" summary="">
<table class="loginForm" summary="">
<tr>
<th><label for="sso-login" class="userNameLoginLabel">Username <span class="required-field">(required)</span></label></th>
<td>
<input id="sso-login" class="textInput" type="text" name="login" value="" size="15" />
</td>
</tr>
<tr>
<th><label for="sso-password" class="passwordLoginLabel">Password <span class="required-field">(required)</span></label></th>
<td>
<input id="sso-password" class="textInput" type="password" name="password" value="" autocomplete="off" />
</td>
</tr>
<tr>
<th><label for="society" class="memberSSOSocietiesList">Society <span class="required-field">(required)</span></label></th>
<td>
<select name="society" class="sso-select-society" id="society-token-f2fc11e2-1981-45c8-a8b9-54b2f83b9a3c">
<option value="ISREAPI">The Int Society for Research on Emotion</option>
<option value="ACV">American College of Veterinary Pathologists</option>
</select>
</td>
</tr>
</table>
</table>
<input type="hidden" name="redirectUri" value="/action/doSearch?prg140729=d2e0b346-99b3-4538-8243-2fbb08871bd0" />
<input type="hidden" name="loginUri" value="/action/doSearch?prg140729=d2e0b346-99b3-4538-8243-2fbb08871bd0" />
<input type="hidden" name="submitViaAJAX" value="true" />
<tr>
<td role="alert" class="error">
<span class="useAJAX_SSO_error error" style="display: none;">The email address and/or password entered does not match our records, please check and try again.</span></td>
</tr>
<input class="sso-submit-button defButton" role="button" type="submit" name="submit" value="Sign in" tabindex="0" aria-label="Sign In via a society" /><br /></form>
</div></div>
</div>
</div>
<div class="widget general-rich-text none  widget-none  widget-compact-all" id="5400f2c3-12ae-4d58-81ff-11246a8f0f87">
<div class="wrapped " id='society-info-text'>
<div class="widget-body body body-none  body-compact-all"><div id="rich-text-5400f2c3-12ae-4d58-81ff-11246a8f0f87" class="pb-rich-text">
<p>Access to society journal content varies across our titles.</p>
<p>If you have access to a journal via a society or association membership, please browse to your society journal, select an article to view, and follow the instructions in this box.</p>
<p>Contact us if you experience any difficulty logging in.</p>
</div></div>
</div>
</div>

<div class="widget graphQueryWidget none  widget-none  widget-compact-all" id="945c9203-f170-4618-a512-c9af215016ff">
<div class="wrapped ">
<div class="widget-body body body-none  body-compact-all"><div class="society-denial-login-link"><script>$(document.currentScript).closest('div.society-denial-login-link').append($(document.currentScript).closest('.mobile-expand,#denial-2').find('.literatumAd.society-denial-login-link .pb-ad').children())</script></div><script>$('.literatumAd.society-denial-login-link').hide()</script></div>
</div>
</div>
<div class="topSeparator">
<p style="text-align:left">Some society journals require you to create a personal profile, then activate your society account</p>
<div class="blueGrayButton smallButton">
<a data-item-name="activate-society" href="/page/resources/societies/activate-your-membership" role="button">Activate my Society Account</a>
</div>
</div>
</div>
</div>
<div id="society-info">
<div class="bottomSeparator">
<p class="signed-as">I am signed in via:</p>
</div>
<div class="mobile-expand">
<div class="widget literatumInstitutionBanner none  widget-none  widget-compact-all" id="9abd0442-8f9c-4410-8840-acc27eb9f8ca">
<div class="wrapped ">
<div class="widget-body body body-none  body-compact-all"><div class="welcome">
<div class="portalInsitutionalButton"><a href="#" onclick="panelToggle('portalInstitutionalLogin', 'myAccountLoginPanel'); return false;">Institution</a></div>
</div></div>
</div>
</div>
<div class="logout-section blueGrayButton smallButton">
<a class="register-link logOut" data-item-name="logout" href="/action/doLogout?redirectUri=#" role="button" aria-label="Sign out" id="ru-society">Logout</a>
</div>
</div>
</div>
</div>
<div class="widget general-html none  widget-none  widget-compact-all" id="05f287e0-10b6-4da1-bdd9-72135b7fc1cf">
<div class="wrapped ">
<div class="widget-body body body-none  body-compact-all"><script>
function getYmCount() {
    let rv=0;
    try{
        rv=Number("2");
        if (isNaN(rv)) rv=0;
    }
    catch (e) {}
    return rv;
}
function getSocietyJournals(index) {
    let rv="";
    try {
        switch (index) {
            case 1:rv="vet"; break;
            case 2:rv="emr"; break;
            case 3:rv=""; break;
            case 4:rv=""; break;
            case 5:rv=""; break;
            default:break;
        }
    }
    catch (e) {}
    return rv;
}
function getSocietyCode(index) {
    let rv="";
    try {
        switch (index) {
            case 1:rv="ACV"; break;
            case 2:rv="ISREAPI"; break;
            case 3:rv=""; break;
            case 4:rv=""; break;
            case 5:rv=""; break;
            default:break;
        }
    }
    catch (e) {}
    return rv;
}
</script></div>
</div>
</div>
<script>
$('#ru-society').attr('href', '/action/doLogout?redirectUri='+window.location.href);
$('.ssoLoginWidget .useAJAX_SSO_error').attr('role','alert');
function initSocietyInfo() {
	let societyName=$('.id-society-activated').attr('name') || 'your society';
	if ($('.id-society-activated>img.user-logo').attr('title')===undefined)
		$('.id-society-activated>img.user-logo').attr('title', 'You are authenticated via '+ societyName);
	else 
		$('.id-society-activated>img.user-logo').attr('title', $('.id-society-activated>img.user-logo').attr('title').replace('signed in','authenticated').replace('your society', societyName));

	$('.id-society-deactivated>img.user-logo').attr('title', 'You are not authenticated via a society');
	$('#society-info .portalInsitutionalButton').after('<div><p style="font-size: 16px">my society or association</p></div>');

	if (hasSocietyIdentity()){
		$('#society-info').show();
		$('#society-login-form').hide();
	}
	else {
		$('#society-info').hide();
		$('#society-login-form').show();
	}
}
function getYmSocietyIndex(){
	let count = getYmCount() || 0;
	let currentJournal = "";
	if (currentJournal.length!==0 && count>0) {
		//console.debug("Looking through "+count+" societies for journal code: "+currentJournal);
		for (i=0; i<count; i++) {
			if (getSocietyJournals(i+1).indexOf(currentJournal)!==-1) {
				console.debug('Journal '+currentJournal+' found for configured society-'+i);
				return i;
			}
		}
	}
	//console.debug('No linked YM SSO society found for current journal');
	return -1;
}
$(function() {
	let ymSocietyIndex=getYmSocietyIndex();
	if (ymSocietyIndex!==-1){
		try{
			let societyOption=$('.sso-select-society option')[ymSocietyIndex];
			$('.sage-sso-label').text(function(){
				return $(this).text().replace('_', societyOption.text);
			});
			$('.sso-select-society').val(getSocietyCode(ymSocietyIndex+1));
			//$('.sso-select-society').closest('tr').hide();
		}
		catch(e) {}
		$('#society-login-form .ym-sso-login, #denial-2 .ym-sso-login').show()
		$('#society-info-text, #society-login-form .topSeparator').hide();
	}
	else{
		$('#society-login-form .ym-sso-login, #denial-2 .ym-sso-login').hide();
		// Check if society ad is present
		if ($('#society-login-form .literatumAd').length!==0) {
			$('#society-info-text, #society-login-form .topSeparator').hide();
		}
		else {
			$('#society-info-text, #society-login-form .topSeparator').show();
		}
	}
	if (hasSocietyIdentity())
		$('#denial-2 .ym-sso-login').hide();
});
$('#frmYMDoLogin input[type="submit"]').click(function() {
	$(this).closest('#frmYMDoLogin').find('.useAJAX_SSO_error').hide();
});
</script></div>
</div>
</div>
<div class="widget general-rich-text none login-instructions widget-none  widget-compact-all widget-border-toggle" id="7f8ccf20-e508-4dc4-8bd0-3b37447a92da">
<div class="wrapped ">
<div class="widget-body body body-none  body-compact-all body-border-toggle"><div id="rich-text-7f8ccf20-e508-4dc4-8bd0-3b37447a92da" class="pb-rich-text">
<p>With society access I can:</p>
<ul>
<li>View or download all the content the society has access to.</li>
</ul>
</div></div>
</div>
</div>
</div>
</div>
</div>
</div></div>
</div>
</div>
</div>
<div id="loginbox-footer">
<div class="widget general-rich-text none desktopOnly widget-none  widget-compact-all" id="6531387b-cd17-4273-a2e3-fe5456ba9911">
<div class="wrapped ">
<div class="widget-body body body-none  body-compact-all"><div id="rich-text-6531387b-cd17-4273-a2e3-fe5456ba9911" class="pb-rich-text">
<p style="text-align: center;"><span style="font-family: arial, helvetica, sans-serif; font-size: small; text-align: center;">Need Help?&nbsp;</span><a href="/page/help/home" style="font-family: arial, helvetica, sans-serif; font-size: small; text-align: center;">Contact SAGE</a></p>
</div></div>
</div>
</div>
<div class="mobileOnly blueGrayButton smallButton" style="padding-top:10px">
<a href="/page/help/home" style="margin-bottom:10px">Need Help? Contact SAGE</a>
</div>
</div>
<input tabindex="0" class="closeLoginPopup" onclick="toggleLoginPopup(false);return false;" src="/pb-assets/Icons/Cross-no-outline-1560270847187.svg" title="Close sign-in menu" alt="x" type="image">
</div></div>
</div>
</div>
</div></div>
</div>
</div>
</div></div>
</div>
</div>
</div></div>
</div>
</div>
</div>
<div class="widget general-html-asset none  widget-none  widget-compact-all" id="4a3dbd8f-4c00-441a-83b1-f52d15c947f5">
<div class="wrapped ">
<div class="widget-body body body-none  body-compact-all"><div id="searchBarContainer">
<div id="mainSearchBar" class="searchBar" role="dialog" data-module-name="auto-suggest" tabindex="0">

<div class="widget quickSearchWidget none portalQuickSearch widget-none  widget-compact-all" id="5970b95b-1daa-4b7c-8aac-d717c09c893a">
<div class="wrapped " id='portalQuickSearch'>
<div class="widget-body body body-none  body-compact-all"><util:actionContext />
<div class="quickSearchFormContainer" data-module-name="auto-suggest">
<form action="/action/doSearch" id="quickSearch" name="quickSearch" class="quickSearchForm " style="padding-left: 0px" title="Quick Search" method="get"><div class="qsFilterOption-div">
<select class="filterOption" name="filterOption">
<option value="allJournal" data-item-name="search-all-journals">Search all journals</option>
<option value="thisJournal" data-item-name="search-this-journal" disabled>Search this journal</option>
</select>
</div>
<span class="simpleSearchBoxContainer" id="meme">
<input name="AllField" class="searchText main-search-field autocomplete" value="" type="search" id="searchText" title="Type search term here" placeholder="Search all SAGE Journals" autocomplete="off" data-history-items-conf="0" data-publication-titles-conf="3" data-publication-items-conf="4" data-topics-conf="0" data-contributors-conf="3" data-display-labels="true" data-fuzzy-suggester="true">
</span>
<input class="mainSearchButton searchButtons pointer" title="search" type="submit" value="Search" /></form>
</div>
<div class="advancedSearchLinkDropZone" data-pb-dropzone="advancedSearchLinkDropZone">
<div class="widget general-html none journalAdvancedSearch widget-none  widget-compact-all" id="069075cf-3cbd-4987-8bbb-f8fcf8ef1c6a">
<div class="wrapped ">
<div class="widget-body body body-none  body-compact-all"><a class="advancedSearchLink" href="/search/advanced">Advanced Search</a></div>
</div>
</div>
</div></div>
</div>
</div>
<input tabindex="0" class="close-button" onclick="closeSearchDialog();return false;" src="/pb-assets/Icons/Error-redcross-1572436449097.svg" type="image" alt="x" role="button">
</div>
</div>
<script>
	if (inPortalHome()) $('#mainSearchBar').remove();
</script></div>
</div>
</div>
</div>
</div>
</div>
</div></div>
</div>
</div>
<div class="widget layout-frame none page-header-divider widget-none  widget-compact-all" id="acde3693-b9e2-455b-9e33-b0c307a98fad">
<div class="wrapped ">
<div class="widget-body body body-none  body-compact-all"><div data-pb-dropzone="contents">
</div></div>
</div>
</div>
</div></div>
</div>
</div>
</div>
</header></div>
</div>
</div>
<div class="widget layout-one-column none  widget-none  widget-compact-all" id="d0f0cfab-b768-49e6-aa02-545c2f1aafb2">
<div class="wrapped ">
<div class="widget-body body body-none  body-compact-all"><div class="pb-columns row-fluid">
<div class="width_1_1">
<div data-pb-dropzone="center">
</div>
</div>
</div></div>
</div>
</div>
<div class="widget pageBody none search-page-body widget-none  widget-compact-all" id="b90442ed-bd15-483c-9c3d-448b7c0604f7">
<div class="wrapped ">
<div class="widget-body body body-none  body-compact-all">
<div class="page-body pagefulltext">
<div data-pb-dropzone="main">
<div class="widget responsive-layout none  widget-none  widget-compact-horizontal" id="5522b9ff-da3b-49f8-a6b0-c804e80074d1">
<div class="wrapped ">
<div class="widget-body body body-none  body-compact-horizontal"><div class="container">
<div class="row row-md  ">
<div class="col-md-2-3 ">
<div class="contents" data-pb-dropzone="contents0">
<div class="widget general-heading none  widget-none  widget-compact-all" id="ae790b9c-277f-48fc-9248-c6aed08277e4">
<div class="wrapped ">
<div class="widget-body body body-none  body-compact-all"><div class="page-heading">
<h1>Advanced Search</h1>
</div></div>
</div>
</div>
<div data-widget-def="newAdvancedSearch" data-widget-id="5d85b1d7-6650-40e0-9588-d7bee9a63649" data-module-name="refine-search">
<div class="widget newAdvancedSearch none  widget-none  widget-compact-horizontal" id="5d85b1d7-6650-40e0-9588-d7bee9a63649">
<div class="wrapped ">
<div class="widget-body body body-none  body-compact-horizontal"><div class="search-tabs search-tabs-widget">
<div class="tab-content">
<div id="refine-search-panel" class="tab-pane clear active" role="tabpanel" aria-labelledby="refine-search-tab" aria-hidden="false">
<div id="mainSearchFormContainer" aria-hidden="false" class="smallMarginTop clear">
<form action="/action/doSearch" id="frmSearch" name="frmSearch" class="frmSearch" method="get"><fieldset id="mainSearchForm" class="mainSearchForm">
<legend class="visuallyhidden">Access Type</legend>
<input type="hidden" name="content" value="articlesChapters" />
<input type="hidden" name="countTerms" value="true" />
<input type="hidden" name="target" value="default" />

<input type="hidden" value="AfterYear" />
<input type="hidden" value="BeforeYear" />
<div class="search-terms">
<div class="formRow">
<label class="visuallyhidden">Search in</label>
<select name="field1" class="fieldSelect" title="">
<option value="AllField">
Anywhere
</option>
<option value="Title">
Title
</option>
<option value="Contrib">
Author
</option>
<option value="Keyword">
Keywords
</option>
<option value="Abstract">
Abstract
</option>
<option value="Affiliation">
Affiliation
</option>
</select>
<input id="advSearch_keyw_for_1" class="search-term" title="Type search term here" type="search" name="text1" value="" placeholder="Enter search term" />
<span tabindex="0" role="button" class="addTerm js__addTermNew hidden" title="Add more search terms"></span>
<span tabindex="0" role="button" class="removeTerm" title="Remove this search term"></span>
</div>
<div class="formRow">
<label class="visuallyhidden">Search in</label>
<select name="field2" class="fieldSelect" title="">
<option value="AllField">
Anywhere
</option>
<option value="Title">
Title
</option>
<option value="Contrib">
Author
</option>
<option value="Keyword">
Keywords
</option>
<option value="Abstract">
Abstract
</option>
<option value="Affiliation">
Affiliation
</option>
</select>
<input id="advSearch_keyw_for_2" class="search-term" title="Type search term here" type="search" name="text2" value="" placeholder="Enter search term" />
<span tabindex="0" role="button" class="addTerm js__addTermNew" title="Add more search terms"></span>
<span tabindex="0" role="button" class="removeTerm hidden" title="Remove this search term"></span>
</div>
</div>
<div class="search-filters">
<div class="normal-filters">
<label for="publication">Published in</label>
<span class="FavFilters">
<a class="getFav" name="get Favorites" id="getFav" tabindex="0">My favorites</a> | <a class="filterClear" id="filterClear" name="filter Clear" tabindex="0">clear</a>
<p id="favError" class="favError"></p>
</span>
<input class="isLoggedIn" id="isLoggedIn" value="false" type="hidden">
<input type="search" class="search-term magicsuggest2" name="publication" data-auto-complete-target="title-auto-complete" placeholder="Enter journal title" title="Type publication here" />
</div>
<div class="normal-filters date-filter formRowRes">

<label class="pub-date-heading">Publication Date</label>
<div class="date-filters">
<div class="date-field">
<input id="anyDate" type="radio" name="Ppub" value="" checked="checked" onchange="SearchUtil.clearMonthYearDropDown()" />
<label for="anyDate">

All dates
</label>
</div>
<div class="date-field timeFrame">
<input id="static-range" type="radio" name="Ppub" value="" onchange="SearchUtil.clearMonthYearDropDown()" />
<label for="static-range">

Last:
</label>
<select id="static-ranges" name="Ppub" class="static-ranges">
<option value="" selected="selected">
Select
</option>
<option value="20200603-20200703">
month
</option>
<option value="20200103-20200703">
6 months
</option>
<option value="20190703-20200703">
year
</option>
</select>
</div>
<div id="timeFrame" class="date-field clear timeFrame">
<input id="custom-range" type="radio" name="Ppub" value="" onchange="SearchUtil.clearMonthYearDropDown()" />
<label for="custom-range">Custom range:</label>
<label class="visuallyhidden">From:</label>
<div class="AfterFilter ">
<util:actionContext />
<util:actionContext />
<label for="AfterYear" class="visuallyhidden"> </label>
<select id="AfterYear" name="AfterYear" class="AfterYearSelect dateFilterSelect ">
<option value="">Year</option>
<option value="2020">2020</option>
<option value="2019">2019</option>
<option value="2018">2018</option>
<option value="2017">2017</option>
<option value="2016">2016</option>
<option value="2015">2015</option>
<option value="2014">2014</option>
<option value="2013">2013</option>
<option value="2012">2012</option>
<option value="2011">2011</option>
<option value="2010">2010</option>
<option value="2009">2009</option>
<option value="2008">2008</option>
<option value="2007">2007</option>
<option value="2006">2006</option>
<option value="2005">2005</option>
<option value="2004">2004</option>
<option value="2003">2003</option>
<option value="2002">2002</option>
<option value="2001">2001</option>

<option value="2000">2000</option>
<option value="1999">1999</option>
<option value="1998">1998</option>
<option value="1997">1997</option>
<option value="1996">1996</option>
<option value="1995">1995</option>
<option value="1994">1994</option>
<option value="1993">1993</option>
<option value="1992">1992</option>
<option value="1991">1991</option>
<option value="1990">1990</option>
<option value="1989">1989</option>
<option value="1988">1988</option>
<option value="1987">1987</option>
<option value="1986">1986</option>
<option value="1985">1985</option>
<option value="1984">1984</option>
<option value="1983">1983</option>
<option value="1982">1982</option>
<option value="1981">1981</option>
<option value="1980">1980</option>
<option value="1979">1979</option>
<option value="1978">1978</option>
<option value="1977">1977</option>
<option value="1976">1976</option>
<option value="1975">1975</option>
<option value="1974">1974</option>
<option value="1973">1973</option>
<option value="1972">1972</option>
<option value="1971">1971</option>
<option value="1970">1970</option>
<option value="1969">1969</option>
<option value="1968">1968</option>
<option value="1967">1967</option>
<option value="1966">1966</option>
<option value="1965">1965</option>
<option value="1964">1964</option>
<option value="1963">1963</option>
<option value="1962">1962</option>
<option value="1961">1961</option>
<option value="1960">1960</option>
<option value="1959">1959</option>
<option value="1958">1958</option>
<option value="1957">1957</option>
<option value="1956">1956</option>
<option value="1955">1955</option>
<option value="1954">1954</option>
<option value="1953">1953</option>
<option value="1952">1952</option>
<option value="1951">1951</option>
<option value="1950">1950</option>
<option value="1949">1949</option>
<option value="1948">1948</option>
<option value="1947">1947</option>
<option value="1946">1946</option>
<option value="1945">1945</option>
<option value="1944">1944</option>
<option value="1943">1943</option>
<option value="1942">1942</option>
<option value="1941">1941</option>
<option value="1940">1940</option>
<option value="1939">1939</option>
<option value="1938">1938</option>
<option value="1937">1937</option>
<option value="1936">1936</option>
<option value="1935">1935</option>
<option value="1934">1934</option>
<option value="1933">1933</option>
<option value="1932">1932</option>
<option value="1931">1931</option>

<option value="1930">1930</option>
<option value="1929">1929</option>
<option value="1928">1928</option>
<option value="1927">1927</option>
<option value="1926">1926</option>
<option value="1925">1925</option>
<option value="1924">1924</option>
<option value="1923">1923</option>
<option value="1922">1922</option>
<option value="1921">1921</option>
<option value="1920">1920</option>
<option value="1919">1919</option>
<option value="1918">1918</option>
<option value="1917">1917</option>
<option value="1916">1916</option>
<option value="1915">1915</option>
<option value="1914">1914</option>
<option value="1913">1913</option>
<option value="1912">1912</option>
<option value="1911">1911</option>
<option value="1910">1910</option>
<option value="1909">1909</option>
<option value="1908">1908</option>
<option value="1907">1907</option>
<option value="1906">1906</option>
<option value="1905">1905</option>
<option value="1904">1904</option>
<option value="1903">1903</option>
<option value="1902">1902</option>
<option value="1901">1901</option>
<option value="1900">1900</option>
<option value="1899">1899</option>
<option value="1898">1898</option>
<option value="1897">1897</option>
<option value="1896">1896</option>
<option value="1895">1895</option>
<option value="1894">1894</option>

<option value="1893">1893</option>
<option value="1892">1892</option>
<option value="1891">1891</option>
<option value="1890">1890</option>
<option value="1889">1889</option>
<option value="1888">1888</option>
<option value="1887">1887</option>
<option value="1886">1886</option>
<option value="1885">1885</option>
<option value="1884">1884</option>
<option value="1883">1883</option>
<option value="1882">1882</option>
<option value="1881">1881</option>
<option value="1880">1880</option>
<option value="1879">1879</option>
<option value="1878">1878</option>
<option value="1877">1877</option>
<option value="1876">1876</option>
<option value="1875">1875</option>
<option value="1874">1874</option>
<option value="1873">1873</option>
<option value="1872">1872</option>
<option value="1871">1871</option>
<option value="1870">1870</option>
<option value="1869">1869</option>
<option value="1868">1868</option>
<option value="1867">1867</option>
<option value="1866">1866</option>
<option value="1865">1865</option>
<option value="1864">1864</option>
<option value="1863">1863</option>
<option value="1862">1862</option>
<option value="1861">1861</option>
<option value="1860">1860</option>

<option value="1859">1859</option>
<option value="1858">1858</option>
<option value="1857">1857</option>
<option value="1856">1856</option>
<option value="1855">1855</option>
<option value="1854">1854</option>
<option value="1853">1853</option>
<option value="1852">1852</option>
<option value="1851">1851</option>
<option value="1850">1850</option>
<option value="1849">1849</option>
<option value="1848">1848</option>
<option value="1847">1847</option>
</select>
</div>
<label class="to-date-label">To:</label>
<div class="BeforeFilter ">
<util:actionContext />
<util:actionContext />
<label for="BeforeYear" class="visuallyhidden"> </label>
<select id="BeforeYear" name="BeforeYear" class="BeforeYearSelect dateFilterSelect ">
<option value="">Year</option>
<option value="2020">2020</option>
<option value="2019">2019</option>
<option value="2018">2018</option>
<option value="2017">2017</option>
<option value="2016">2016</option>
<option value="2015">2015</option>
<option value="2014">2014</option>
<option value="2013">2013</option>
<option value="2012">2012</option>
<option value="2011">2011</option>
<option value="2010">2010</option>
<option value="2009">2009</option>
<option value="2008">2008</option>
<option value="2007">2007</option>
<option value="2006">2006</option>
<option value="2005">2005</option>
<option value="2004">2004</option>
<option value="2003">2003</option>
<option value="2002">2002</option>
<option value="2001">2001</option>
<option value="2000">2000</option>
<option value="1999">1999</option>
<option value="1998">1998</option>
<option value="1997">1997</option>
<option value="1996">1996</option>
<option value="1995">1995</option>
<option value="1994">1994</option>
<option value="1993">1993</option>
<option value="1992">1992</option>
<option value="1991">1991</option>
<option value="1990">1990</option>
<option value="1989">1989</option>
<option value="1988">1988</option>
<option value="1987">1987</option>
<option value="1986">1986</option>
<option value="1985">1985</option>
<option value="1984">1984</option>
<option value="1983">1983</option>
<option value="1982">1982</option>
<option value="1981">1981</option>
<option value="1980">1980</option>
<option value="1979">1979</option>
<option value="1978">1978</option>
<option value="1977">1977</option>
<option value="1976">1976</option>
<option value="1975">1975</option>
<option value="1974">1974</option>
<option value="1973">1973</option>
<option value="1972">1972</option>
<option value="1971">1971</option>
<option value="1970">1970</option>
<option value="1969">1969</option>
<option value="1968">1968</option>

<option value="1967">1967</option>
<option value="1966">1966</option>
<option value="1965">1965</option>
<option value="1964">1964</option>
<option value="1963">1963</option>
<option value="1962">1962</option>
<option value="1961">1961</option>
<option value="1960">1960</option>
<option value="1959">1959</option>
<option value="1958">1958</option>
<option value="1957">1957</option>
<option value="1956">1956</option>
<option value="1955">1955</option>
<option value="1954">1954</option>
<option value="1953">1953</option>
<option value="1952">1952</option>
<option value="1951">1951</option>
<option value="1950">1950</option>
<option value="1949">1949</option>
<option value="1948">1948</option>
<option value="1947">1947</option>
<option value="1946">1946</option>
<option value="1945">1945</option>
<option value="1944">1944</option>
<option value="1943">1943</option>
<option value="1942">1942</option>
<option value="1941">1941</option>
<option value="1940">1940</option>
<option value="1939">1939</option>
<option value="1938">1938</option>
<option value="1937">1937</option>
<option value="1936">1936</option>
<option value="1935">1935</option>
<option value="1934">1934</option>
<option value="1933">1933</option>
<option value="1932">1932</option>
<option value="1931">1931</option>
<option value="1930">1930</option>
<option value="1929">1929</option>
<option value="1928">1928</option>
<option value="1927">1927</option>
<option value="1926">1926</option>
<option value="1925">1925</option>
<option value="1924">1924</option>
<option value="1923">1923</option>
<option value="1922">1922</option>
<option value="1921">1921</option>
<option value="1920">1920</option>
<option value="1919">1919</option>
<option value="1918">1918</option>
<option value="1917">1917</option>
<option value="1916">1916</option>
<option value="1915">1915</option>
<option value="1914">1914</option>
<option value="1913">1913</option>
<option value="1912">1912</option>
<option value="1911">1911</option>
<option value="1910">1910</option>
<option value="1909">1909</option>
<option value="1908">1908</option>
<option value="1907">1907</option>
<option value="1906">1906</option>
<option value="1905">1905</option>
<option value="1904">1904</option>
<option value="1903">1903</option>
<option value="1902">1902</option>
<option value="1901">1901</option>
<option value="1900">1900</option>
<option value="1899">1899</option>
<option value="1898">1898</option>
<option value="1897">1897</option>
 <option value="1896">1896</option>
<option value="1895">1895</option>
<option value="1894">1894</option>
<option value="1893">1893</option>
<option value="1892">1892</option>
<option value="1891">1891</option>
<option value="1890">1890</option>
<option value="1889">1889</option>
<option value="1888">1888</option>
<option value="1887">1887</option>
<option value="1886">1886</option>
<option value="1885">1885</option>
<option value="1884">1884</option>
<option value="1883">1883</option>
<option value="1882">1882</option>
<option value="1881">1881</option>
<option value="1880">1880</option>
<option value="1879">1879</option>
<option value="1878">1878</option>
<option value="1877">1877</option>
<option value="1876">1876</option>
<option value="1875">1875</option>
<option value="1874">1874</option>
<option value="1873">1873</option>
<option value="1872">1872</option>
<option value="1871">1871</option>
<option value="1870">1870</option>
<option value="1869">1869</option>
<option value="1868">1868</option>
<option value="1867">1867</option>
<option value="1866">1866</option>
<option value="1865">1865</option>
<option value="1864">1864</option>
<option value="1863">1863</option>
<option value="1862">1862</option>
<option value="1861">1861</option>
<option value="1860">1860</option>
<option value="1859">1859</option>
<option value="1858">1858</option>
<option value="1857">1857</option>
<option value="1856">1856</option>
<option value="1855">1855</option>
<option value="1854">1854</option>
<option value="1853">1853</option>
<option value="1852">1852</option>
<option value="1851">1851</option>
<option value="1850">1850</option>
<option value="1849">1849</option>
<option value="1848">1848</option>
<option value="1847">1847</option>
</select>
</div>
</div>
</div>
</div>
<div class="advanced-filters clear">
<span class="advancedFiltersHeader" role="button">Access Type&nbsp;<span class="arrowDecoration arrow-down"></span></span>
<span class="advancedFiltersHeader hidden" role="button">Access Type&nbsp;&nbsp;<span class="arrowDecoration arrow-up"></span></span>
<div class="advancedFilters hidden">
<div class="extraContentFilters">
<input type="checkbox" name="earlycite" value="on" checked="checked" />
<label for="earlycite">Include&nbsp;Pre-print</label>
</div>
<input type="hidden" name="earlycite" value="off" disabled />
<fieldset>
<ul class="accessFilterList">
<li>
<input id="allContent" type="radio" name="access" value="" checked="checked" />
<label for="allContent">All content</label>
</li>
<li>
<input id="openAccess" type="radio" name="access" value="18" />
<label for="openAccess">Open access content only</label>
</li>
<li>
<input id="accessOnly" type="radio" name="access" value="user" />
<label for="accessOnly">Only content to which I have full access</label>
</li>
</ul>
</fieldset>
</div>
</div>

</div>
<div class="clear">
<input id="submitPubSearchButton" class="searchButtons pointer" title="Search" type="submit" value="Search" />
</div>
</fieldset></form>
</div>
</div>
</div>
</div></div>
</div>
</div>
</div>
<div class="widget citationSearch none  widget-none  widget-compact-horizontal" id="3e7d3c68-7d28-4f27-ac7c-67f50457c562">
<div class="wrapped ">
<h2 class="widget-header header-none  header-compact-horizontal">Citation Search</h2>
<div class="widget-body body body-none  body-compact-horizontal"><div class="citationSearchContainer clear searchBox">
<form action="/action/quickLink" id="citationSearchForm" name="citationSearch" method="get"><fieldset>
<select name="quickLinkJournal" size="7" id="publicationSpan" class=" citationJournalName citation magicsuggest" data-placeholder="Journal">
<option value="ijoa">A.P.T.O. Journal</option>
<option value="aipa">AADE in Practice</option>
<option value="rpsa">AAESPH Review</option>
<option value="whsc">AAOHN Journal</option>
<option value="bcqb">ABCA Bulletin</option>
<option value="acaa">About Campus</option>
<option value="phre">Abstract of Sanitary Reports</option>
<option value="aaxa">Abstracts in Anthropology</option>
<option value="bcqa">ABWA Bulletin</option>
<option value="afpa">Academic Forensic Pathology</option>
<option value="apca">Academic Pathology</option>
<option value="iscb">Academic Therapy</option>
<option value="isca">Academic Therapy Quarterly</option>
<option value="acha">Accounting History</option>
<option value="acrc">Acta Radiologica</option>
<option value="acra">Acta Radiologica</option>
<option value="acrb">Acta Radiologica. Diagnosis</option>
<option value="arrb">Acta Radiologica Open</option>
<option value="arra">Acta Radiologica Short Reports</option>
<option value="asja">Acta Sociologica</option>
<option value="sjpb">Acta Socio-Medica Scandinavica</option>
<option value="arja">Action Research</option>
<option value="alha">Active Learning in Higher Education</option>
<option value="aima">Acupuncture in Medicine</option>
<option value="cbaa">A Current Bibliography on African Affairs</option>
<option value="adba">Adaptive Behavior</option>
<option value="aipb">ADCES in Practice</option>
<option value="aasb">Administration &amp; Society</option>
<option value="asqa">Administrative Science Quarterly</option>
<option value="aafa">Adoption &amp; Fostering</option>
<option value="adta">Adsorption Science &amp; Technology</option>
<option value="aeqa">Adult Education</option>
<option value="aeqb">Adult Education Quarterly</option>
<option value="alxa">Adult Learning</option>
<option value="acma">Advanced Composites Letters</option>
<option value="adra">Advances in Dental Research</option>
<option value="adha">Advances in Developing Human Resources</option>
<option value="adea">Advances in Mechanical Engineering</option>
<option value="ampa">Advances in Methods and Practices in Psychological Science</option>
<option value="asea">Advances in Structural Engineering</option>
<option value="wafd">Advocate of Peace</option>
<option value="waff">Advocate of Peace</option>
<option value="wafi">Advocate of Peace Through Justice</option>
<option value="eroa">AERA Open</option>
<option value="affa">Affilia</option>
<option value="afra">Africa Spectrum</option>
<option value="ahda">Aging and Human Development</option>
<option value="agsa">Agrarian South: Journal of Political Economy</option>
<option value="aswa">Air, Soil and Water Research</option>
<option value="alaa">Alexandria</option>
<option value="nadb">Alkoholpolitik</option>
<option value="aara">Allergy &amp; Rhinology</option>
<option value="alna">AlterNative: An International Journal of Indigenous Peoples</option>
<option value="chpa">Alternative health practitioner</option>
<option value="aljb">Alternative Law Journal</option>
<option value="alta">Alternatives</option>
<option value="atla">Alternatives to Laboratory Animals</option>
<option value="wafc">American Advocate of Peace</option>
<option value="whsa">American Association of Industrial Nurses Journal</option>
<option value="absb">American Behavioral Scientist</option>
<option value="aera">American Educational Research Journal</option>
<option value="ajaa">American Journal of Alzheimer's Care and Related Disorders</option>
<option value="ajac">American Journal of Alzheimer's Care and Related Disorders &amp; Research</option>
<option value="ajab">American Journal of Alzheimer's Care and Research</option>
<option value="ajad">American Journal of Alzheimer's Disease</option>
<option value="ajae">American Journal of Alzheimer's Disease &amp; Other Dementiasr</option>
<option value="ajec">American Journal of Evaluation</option>
<option value="ahpa">American Journal of Health Promotion</option>
<option value="ajhb">American Journal of Hospice and Palliative Medicine®</option>
<option value="ajha">American Journal of Hospice Care</option>
<option value="jlma">American Journal of Law &amp; Medicine</option>
<option value="ajla">American Journal of Lifestyle Medicine</option>
<option value="ajmb">American Journal of Medical Quality</option>
<option value="jmha">American Journal of Men's Health</option>
<option value="ajrb">American Journal of Rhinology</option>
<option value="ajra">American Journal of Rhinology &amp; Allergy</option>
<option value="etpa">American Journal of Small Business</option>
<option value="jmxc">American Marketing Journal</option>
<option value="apra">American Politics Quarterly</option>
<option value="aprb">American Politics Research</option>
<option value="asra">American Sociological Review</option>
<option value="staa">American String Teacher</option>
<option value="aica">Anaesthesia and Intensive Care</option>
<option value="acia">Analytical Chemistry Insights</option>
<option value="anga">Angiology</option>
<option value="clwa">Anglo-American Law Review</option>
<option value="anma">Animation</option>
<option value="sjsa">Annales Chirurgiae et Gynaecologiae</option>
<option value="acbb">Annals of Clinical Biochemistry</option>
<option value="aona">Annals of Neurosciences</option>
<option value="aora">Annals of Otology, Rhinology &amp; Laryngology</option>
<option value="aopd">Annals of Pharmacotherapy</option>
<option value="saxa">Annals of Sex Research</option>
<option value="anib">Annals of the ICRP</option>
<option value="ania">Annals of the ICRP/ICRP Publication</option>
<option value="anra">The Anthropocene Review</option>
<option value="anta">Anthropological Theory</option>
<option value="avca">Antiviral Chemistry and Chemotherapy</option>
<option value="jwsa">ANTYAJAA: Indian Journal of Women and Social Change</option>
<option value="apbb">Applied Biosafety</option>
<option value="apma">Applied Psychological Measurement</option>
<option value="aspc">Applied Spectroscopy</option>
<option value="ijob">APTO</option>
<option value="prja">Archive for the Psychology of Religion</option>
<option value="afsa">Armed Forces &amp; Society</option>
<option value="atha">Arthaniti: Journal of Economic Theory and Practice</option>
<option value="ahha">Arts and Humanities in Higher Education</option>
<option value="amja">Asian and Pacific Migration Journal</option>
<option value="aana">Asian Cardiovascular and Thoracic Annals</option>
<option value="acpa">Asian Journal of Comparative Politics</option>
<option value="alea">Asian Journal of Legal Education</option>
<option value="ajca">Asian Journal of Management Cases</option>
<option value="abra">Asia Pacific Business Review</option>
<option value="apja">Asia Pacific Journal of Human Resources</option>
<option value="abrb">Asia-Pacific Journal of Management Research and Innovation</option>
<option value="apha">Asia Pacific Journal of Public Health</option>
<option value="jrda">Asia-Pacific Journal of Rural Development</option>
<option value="amea">Asia Pacific Media Educator</option>
<option value="asna">ASN Neuro</option>
<option value="asma">Assessment</option>
<option value="aeib">Assessment for Effective Intervention</option>
<option value="aeca">Australasian Journal of Early Childhood</option>
<option value="apya">Australasian Psychiatry</option>
<option value="anja">Australian &amp; New Zealand Journal of Criminology</option>
<option value="anpa">Australian &amp; New Zealand Journal of Psychiatry</option>
<option value="acda">Australian Journal of Career Development</option>
<option value="aeda">Australian Journal of Education</option>
<option value="auma">Australian Journal of Management</option>
<option value="hime">Australian Medical Record</option>
<option value="hima">Australian Medical Record Journal</option>
<option value="auta">Autism</option>
<option value="dlia">Autism &amp; Developmental Language Impairments</option>
<option value="avbe">Avian and Poultry Biology Reviews</option>
<option value="avba">Avian Biology Research</option>
<option value="cria">AVMA Medical &amp; Legal Journal</option>
<option value="raea">Baptist Review and Expositor</option>
<option value="bcna">Behavioral and Cognitive Neuroscience Reviews</option>
<option value="bhda">Behavioral Disorders</option>
<option value="bmoa">Behavior Modification</option>
<option value="ccra">Behavior Science Notes</option>
<option value="ccrb">Behavior Science Research</option>
<option value="bbxa">Beyond Behavior</option>
<option value="btba">Biblical Theology Bulletin</option>
<option value="bdsa">Big Data &amp; Society</option>
<option value="bcia">Biochemistry Insights</option>
<option value="bbia">Bioinformatics and Biology Insights</option>
<option value="brna">Biological Research For Nursing</option>
<option value="bmia">Biomarker Insights</option>
<option value="bica">Biomarkers in Cancer</option>
<option value="beca">Biomedical Engineering and Computational Biology</option>
<option value="biia">Biomedical Informatics Insights</option>
<option value="bioa">BioScope: South Asian Screen Studies</option>
<option value="ulta">BMUS Bulletin</option>
<option value="boda">Body &amp; Society</option>
<option value="btra">Bone and Tissue Regeneration Insights</option>
<option value="bnaa">Brain and Neuroscience Advances</option>
<option value="bsaa">Brain Science Advances</option>
<option value="bcba">Breast Cancer: Basic and Clinical Research</option>
<option value="bjra">British Journalism Review</option>
<option value="dvda">The British Journal of Diabetes &amp; Vascular Disease</option>
<option value="bjia">British Journal of Infection Control</option>
<option value="uroa">British Journal of Medical and Surgical Urology</option>
<option value="bjmb">British Journal of Music Therapy</option>
<option value="bjod">British Journal of Occupational Therapy</option>
<option value="jooc">British Journal of Orthodontics</option>
<option value="bjpb">British Journal of Pain</option>
<option value="ppjc">British Journal of Perioperative Nursing (United Kingdom)</option>
<option value="bpia">The British Journal of Politics and International Relations</option>
<option value="ppjb">British Journal of Theatre Nursing (United Kingdom)</option>
<option value="jvib">British Journal of Visual Impairment</option>
<option value="mina">British Menopause Society Journal</option>
<option value="brqa">BRQ Business Research Quarterly</option>
<option value="jvub">Bruit</option>
<option value="buaa">Building Acoustics</option>
<option value="bsea">Building Services Engineering Research and Technology</option>
<option value="ijga">Bulletin (Centre for Women's Development Studies)</option>
<option value="aspa">Bulletin (Society for Applied Spectroscopy)</option>
<option value="sdia">Bulletin of Peace Proposals</option>
<option value="bsta">Bulletin of Science, Technology &amp; Society</option>
<option value="bmsa">Bulletin of Sociological Methodology/Bulletin de Méthodologie Sociologique</option>
<option value="bosb">Bulletin of the Atomic Scientists</option>
<option value="bosa">Bulletin of the Atomic Scientists of Chicago</option>
<option value="evjb">Bulletin of the Australasian Evaluation Society</option>
<option value="bulb">Bulletin of the Department of Secondary-School Principals of the National Education Association</option>
<option value="trja">Bulletin of the United States Institute for Textile Research, Inc</option>
<option value="phrc">Bulletins of the Public Health</option>
<option value="basa">Business &amp; Society</option>
<option value="bcqe">Business and Professional Communication Quarterly</option>
<option value="bcqd">Business Communication Quarterly</option>
<option value="bira">Business Information Review</option>
<option value="bpra">Business Perspectives and Research</option>
<option value="caea">Cahiers Élisabéthains</option>
<option value="csaa">Calcutta Statistical Association Bulletin</option>
<option value="cmra">California Management Review</option>
<option value="fmxb">CAM</option>
<option value="fmxc">CAM Journal</option>
<option value="fmxa">CAM Newsletter</option>
<option value="caja">Canadian Association of Radiologists Journal</option>
<option value="cjka">Canadian Journal of Kidney Health and Disease</option>
<option value="cjnb">Canadian Journal of Nursing Research</option>
<option value="cjoc">Canadian Journal of Occupational Therapy</option>
<option value="cjoa">Canadian Journal of Occupational Therapy</option>
<option value="cjob">Canadian Journal of Occupational Therapy and Physiotherapy</option>
<option value="psgb">Canadian Journal of Plastic Surgery</option>
<option value="cjsa">Canadian Journal of School Psychology</option>
<option value="cphb">Canadian Pharmacists Journal</option>
<option value="cphc">Canadian Pharmacists Journal / Revue des Pharmaciens du Canada</option>
<option value="cpaa">Canadian Psychiatric Association Journal</option>
<option value="ccxa">Cancer Control</option>
<option value="cgma">Cancer Growth and Metastasis</option>
<option value="cixa">Cancer Informatics</option>
<option value="cnca">Capital &amp; Class</option>
<option value="ccla">Cardiac Cath Lab Director</option>
<option value="ctoa">Cardiovascular and Thoracic Open</option>
<option value="vasa">Cardiovascular Surgery</option>
<option value="cdeb">Career Development and Transition for Exceptional Individuals</option>
<option value="cdea">Career Development for Exceptional Individuals</option>
<option value="cara">CARTILAGE</option>
<option value="cmma">Cell Medicine</option>
<option value="clla">Cell Transplantation</option>
<option value="crpa">Cellular Polymers</option>
<option value="crpb">Cellular Polymers</option>
<option value="cepa">Cephalalgia</option>
<option value="repa">Cephalalgia Reports</option>
<option value="chda">Childhood</option>
<option value="canb">Childhood Obesity and Nutrition</option>
<option value="clta">Child Language Teaching and Therapy</option>
<option value="cmxa">Child Maltreatment</option>
<option value="cnoa">Child Neurology Open</option>
<option value="cina">China Information</option>
<option value="chra">China Report</option>
<option value="chsa">Chinese Journal of Sociology</option>
<option value="csda">Chinese Sociological Dialogue</option>
<option value="ceja">Christian Education Journal</option>
<option value="cala">Christianity &amp; Literature</option>
<option value="chia">Chronic Illness</option>
<option value="crda">Chronic Respiratory Disease</option>
<option value="cssa">Chronic Stress</option>
<option value="csea">Citizenship, Social and Economics Education</option>
<option value="cpcf">Cleft Palate Journal</option>
<option value="claa">Clin-Alert</option>
<option value="cata">Clinical and Applied Thrombosis/Hemostasis</option>
<option value="ctna">Clinical and Translational Neuroscience</option>
<option value="ccsa">Clinical Case Studies</option>
<option value="ccpa">Clinical Child Psychology and Psychiatry</option>
<option value="eegb">Clinical EEG and Neuroscience</option>
<option value="eega">Clinical Electroencephalography</option>
<option value="ceta">Clinical Ethics</option>
<option value="icrb">Clinical Medicine: Case Reports</option>
<option value="amdb">Clinical medicine. Arthritis and musculoskeletal disorders</option>
<option value="bdxb">Clinical medicine. Blood disorders</option>
<option value="cicb">Clinical medicine. Cardiology</option>
<option value="crab">Clinical medicine. Circulatory, respiratory and pulmonary medicine</option>
<option value="entb">Clinical medicine. Ear, nose and throat</option>
<option value="endb">Clinical medicine. Endocrinology and diabetes</option>
<option value="cmgb">Clinical Medicine. Gastroenterology</option>
<option value="oncb">Clinical medicine. Oncology</option>
<option value="patb">Clinical medicine. Pathology</option>
<option value="pdib">Clinical medicine. Pediatrics</option>
<option value="rehb">Clinical medicine. Reproductive health</option>
<option value="thpb">Clinical Medicine. Therapeutics</option>
<option value="trib">Clinical medicine. Trauma and intensive medicine</option>
<option value="cmub">Clinical medicine. Urology</option>
<option value="cmwb">Clinical medicine. Women's health</option>
<option value="amda">Clinical Medicine Insights: Arthritis and Musculoskeletal Disorders</option>
<option value="bdxa">Clinical Medicine Insights: Blood Disorders</option>
<option value="cica">Clinical Medicine Insights: Cardiology</option>
<option value="icra">Clinical Medicine Insights: Case Reports</option>
<option value="craa">Clinical Medicine Insights: Circulatory, Respiratory and Pulmonary Medicine</option>
<option value="enta">Clinical Medicine Insights: Ear, Nose and Throat</option>
<option value="enda">Clinical Medicine Insights: Endocrinology and Diabetes</option>
<option value="cmga">Clinical Medicine Insights: Gastroenterology</option>
<option value="onca">Clinical Medicine Insights: Oncology</option>
<option value="pata">Clinical Medicine Insights: Pathology</option>
<option value="pdia">Clinical Medicine Insights: Pediatrics</option>
<option value="psya">Clinical Medicine Insights: Psychiatry</option>
<option value="reha">Clinical Medicine Insights: Reproductive Health</option>
<option value="thpa">Clinical Medicine Insights: Therapeutics</option>
<option value="tria">Clinical Medicine Insights: Trauma and Intensive Medicine</option>
<option value="cmua">Clinical Medicine Insights: Urology</option>
<option value="cmwa">Clinical Medicine Insights: Women's Health</option>
<option value="cnra">Clinical Nursing Research</option>
<option value="patc">Clinical Pathology</option>
<option value="cpja">Clinical Pediatrics</option>
<option value="cpxa">Clinical Psychological Science</option>
<option value="crea">Clinical Rehabilitation</option>
<option value="crib">Clinical Risk</option>
<option value="ctja">Clinical Trials</option>
<option value="ctra">Clothing and Textiles Research Journal</option>
<option value="cjxa">Collections</option>
<option value="clwb">Common Law World Review</option>
<option value="coma">Communication &amp; Sport</option>
<option value="ctpa">Communication and the Public</option>
<option value="cdqc">Communication Disorders Quarterly</option>
<option value="crxa">Communication Research</option>
<option value="crwa">Community College Review</option>
<option value="sgra">Comparative Group Studies</option>
<option value="cpsa">Comparative Political Studies</option>
<option value="cbrb">Compensation &amp; Benefits Review</option>
<option value="cbra">Compensation Review</option>
<option value="ccha">Competition &amp; Change</option>
<option value="crna">Competition and Regulation in Network Industries</option>
<option value="chpb">Complementary health practice review</option>
<option value="ppcb">Composite Polymers</option>
<option value="copa">Comprehensive Psychology</option>
<option value="sscc">Computers and the Social Sciences</option>
<option value="cera">Concurrent Engineering</option>
<option value="cmpb">Conflict Management and Peace Science</option>
<option value="jcra">Conflict Resolution</option>
<option value="ctca">Contact</option>
<option value="cdxa">Contemporary Drug Problems</option>
<option value="ceda">Contemporary Education Dialogue</option>
<option value="ciea">Contemporary Issues in Early Childhood</option>
<option value="hsaa">Contemporary Perspectives</option>
<option value="cmea">Contemporary Review of the Middle East</option>
<option value="csxa">Contemporary Sociology</option>
<option value="voda">Contemporary Voice of Dalit</option>
<option value="ctxa">Contexts</option>
<option value="jdsa">Contributions to Asian Studies</option>
<option value="cisa">Contributions to Indian Sociology</option>
<option value="cona">Convergence</option>
<option value="caca">Cooperation and Conflict</option>
<option value="cqxb">Cornell Hospitality Quarterly</option>
<option value="cqxa">Cornell Hotel and Restaurant Administration Quarterly</option>
<option value="cjba">Correctional Psychologist</option>
<option value="ecxa">Council review</option>
<option value="cora">Counseling Outcome Research and Evaluation</option>
<option value="cpha">CPJ</option>
<option value="cpce">Cranio - Facial Cleft Palate Bibliography</option>
<option value="cmta">Craniomaxillofacial Trauma &amp; Reconstruction</option>
<option value="cmoa">Craniomaxillofacial Trauma &amp; Reconstruction Open</option>
<option value="cmca">Crime, Media, Culture</option>
<option value="cadc">Crime &amp; Delinquency</option>
<option value="crja">Criminal Justice</option>
<option value="cjbb">Criminal Justice and Behavior</option>
<option value="cjpa">Criminal Justice Policy Review</option>
<option value="cjra">Criminal Justice Review</option>
<option value="crjb">Criminology &amp; Criminal Justice</option>
<option value="crra">Critical Research on Religion</option>
<option value="croa">Critical Reviews in Oral Biology &amp; Medicine</option>
<option value="avbb">Critical Reviews in Poultry Biology</option>
<option value="cspa">Critical Social Policy</option>
<option value="crsb">Critical Sociology</option>
<option value="csta">Critical Studies in Television</option>
<option value="coaa">Critique of Anthropology</option>
<option value="ccrc">Cross-Cultural Research</option>
<option value="cdya">Cultural Dynamics</option>
<option value="cgjb">cultural geographies</option>
<option value="psca">Cultural Hermeneutics</option>
<option value="cusa">Cultural Sociology</option>
<option value="csca">Cultural Studies ↔ Critical Methodologies</option>
<option value="capa">Culture &amp; Psychology</option>
<option value="cula">Cultures of Science</option>
<option value="cdpa">Current Directions in Psychological Science</option>
<option value="cbib">Currents in Biblical Research</option>
<option value="cbia">Currents in Research</option>
<option value="csia">Current Sociology</option>
<option value="irea">David Davies Memorial Institute of International Studies. Annual memorial lecture</option>
<option value="dema">Dementia</option>
<option value="dmra">Dementia and Neurodegeneration</option>
<option value="dcwa">Developmental Child Welfare</option>
<option value="dvra">Diabetes and Vascular Disease Research</option>
<option value="aeia">Diagnostique</option>
<option value="dhga">Dialogues in Human Geography</option>
<option value="aopc">DICP</option>
<option value="dhja">DIGITAL HEALTH</option>
<option value="dioa">Diogenes</option>
<option value="dcma">Discourse &amp; Communication</option>
<option value="dasa">Discourse &amp; Society</option>
<option value="disa">Discourse Studies</option>
<option value="dosb">Dose-Response</option>
<option value="drta">Dramatherapy</option>
<option value="dija">Drug Information Bulletin</option>
<option value="dijb">Drug Information Journal</option>
<option value="aopa">Drug Intelligence</option>
<option value="aopb">Drug Intelligence &amp; Clinical Pharmacy</option>
<option value="dspa">Drug Science, Policy and Law</option>
<option value="dtia">Drug Target Insights</option>
<option value="eara">Ear, Nose &amp; Throat Journal</option>
<option value="eqsa">Earthquake Spectra</option>
<option value="eepa">East European Politics and Societies</option>
<option value="roea">ECNU Review of Education</option>
<option value="eida">Economic and Industrial Democracy</option>
<option value="edqa">Economic Development Quarterly</option>
<option value="cgja">Ecumene</option>
<option value="esja">Education, Citizenship and Social Justice</option>
<option value="emab">Educational Administration</option>
<option value="emaa">Educational Administration Bulletin</option>
<option value="eaqa">Educational Administration Quarterly</option>
<option value="epma">Educational and Psychological Measurement</option>
<option value="epaa">Educational Evaluation and Policy Analysis</option>
<option value="ehma">Educational Horizons</option>
<option value="emac">Educational Management &amp; Administration</option>
<option value="emad">Educational Management Administration &amp; Leadership</option>
<option value="edna">Educational Neuroscience</option>
<option value="epxa">Educational Policy</option>
<option value="edra">Educational Researcher</option>
<option value="eusa">Education and Urban Society</option>
<option value="ldma">E-Learning and Digital Media</option>
<option value="enxa">Electronic News</option>
<option value="eaxa">Emerging Adulthood</option>
<option value="eeca">Emerging Economies Cases Journal</option>
<option value="emia">Emerging Economy Studies</option>
<option value="emra">Emotion Review</option>
<option value="arta">Empirical Studies of the Arts</option>
<option value="eaea">Energy &amp; Environment</option>
<option value="eeaa">Energy Exploration &amp; Exploitation</option>
<option value="eima">Engineering in Medicine</option>
<option value="ppcc">Engineering Plastics</option>
<option value="eexa">Entrepreneurship Education and Pedagogy</option>
<option value="etpb">Entrepreneurship Theory and Practice</option>
<option value="ehia">Environmental Health Insights</option>
<option value="elja">Environmental Law Review</option>
<option value="eaba">Environment and Behavior</option>
<option value="epna">Environment and Planning A: Economy and Space</option>
<option value="epba">Environment and Planning B: Planning and Design</option>
<option value="epbb">Environment and Planning B: Urban Analytics and City Science</option>
<option value="epca">Environment and Planning C: Government and Policy</option>
<option value="epcb">Environment and Planning C: Politics and Space</option>
<option value="epda">Environment and Planning D: Society and Space</option>
<option value="enea">Environment and Planning E: Nature and Space</option>
<option value="eaua">Environment and Urbanization</option>
<option value="euaa">Environment and Urbanization ASIA</option>
<option value="gaeb">Epigenetics Insights</option>
<option value="epib">Epilepsy Currents</option>
<option value="erga">Ergonomics in Design</option>
<option value="etna">Ethnicities</option>
<option value="etha">Ethnography</option>
<option value="eera">European Educational Research Journal</option>
<option value="acca">European Heart Journal: Acute Cardiovascular Care</option>
<option value="ehqb">European History Quarterly</option>
<option value="ejaa">European Journal of Archaeology</option>
<option value="cnua">European Journal of Cardiovascular Nursing</option>
<option value="cprb">European Journal of Cardiovascular Prevention &amp; Rehabilitation</option>
<option value="ejca">European Journal of Communication</option>
<option value="euca">European Journal of Criminology</option>
<option value="ecsa">European Journal of Cultural Studies</option>
<option value="ejda">European Journal of Industrial Relations</option>
<option value="ejia">European Journal of Inflammation</option>
<option value="ejta">European Journal of International Relations</option>
<option value="emsa">European Journal of Mass Spectrometry</option>
<option value="ejoa">European Journal of Ophthalmology</option>
<option value="epta">European Journal of Political Theory</option>
<option value="cprc">European Journal of Preventive Cardiology</option>
<option value="ejpa">European Journal of Probation</option>
<option value="ejsa">European Journal of Social Security</option>
<option value="esta">European Journal of Social Theory</option>
<option value="ejwa">European Journal of Women's Studies</option>
<option value="ella">European Labour Law Journal</option>
<option value="emsb">European Mass Spectrometry</option>
<option value="epea">European Physical Education Review</option>
<option value="isba">European Small Business Journal</option>
<option value="esoa">European Stroke Journal</option>
<option value="ehqa">European Studies Review</option>
<option value="eupa">European Union Politics</option>
<option value="eura">European Urban and Regional Studies</option>
<option value="euva">European View</option>
<option value="evia">Evaluation</option>
<option value="ehpa">Evaluation &amp; the Health Professions</option>
<option value="evja">Evaluation Journal of Australasia</option>
<option value="ajea">Evaluation News</option>
<option value="ajeb">Evaluation Practice</option>
<option value="erxa">Evaluation Quarterly</option>
<option value="erxb">Evaluation Review</option>
<option value="evba">Evolutionary Bioinformatics</option>
<option value="evpa">Evolutionary Psychology</option>
<option value="ecxc">Exceptional Children</option>
<option value="rseb">Exceptional Education Quarterly</option>
<option value="jmeb">Exchange: The Organizational Behavior Teaching Journal</option>
<option value="cbxa">Exosomes and Microvesicles</option>
<option value="ebmb">Experimental Biology and Medicine</option>
<option value="fisa">Families in Society</option>
<option value="fbra">Family Business Review</option>
<option value="fvea">Family Violence &amp; Ethnic Populations</option>
<option value="flra">Federal Law Review</option>
<option value="fapa">Feminism &amp; Psychology</option>
<option value="fcxa">Feminist Criminology</option>
<option value="fera">Feminist Review</option>
<option value="ftha">Feminist Theology</option>
<option value="ftya">Feminist Theory</option>
<option value="fmxd">Field Methods</option>
<option value="fiba">FIIB Business Review</option>
<option value="flaa">First Language</option>
<option value="foab">Focus on Autism and Other Developmental Disabilities</option>
<option value="foaa">Focus on Autistic Behavior</option>
<option value="fnba">Food and Nutrition Bulletin</option>
<option value="fstc">Food Science and Technology International</option>
<option value="faia">Foot &amp; Ankle</option>
<option value="faib">Foot &amp; Ankle International</option>

<option value="faoa">Foot &amp; Ankle Orthopaedics</option>
<option value="fasa">Foot &amp; Ankle Specialist</option>
<option value="ftra">Foreign Trade Review</option>
<option value="foia">Forum Italicum</option>
<option value="frca">French Cultural Studies</option>
<option value="gcta">G/C/T</option>
<option value="gaca">Games and Culture</option>
<option value="gaza">Gazette (Leiden, Netherlands)</option>
<option value="gtda">Gender, Technology and Development</option>
<option value="gasa">Gender &amp; Society</option>
<option value="gnga">Gender and the Genome</option>
<option value="gmtb">General Music Today</option>
<option value="grsa">Gene Regulation and Systems Biology</option>
<option value="gana">Genes &amp; Cancer</option>
<option value="gaea">Genetics &amp; Epigenetics</option>
<option value="gena">Genomics Insights</option>
<option value="slga">Georgia Government Review</option>
<option value="gosa">Geriatric Orthopaedic Surgery &amp; Rehabilitation</option>
<option value="gjha">German Journal of Human Resource Management</option>
<option value="ggma">Gerontology and Geriatric Medicine</option>
<option value="gcqb">Gifted Child Quarterly</option>
<option value="gctc">Gifted Child Today</option>
<option value="gctb">Gifted Child Today Magazine</option>
<option value="geia">Gifted Education International</option>
<option value="gtna">Giornale di Tecniche Nefrologiche e Dialitiche</option>
<option value="grha">Global &amp; Regional Health Technology Assessment</option>
<option value="gama">Global Advances in Health and Medicine</option>
<option value="gbra">Global Business Review</option>
<option value="pedb">Global Health Promotion</option>
<option value="emea">Global Journal of Emerging Market Economies</option>
<option value="gcha">Global Media and China</option>
<option value="gmca">Global Media and Communication</option>
<option value="gpha">Global Pediatric Health</option>
<option value="gqna">Global Qualitative Nursing Research</option>
<option value="gspa">Global Social Policy</option>
<option value="gsja">Global Spine Journal</option>
<option value="gsca">Global Studies of Childhood</option>
<option value="gomb">Group &amp; Organization Management</option>
<option value="goma">Group &amp; Organization Studies</option>
<option value="gaqa">Group Analysis</option>
<option value="gpia">Group Processes &amp; Intergroup Relations</option>
<option value="jhsa">Hand</option>
<option value="hana">HAND</option>
<option value="hpma">Handbook of Practice Management</option>
<option value="hthb">Hand Therapy</option>
<option value="wafa">Harbinger of Peace</option>
<option value="hija">Harvard International Journal of Press/Politics</option>
<option value="heaa">Health</option>
<option value="hmfa">Healthcare Management Forum</option>
<option value="hebc">Health Education &amp; Behavior</option>
<option value="heja">Health Education Journal</option>
<option value="heba">Health Education Monographs</option>
<option value="hebb">Health Education Quarterly</option>
<option value="jhia">Health Informatics</option>
<option value="jhib">Health Informatics Journal</option>
<option value="himc">Health Information Management</option>
<option value="himd">Health Information Management Journal</option>
<option value="hppa">Health Promotion Practice</option>
<option value="hpoa">Health Psychology Open</option>
<option value="hisa">Health Services Insights</option>
<option value="hsma">Health Services Management Research</option>
<option value="phrb">Health Services Reports</option>
<option value="hmea">Health Services Research and Managerial Epidemiology</option>
<option value="heia">Heart International</option>
<option value="hmxa">Henley Manager Update</option>
<option value="hera">HERD: Health Environments Research &amp; Design Journal</option>
<option value="hefa">Higher Education for the Future</option>
<option value="hipa">High Performance Polymers</option>
<option value="hpia">HIP International</option>
<option value="hcia">Hispanic Health Care International</option>
<option value="hjba">Hispanic Journal of Behavioral Sciences</option>
<option value="hsab">History and Sociology of South Asia</option>
<option value="hpya">History of Psychiatry</option>
<option value="hosa">History of Science</option>
<option value="hhsa">History of the Human Sciences</option>
<option value="hhcb">Home Health Care Management &amp; Practice</option>
<option value="hsxa">Homicide Studies</option>
<option value="hkja">Hong Kong Journal of Emergency Medicine</option>
<option value="hjoa">Hong Kong Journal of Occupational Therapy</option>
<option value="otrb">Hong Kong Journal of Orthopaedic Surgery</option>
<option value="jhtb">Hospitality Education and Research Journal</option>
<option value="jhtc">Hospitality Research Journal</option>
<option value="hpxa">Hospital Pharmacy</option>
<option value="phra">HSMHA Health Reports</option>
<option value="hetb">Human &amp; Experimental Toxicology</option>
<option value="hfsa">Human Factors</option>
<option value="huga">Human Geography</option>
<option value="hasa">Humanity &amp; Society</option>
<option value="huma">Human Relations</option>
<option value="hrda">Human Resource Development Review</option>
<option value="heta">Human Toxicology</option>
<option value="cana">ICAN: Infant, Child, &amp; Adolescent Nutrition</option>
<option value="icua">ICU Director</option>
<option value="iflb">IFLA Journal</option>
<option value="ksma">IIM Kozhikode Society &amp; Management Review</option>
<option value="icla">Illness, Crisis &amp; Loss</option>
<option value="ilra">ILR Review</option>
<option value="icaa">Imagination, Cognition and Personality</option>
<option value="iiia">Immunology and Immunogenetics Insights</option>
<option value="irpa">Implementation Research and Practice</option>
<option value="impa">Improving Schools</option>
<option value="ioca">Index on Censorship</option>
<option value="ihra">Indian Historical Review</option>
<option value="occa">Indian Journal of Clinical Cardiology</option>
<option value="icma">Indian Journal of Clinical Medicine</option>
<option value="ijca">Indian Journal of Corporate Governance</option>
<option value="ijgb">Indian Journal of Gender Studies</option>
<option value="jhda">Indian Journal of Human Development</option>
<option value="szja">Indian Journal of Psychological Medicine</option>
<option value="ipaa">Indian Journal of Public Administration</option>
<option value="iqqa">India Quarterly</option>
<option value="ibeb">Indoor and Built Environment</option>
<option value="ibea">Indoor Environment</option>
<option value="oaeb">Industrial &amp; Environmental Crisis Quarterly</option>
<option value="oaea">Industrial Crisis Quarterly</option>
<option value="ihea">Industry and Higher Education</option>
<option value="idra">Infectious Diseases: Research and Treatment</option>
<option value="ssia">Information (International Social Science Council)</option>
<option value="idva">Information Development</option>
<option value="ivia">Information Visualization</option>
<option value="inib">Innate Immunity</option>
<option value="inoa">InnovAiT</option>
<option value="inva">Innovations</option>
<option value="inqa">INQUIRY: The Journal of Health Care Organization, Provision, and Financing</option>
<option value="jvia">Insight</option>
<option value="ioaa">Insight on Africa</option>
<option value="icba">Institutionalised Children Explorations and Beyond</option>
<option value="crsa">Insurgent Sociologist</option>
<option value="icta">Integrative Cancer Therapies</option>
<option value="imia">Integrative Medicine Insights</option>
<option value="slra">Interlanguage studies bulletin (Utrecht)</option>
<option value="iasa">International Area Review</option>
<option value="iasb">International Area Studies Review</option>
<option value="ibmc">International Bulletin of Missionary Research</option>
<option value="ibmd">International Bulletin of Mission Research</option>
<option value="gazb">International Communication Gazette</option>
<option value="icja">International Criminal Justice Review</option>
<option value="ijxa">International Journal</option>
<option value="arxa">International Journal of Advanced Robotic Systems</option>
<option value="jaea">International Journal of Aeroacoustics</option>
<option value="jaca">International Journal of Architectural Computing</option>
<option value="jbda">International Journal of Behavioral Development</option>
<option value="ijba">International Journal of Bilingualism</option>
<option value="jobd">International Journal of Business Communication</option>
<option value="icpe">International Journal of Care Coordination</option>
<option value="icpd">International Journal of Care Pathways</option>
<option value="icec">International Journal of Christianity &amp; Education</option>
<option value="cosa">International Journal of Comparative Sociology</option>
<option value="ccma">International Journal of Cross Cultural Management</option>
<option value="icsa">International Journal of Cultural Studies</option>
<option value="ijda">International Journal of Damage Mechanics</option>
<option value="jdia">International Journal of Discrimination and the Law</option>
<option value="dsna">International Journal of Distributed Sensor Networks</option>
<option value="refa">International Journal of Educational Reform</option>
<option value="enba">International Journal of Engineering Business Management</option>
<option value="jera">International Journal of Engine Research</option>
<option value="ieia">The International Journal of Entrepreneurship and Innovation</option>
<option value="nana">International Journal of Green Nanotechnology</option>
<option value="joha">International Journal of Health Services</option>
<option value="hdea">International Journal of Heritage in the Digital Era</option>
<option value="ijia">International Journal of Immunopathology and Pharmacology</option>
<option value="insa">International Journal of Insect Science</option>
<option value="lrtc">International Journal of Lighting Research and Technology</option>
<option value="ijla">The International Journal of Lower Extremity Wounds</option>
<option value="ijha">International Journal of Maritime History</option>

<option value="mrea">International Journal of Market Research</option>
<option value="ijja">International Journal of Mechanical Engineering Education</option>
<option value="mava">International Journal of Micro Air Vehicles</option>
<option value="ijma">International Journal of Music Education</option>
<option value="ijod">International Journal of Offender Therapy</option>
<option value="ijoe">International Journal of Offender Therapy and Comparative Criminology</option>
<option value="psma">International Journal of Police Science &amp; Management</option>
<option value="prsa">International Journal of Protective Structures</option>
<option value="ijqa">International Journal of Qualitative Methods</option>
<option value="irma">International Journal of Rural Management</option>
<option value="sgrc">International Journal of Small Group Research</option>
<option value="ispa">International Journal of Social Psychiatry</option>
<option value="spsa">International Journal of Space Structures</option>
<option value="spoa">International Journal of Sports Science &amp; Coaching</option>
<option value="scda">International Journal of Spray and Combustion Dynamics</option>
<option value="stda">International Journal of STD &amp; AIDS</option>
<option value="wsoa">International Journal of Stroke</option>
<option value="ijsa">International Journal of Surgical Pathology</option>
<option value="thra">International Journal of Tourism and Hospitality Research</option>
<option value="ijtb">International Journal of Toxicology</option>
<option value="trya">International Journal of Tryptophan Research</option>
<option value="mrxa">International Migration Review</option>
<option value="jefb">International Nonwovens Journal</option>
<option value="iaba">International Political Science Abstracts</option>
<option value="ipsa">International Political Science Review</option>
<option value="ipra">International Polymer Science and Technology</option>
<option value="qcha">International Quarterly of Community Health Education</option>
<option value="irxa">International Regional Science Review</option>
<option value="ireb">International Relations</option>
<option value="irsb">International Review for the Sociology of Sport</option>
<option value="rasb">International Review of Administrative Sciences</option>
<option value="irqa">International Review of Qualitative Research</option>
<option value="irsa">International Review of Sport Sociology</option>
<option value="irva">International Review of Victimology</option>
<option value="isbb">International Small Business Journal</option>
<option value="iswb">International Social Work</option>
<option value="issa">International Sociology</option>
<option value="isqa">International Studies</option>
<option value="intc">Interpretation</option>
<option value="inea">Interventional Neuroradiology</option>
<option value="iscc">Intervention in School and Clinic</option>
<option value="jbta">Iowa State Journal of Business and Technical Communication</option>
<option value="ipea">i-Perception</option>
<option value="iesa">Irish Economic and Social History</option>
<option value="irja">Irish Journal of Sociology</option>
<option value="itqa">Irish Theological Quarterly</option>
<option value="jnra">Jadavpur Journal of International Relations</option>
<option value="jlab">JALA: Journal of the Association for Laboratory Automation</option>
<option value="jpma">Japanese Clinical Medicine</option>
<option value="jcta">JDR Clinical &amp; Translational Research</option>
<option value="brja">Jindal Journal of Business Research</option>
<option value="rshb">Journal (Royal Society of Health)</option>
<option value="rsea">Journal for Special Educators</option>
<option value="jegb">Journal for the Education of the Gifted</option>
<option value="jhaa">Journal for the History of Astronomy</option>
<option value="jnta">Journal for the Study of the New Testament</option>
<option value="jota">Journal for the Study of the Old Testament</option>
<option value="jspa">Journal for the Study of the Pseudepigrapha</option>
<option value="jvua">Journal for Vascular Ultrasound</option>
<option value="joua">Journalism</option>
<option value="jmoa">Journalism &amp; Communication Monographs</option>
<option value="jmcb">Journalism &amp; Mass Communication Educator</option>
<option value="jmqc">Journalism &amp; Mass Communication Quarterly</option>
<option value="jmqa">Journalism Bulletin</option>
<option value="jmqb">Journalism Quarterly</option>
<option value="jafa">Journal of Accounting, Auditing &amp; Finance</option>
<option value="jara">Journal of Adolescent Research</option>
<option value="adua">Journal of Adult and Continuing Education</option>
<option value="joac">Journal of Advanced Academics</option>
<option value="aada">Journal of Advanced Oral Research</option>
<option value="adva">Journal of Advertising Education</option>
<option value="jaha">Journal of Aging and Health</option>
<option value="acta">Journal of Algorithms &amp; Computational Technology</option>
<option value="jbfa">Journal of Applied Biomaterials &amp; Functional Materials</option>
<option value="jbfb">Journal of Applied Biomaterials and Biomechanics</option>
<option value="jaga">Journal of Applied Gerontology</option>
<option value="jaxc">Journal of Applied Social Science</option>
<option value="jaxa">Journal of Applied Sociology</option>
<option value="jasa">Journal of Asian and African Studies</option>
<option value="ecia">Journal of Asian Economic Integration</option>
<option value="aiaa">Journal of Asian Security and International Affairs</option>
<option value="jaaa">Journal of Asthma &amp; Allergy Educators</option>
<option value="jada">Journal of Attention Disorders</option>
<option value="sapa">Journal of Behavioural Science</option>
<option value="jbca">Journal of Bioactive and Compatible Polymers</option>
<option value="jbra">Journal of Biological Rhythms</option>
<option value="jbaa">Journal of Biomaterials Applications</option>
<option value="jbxa">Journal of Biomolecular Screening</option>
<option value="jbpa">Journal of Black Psychology</option>
<option value="jbsa">Journal of Black Studies</option>
<option value="cnsb">Journal of brain disease</option>
<option value="bjma">Journal of British Music Therapy</option>
<option value="jend">Journal of Building Physics</option>
<option value="jbtb">Journal of Business and Technical Communication</option>
<option value="joba">Journal of Business Communication</option>
<option value="cpta">Journal of Cardiovascular Pharmacology and Therapeutics</option>
<option value="cpra">Journal of Cardiovascular Risk</option>
<option value="jcaa">Journal of Career Assessment</option>
<option value="jcdb">Journal of Career Development</option>
<option value="jcda">Journal of Career Education</option>
<option value="jela">Journal of Cases in Educational Leadership</option>
<option value="clda">Journal of Cell Death</option>
<option value="cela">Journal of Cellular Plastics</option>
<option value="cnsa">Journal of Central Nervous System Disease</option>
<option value="jcba">Journal of Cerebral Blood Flow &amp; Metabolism</option>
<option value="chla">Journal of Chemical Research</option>
<option value="chca">Journal of Child Health Care</option>
<option value="cdqa">Journal of Childhool Communication Disorders</option>
<option value="jcna">Journal of Child Neurology</option>
<option value="cdqb">Journal of Children's Communication Development</option>
<option value="cwsa">Journal of Chinese Writing Systems</option>
<option value="icea">Journal of Christian Education</option>
<option value="jnla">Journal of Christian Education</option>
<option value="cejb">Journal of Christian Education: Original Series</option>
<option value="cbxb">Journal of Circulating Biomarkers</option>
<option value="jcsa">Journal of Classical Sociology</option>
<option value="urob">Journal of Clinical Urology</option>
<option value="jitb">Journal of Coated Fabrics</option>
<option value="jita">Journal of Coated Fibrous Materials</option>
<option value="edma">Journal of Cognitive Engineering and Decision Making</option>
<option value="csra">Journal of College Student Retention: Research, Theory &amp; Practice</option>
<option value="jfsb">Journal of Combustion Toxicology</option>
<option value="jcia">Journal of Communication Inquiry</option>
<option value="coba">Journal of Comorbidity</option>
<option value="aasa">Journal of Comparative Administration</option>
<option value="jcma">Journal of Composite Materials</option>
<option value="ccna">Journal of Concussion</option>
<option value="jcrb">Journal of Conflict Resolution</option>
<option value="jcoa">Journal of Connectivity</option>
<option value="joca">Journal of Consumer Culture</option>
<option value="jfsd">Journal of Consumer Product Flammability</option>
<option value="ccja">Journal of Contemporary Criminal Justice</option>
<option value="jcec">Journal of Contemporary Ethnography</option>
<option value="jcha">Journal of Contemporary History</option>
<option value="jcxa">Journal of Correctional Health Care</option>
<option value="jcva">Journal of Creating Value</option>
<option value="crca">Journal of Creative Communications</option>
<option value="jcca">Journal of Cross-Cultural Psychology</option>
<option value="ccaa">Journal of Current Chinese Affairs</option>
<option value="saaa">Journal of Current Southeast Asian Affairs</option>
<option value="cmsa">Journal of Cutaneous Medicine and Surgery</option>
<option value="dmsa">The Journal of Defense Modeling and Simulation</option>
<option value="jdrb">Journal of Dental Research</option>
<option value="jdsb">Journal of Developing Societies</option>
<option value="jdpa">Journal of Development Policy and Practice</option>
<option value="dsta">Journal of Diabetes Science and Technology</option>
<option value="jdma">Journal of Diagnostic Medical Sonography</option>
<option value="dpsa">Journal of Disability Policy Studies</option>
<option value="drea">Journal of Drug Education</option>
<option value="joda">Journal of Drug Issues</option>
<option value="ecla">Journal of Early Childhood Literacy</option>
<option value="ecra">Journal of Early Childhood Research</option>
<option value="jeib">Journal of Early Intervention</option>
<option value="jexa">Journal of Education</option>
<option value="jebb">Journal of Educational and Behavioral Statistics</option>
<option value="jeca">Journal of Educational Computing Research</option>
<option value="jeba">Journal of Educational Statistics</option>

<option value="etsa">Journal of Educational Technology Systems</option>
<option value="iceb">Journal of Education and Christian Belief</option>
<option value="jsda">Journal of Education for Sustainable Development</option>
<option value="jepb">Journal of Elastomers &amp; Plastics</option>
<option value="jepa">Journal of Elastoplastics</option>
<option value="emfa">Journal of Emerging Market Finance</option>
<option value="ebxa">Journal of Emotional and Behavioral Disorders</option>
<option value="jrea">Journal of Empirical Research on Human Research Ethics</option>
<option value="pevb">Journal of Endometriosis</option>
<option value="peva">Journal of Endometriosis and Pelvic Pain Disorders</option>
<option value="inia">Journal of Endotoxin Research</option>
<option value="jeta">Journal of Endovascular Therapy</option>
<option value="jefa">Journal of Engineered Fibers and Fabrics</option>
<option value="enga">Journal of English Linguistics</option>
<option value="eiea">Journal of Entrepreneurship and Innovation in Emerging Economies</option>
<option value="ensa">Journal of Eurasian Studies</option>
<option value="espa">Journal of European Social Policy</option>
<option value="jesa">Journal of European Studies</option>
<option value="chpc">Journal of Evidence-Based Complementary &amp; Alternative Medicine</option>
<option value="chpd">Journal of Evidence-Based Integrative Medicine</option>
<option value="ecxb">Journal of Exceptional Children</option>
<option value="jeea">Journal of Experiential Education</option>
<option value="exna">Journal of Experimental Neuroscience</option>
<option value="eppa">Journal of Experimental Psychopathology</option>
<option value="jfha">Journal of Family History</option>
<option value="jfia">Journal of Family Issues</option>
<option value="jfna">Journal of Family Nursing</option>
<option value="jfma">Journal of Feline Medicine and Surgery</option>
<option value="jora">Journal of Feline Medicine and Surgery Open Reports</option>
<option value="jfsa">Journal of Fire &amp; Flammability</option>
<option value="jfea">Journal of Fire Protection Engineering</option>
<option value="jfsc">Journal of Fire Retardant Chemistry</option>
<option value="jfse">Journal of Fire Sciences</option>
<option value="gema">Journal of General Management</option>
<option value="jgma">Journal of Generic Medicines</option>
<option value="jgpb">Journal of Geriatric Psychiatry and Neurology</option>
<option value="jhsb">Journal of Hand Surgery</option>
<option value="jhsc">Journal of Hand Surgery (European Volume)</option>
<option value="hsba">Journal of Health and Human Behavior</option>
<option value="hsbb">Journal of Health and Social Behavior</option>
<option value="jhma">Journal of Health Management</option>
<option value="hpqa">Journal of Health Psychology</option>
<option value="hsrb">Journal of Health Services Research &amp; Policy</option>
<option value="hmja">Journal of Heritage Management</option>
<option value="jhha">Journal of Hispanic Higher Education</option>
<option value="jhca">Journal of Histochemistry &amp; Cytochemistry</option>
<option value="jhrb">Journal of Historical Research in Music Education</option>
<option value="jhna">Journal of Holistic Nursing</option>
<option value="hhca">Journal of Home Health Care Practice</option>
<option value="jhtd">Journal of Hospitality &amp; Tourism Research</option>
<option value="jhta">Journal of Hospitality Education</option>
<option value="jhpa">Journal of Humanistic Psychology</option>
<option value="jhla">Journal of Human Lactation</option>
<option value="jhva">Journal of Human Values</option>
<option value="iema">Journal of Inborn Errors of Metabolism and Screening</option>
<option value="jioa">Journal of Indian Orthodontic Society</option>
<option value="jira">Journal of Industrial Relations</option>
<option value="jitc">Journal of Industrial Textiles</option>
<option value="bjib">Journal of Infection Prevention</option>
<option value="jisb">Journal of Information Science</option>
<option value="jina">Journal of Information Technology</option>
<option value="ttca">Journal of Information Technology Teaching Cases</option>
<option value="joia">Journal of Infrastructure Development</option>
<option value="icpb">Journal of Integrated Care</option>
<option value="icpc">Journal of integrated Care Pathways</option>
<option value="jldc">Journal of Intellectual Disabilities</option>
<option value="jima">Journal of Intelligent Material Systems and Structures</option>
<option value="jica">Journal of Intensive Care Medicine</option>
<option value="jiea">Journal of Interdisciplinary Economics</option>
<option value="lsra">Journal of International Life Sciences Research</option>
<option value="jiga">Journal of International Marketing</option>
<option value="imra">Journal of International Medical Research</option>
<option value="iptb">Journal of International Political Theory</option>
<option value="jiva">Journal of Interpersonal Violence</option>
<option value="hica">Journal of Investigative Medicine High Impact Case Reports</option>
<option value="jlac">Journal of Laboratory Automation</option>
<option value="lrsa">Journal of Land and Rural Studies</option>
<option value="jlsa">Journal of Language and Social Psychology</option>
 <option value="jlob">Journal of Leadership &amp; Organizational Studies</option>
<option value="jloa">Journal of Leadership Studies</option>
<option value="ldxa">Journal of Learning Disabilities</option>
<option value="jldb">Journal of Learning Disabilities</option>
<option value="jlda">Journal of Learning Disabilities for Nursing, Health, and Social Care</option>
<option value="lisa">Journal of librarianship</option>
<option value="lisb">Journal of Librarianship and Information Science</option>
<option value="jlrb">Journal of Literacy Research</option>
<option value="lfna">Journal of Low Frequency Noise, Vibration and Active Control</option>
<option value="jmka">Journal of Macromarketing</option>
<option value="icpa">Journal of Managed Care</option>
<option value="joma">Journal of Management</option>
<option value="jmed">Journal of Management Education</option>
<option value="jmia">Journal of Management Inquiry</option>
<option value="jmxa">Journal of Marketing</option>
<option value="ppob">Journal of Marketing &amp; Public Policy</option>
<option value="jmda">Journal of Marketing Education</option>
<option value="mrja">Journal of Marketing Research</option>
<option value="mcua">Journal of Material Culture</option>
<option value="jmsa">Journal of Mechanical Engineering Science</option>
<option value="jmba">Journal of Medical Biography</option>
<option value="mdea">Journal of Medical Education and Curricular Development</option>
<option value="mmja">Journal of Medical Marketing</option>
<option value="msca">Journal of Medical Screening</option>
<option value="jmfa">Journal of Micromanufacturing</option>
<option value="mmra">Journal of Mixed Methods Research</option>
<option value="meha">Journal of Modern European History</option>
<option value="jmta">Journal of Music Teacher Education</option>
<option value="jlub">Journal of National Law University Delhi</option>
<option value="jnsa">Journal of Near Infrared Spectroscopy</option>
<option value="nnta">Journal of Neonatology</option>
<option value="crnb">Journal of Network Industries</option>
<option value="nnra">Journal of Neurologic Rehabilitation</option>
<option value="ocsb">Journal of Ocean and Climate</option>
<option value="ijoc">Journal of Offender Therapy</option>
<option value="aexa">Journal of Omicron Chi Epsilon</option>
<option value="oppa">Journal of Oncology Pharmacy Practice</option>
<option value="jnpa">Journal of Onco-Nephrology</option>
<option value="ospa">Journal of Operations and Strategic Planning</option>
<option value="jooa">Journal of Orthodontics</option>
<option value="otra">Journal of Orthopaedics, Trauma and Rehabilitation</option>
<option value="osja">Journal of Orthopaedic Surgery</option>
<option value="pala">Journal of Palliative Care</option>
<option value="pena">Journal of Parenteral and Enteral Nutrition</option>
<option value="pccb">Journal of Pastoral Care</option>
<option value="pcca">Journal of Pastoral Care &amp; Counseling</option>
<option value="jpxa">Journal of Patient Experience</option>
<option value="cric">Journal of Patient Safety and Risk Management</option>
<option value="jpda">Journal of Peacebuilding &amp; Development</option>
<option value="jpra">Journal of Peace Research</option>
<option value="cmpa">Journal of Peace Science</option>
<option value="jpob">Journal of Pediatric Oncology Nursing</option>
<option value="ppja">Journal of Perioperative Practice</option>
<option value="jppa">Journal of Pharmacy Practice</option>
<option value="pmta">Journal of Pharmacy Technology</option>
<option value="jpea">Journal of Planning Education and Research</option>
<option value="jpha">Journal of Planning History</option>
<option value="jplb">Journal of Planning Literature</option>
<option value="jpfa">Journal of Plastic Film &amp; Sheeting</option>
<option value="pnza">Journal of Political Science</option>
<option value="plaa">Journal of Politics in Latin America</option>
<option value="pbia">Journal of Positive Behavior Interventions</option>
<option value="prva">Journal of Prevention and Health Promotion</option>
<option value="jpca">Journal of Primary Care &amp; Community Health</option>
<option value="tpjc">Journal of Prison Discipline and Philanthropy (1857)</option>
<option value="jpsa">Journal of Psoriasis and Psoriatic Arthritis</option>
<option value="jpaa">Journal of Psychoeducational Assessment</option>
<option value="ptja">Journal of Psychology and Theology</option>
<option value="jopa">Journal of Psychopharmacology</option>
<option value="ssha">Journal of Psychosexual Health</option>
<option value="ppoa">Journal of Public Policy &amp; Marketing</option>
<option value="jlra">Journal of Reading Behavior</option>
<option value="jrta">Journal of Rehabilitation and Assistive Technologies Engineering</option>
<option value="jrpa">Journal of Reinforced Plastics and Composites</option>
<option value="rbfa">Journal of Reproductive and Stem Cell Biotechnology</option>
<option value="rbfb">Journal of Reproductive Biotechnology and Fertility</option>
<option value="jrca">Journal of Research in Crime and Delinquency</option>
<option value="jria">Journal of Research in International Education</option>
<option value="jrma">Journal of Research in Music Education</option>
 <option value="jrnb">Journal of Research in Nursing</option>
<option value="jrla">Journal of Research on Leadership Education</option>
<option value="jsma">Journal of Sandwich Structures &amp; Materials</option>
<option value="jsla">Journal of School Leadership</option>
<option value="jsnb">The Journal of School Nursing</option>
<option value="jsoa">Journal of Scleroderma and Related Disorders</option>
<option value="joab">Journal of Secondary Gifted Education</option>
<option value="jsra">Journal of Service Research</option>
<option value="seaa">Journal of Shoulder and Elbow Arthroplasty</option>
<option value="spra">Journal of Social and Personal Relationships</option>
<option value="jsaa">Journal of Social Archaeology</option>
<option value="sisa">Journal of Social Inclusion Studies</option>
<option value="jswa">Journal of Social Work</option>
<option value="josb">Journal of Sociology</option>
<option value="sada">Journal of South Asian Development</option>
<option value="jsta">Journal of Special Education Technology</option>
<option value="jsfa">Journal of Spiritual Formation and Soul Care</option>
<option value="jssa">Journal of Sport and Social Issues</option>
<option value="jsea">Journal of Sports Economics</option>
<option value="sdja">Journal of Strain Analysis</option>
<option value="jsca">Journal of Strategic Contracting and Negotiation</option>
<option value="stma">Journal of Stroke Medicine</option>
<option value="jsia">Journal of Studies in International Education</option>
<option value="jtea">Journal of Teacher Education</option>
<option value="jtwa">Journal of Technical Writing and Communication</option>
<option value="jtta">Journal of Telemedicine and Telecare</option>
<option value="texa">Journal of Textiles and Fibrous Materials</option>
<option value="jama">Journal of the Academy of Marketing Science</option>
<option value="apba">Journal of the American Biological Safety Association</option>
<option value="ijta">Journal of the American College of Toxicology</option>
<option value="japa">Journal of the American Psychiatric Nurses Association</option>
<option value="apaa">Journal of the American Psychoanalytic Association</option>
<option value="ansa">Journal of the Anthropological Survey of India</option>
<option value="rpsc">Journal of the Association for Persons with Severe Handicaps</option>
<option value="rpsb">Journal of the Association for the Severely Handicapped</option>
<option value="bjoa">Journal of the Association of Occupational Therapists</option>
<option value="jpoa">Journal of the Association of Pediatric Oncology Nurses</option>
<option value="jeia">Journal of the Division for Early Childhood</option>
<option value="crua">Journal of the ICRU</option>
<option value="jila">Journal of the Institution of Locomotive Engineers</option>
<option value="inca">Journal of the Intensive Care Society</option>
<option value="jiaa">Journal of the International Association of Physicians in AIDS Care</option>
<option value="jiab">Journal of the International Association of Providers of AIDS Care (JIAPAC)</option>
<option value="jtpa">Journal of Theoretical Politics</option>
<option value="jraa">Journal of the Renin-Angiotensin-Aldosterone System</option>
<option value="jenc">Journal of Thermal Envelope and Building Science</option>
<option value="jena">Journal of Thermal Insulation</option>
<option value="jenb">Journal of Thermal Insulation and Building Envelopes</option>
<option value="jtca">Journal of Thermoplastic Composite Materials</option>
<option value="rsha">Journal of the Royal Sanitary Institute</option>
<option value="rshe">Journal of the Royal Society for the Promotion of Health</option>
<option value="rshd">Journal of the Royal Society of Health</option>
<option value="jrsb">Journal of the Royal Society of Medicine</option>
<option value="rshh">Journal of the Sanitary Institute</option>
<option value="rsxa">Journal of the Society for Gynecologic Investigation</option>
<option value="osjb">Journal of the Western Pacific Orthopaedic Association</option>
<option value="teja">Journal of Tissue Engineering</option>
<option value="tcna">Journal of Transcultural Nursing</option>
<option value="jtda">Journal of Transformative Education</option>
<option value="pita">Journal of Transplant Coordination</option>
<option value="jtrb">Journal of Travel Research</option>
<option value="juha">Journal of Urban History</option>
<option value="jvma">Journal of Vacation Marketing</option>
<option value="vmja">Journal of Vascular Medicine and Biology</option>
<option value="jvuc">Journal of Vascular Technology</option>
<option value="jovb">Journal of Veterinary Dentistry</option>
<option value="vdia">Journal of Veterinary Diagnostic Investigation</option>
<option value="jvcb">Journal of Vibration and Control</option>
<option value="vvja">Journal of Victimology and Victim Justice</option>
<option value="vcua">Journal of Visual Culture</option>
<option value="jvba">Journal of Visual Impairment &amp; Blindness</option>
<option value="vrda">Journal of VitreoRetinal Diseases</option>
<option value="nvsa">Journal of Voluntary Action Research</option>
<option value="wcca">Journal of White Collar and Corporate Crime</option>
<option value="jwba">Journal of Wide Bandgap Materials</option>
<option value="mhsa">Journal on Migration and Human Security</option>
<option value="cvda">JRSM Cardiovascular Disease</option>
<option value="shrb">JRSM Open</option>
<option value="shra">JRSM Short Reports</option>
<option value="jrxa">Justice Research and Policy</option>
<option value="scxa">Knowledge</option>
<option value="lana">Laboratory Animals</option>
<option value="jlaa">Laboratory Automation News</option>
<option value="lsja">Labor Studies Journal</option>
<option value="linb">Language and Linguistics</option>
<option value="lala">Language and Literature</option>
<option value="lasa">Language and Speech</option>
<option value="ltra">Language Teaching Research</option>
<option value="ltja">Language Testing</option>
<option value="lapa">Latin American Perspectives</option>
<option value="lcha">Law, Culture and the Humanities</option>
<option value="lmeb">Law, Medicine and Health Care</option>
<option value="leaa">Leadership</option>
<option value="ldqa">Learning Disability Quarterly</option>
<option value="alja">Legal Service Bulletin</option>
<option value="lrtd">Lighting Research &amp; Technology</option>
<option value="lrtb">Lighting Research &amp; Technology</option>
<option value="lixa">Lipid Insights</option>
<option value="lrxe">Literacy Research: Theory, Method, and Practice</option>
<option value="lrxd">Literacy Research Association Yearbook</option>
<option value="laha">Literature &amp; History</option>
<option value="leca">Local Economy</option>
<option value="lupa">Lupus</option>
<option value="maaa">Maastricht Journal of European and Comparative Law</option>
<option value="mria">Magnetic Resonance Insights</option>
<option value="moha">Management &amp; Organizational History</option>
<option value="mlsa">Management and Labour Studies</option>
<option value="mcqa">Management Communication Quarterly</option>
<option value="mlqa">Management Education and Development</option>
<option value="miea">Management in Education</option>
<option value="mlqb">Management Learning</option>
<option value="mtra">Management Teaching Review</option>
<option value="mara">Margin: The Journal of Applied Economic Research</option>
<option value="mtqa">Marketing Theory</option>
<option value="mreb">Market Research Society. Journal.</option>
<option value="mmsa">Mathematics and Mechanics of Solids</option>
<option value="mppa">MDM Policy &amp; Practice</option>
<option value="maca">Measurement and Control</option>
<option value="mecb">Measurement and Evaluation in Counseling and Development</option>
<option value="meca">Measurement and Evaluation in Guidance</option>
<option value="mcsa">Media, Culture &amp; Society</option>
<option value="mwca">Media, War &amp; Conflict</option>
<option value="miaa">Media Information Australia</option>
<option value="miad">Media International Australia</option>
<option value="miab">Media International Australia</option>
<option value="miac">Media International Australia incorporating Culture and Policy</option>
<option value="mcrd">Medical Care Research and Review</option>
<option value="mcrc">Medical Care Review</option>
<option value="mdma">Medical Decision Making</option>
<option value="meia">Medical Equipment Insights</option>
<option value="mlia">Medical Law International</option>
<option value="mljb">Medicao-Legal and Criminological Review</option>
<option value="msla">Medicine, Science and the Law</option>
<option value="mapa">Medicine Access @ Point of Care</option>
<option value="mljc">Medico-Legal Journal</option>
<option value="lmea">Medicolegal News</option>
<option value="mssa">Memory Studies</option>
<option value="jmma">Men and Masculinities</option>
<option value="minb">Menopause International</option>
<option value="meta">Metamorphosis</option>
<option value="miob">Methodological Innovations</option>
<option value="mioa">Methodological Innovations Online</option>
<option value="mbia">Microbiology Insights</option>
<option value="arpa">Midwest Review of Public Administration</option>
<option value="mlaa">Millennial Asia</option>
<option value="mila">Millennium</option>
<option value="misb">Missiology</option>
<option value="mmca">Mobile Media &amp; Communication</option>
<option value="jvca">Modal Analysis</option>
<option value="mcxa">Modern China</option>
<option value="mixa">Molecular Imaging</option>
<option value="mpxa">Molecular Pain</option>
<option value="msja">Multiple Sclerosis Journal</option>
<option value="msoa">Multiple Sclerosis Journal - Experimental, Translational and Clinical</option>
<option value="mnsa">Music &amp; Science</option>
<option value="msxa">Musicae Scientiae</option>
<option value="mejc">Music Educators Journal</option>
<option value="meja">Music Supervisors' Bulletin</option>
<option value="mejb">Music Supervisors' Journal</option>
<option value="naba">Nanobiomedicine</option>
<option value="naxa">Nanomaterials and Nanotechnology</option>
<option value="nasa">NASNewsletter</option>
<option value="nasb">NASN School Nurse</option>
<option value="buld">NASSP Bulletin</option>
<option value="nera">National Institute Economic Review</option>
<option value="jmxb">National Marketing Review</option>
<option value="srxb">National Sculpture Review</option>
<option value="npxa">Natural Product Communications</option>
<option value="ncta">NCTR Newsletter</option>
<option value="npca">Nephrology @ Point of Care</option>
<option value="nrra">Nephrology Research &amp; Reviews</option>
<option value="nqha">Netherlands Quarterly of Human Rights</option>
<option value="nnrb">Neurorehabilitation and Neural Repair</option>
<option value="exnb">Neuroscience Insights</option>
<option value="njea">New Journal of European Criminal Law</option>
<option value="nlfa">New Labor Forum</option>
<option value="nmsa">New Media &amp; Society</option>
<option value="npsa">New Perspectives</option>
<option value="tpsa">Newsletter, Transcultural Research in Mental Health Problems</option>
<option value="stha">Newsletter of the Program on Public Conceptions of Science</option>
<option value="sthc">Newsletter on Science, Technology &amp; Human Values</option>
<option value="newa">NEW SOLUTIONS: A Journal of Environmental and Occupational Health Policy</option>
<option value="nrja">Newspaper Research Journal</option>
<option value="nhra">NHRD Network Journal</option>
<option value="nctc">Nineteenth Century Theatre</option>
<option value="nctd">Nineteenth Century Theatre and Film</option>
<option value="nctb">Nineteenth Century Theatre Research</option>
<option value="nira">NIR news</option>
<option value="nvwa">Noise &amp; Vibration Worldwide</option>
<option value="dosa">Nonlinearity in Biology, Toxicology, Medicine</option>
<option value="nvsb">Nonprofit and Voluntary Sector Quarterly</option>
<option value="njna">Nordic Journal of Nursing Research</option>
<option value="nada">Nordic Studies on Alcohol and Drugs</option>
<option value="nadc">Nordisk Alkoholtisdkrift (Nordic Alcohol Studies)</option>
<option value="naaa">North American Archaeologist</option>
<option value="cada">NPPA Journal</option>
<option value="jrna">NT Research</option>
<option value="nrsa">Nuclear Receptor Signaling</option>
<option value="neja">Nursing Ethics</option>
<option value="cjna">Nursing Papers - Perspectives en Nursing</option>
<option value="nsqa">Nursing Science Quarterly</option>
<option value="naha">Nutrition and Health</option>
<option value="nmia">Nutrition and Metabolic Insights</option>
<option value="ncpa">Nutrition in Clinical Practice</option>
<option value="obma">Obstetric Medicine</option>
<option value="ibma">Occasional Bulletin from the Missionary Research Library</option>
<option value="ibmb">Occasional Bulletin of Missionary Research</option>
<option value="whsb">Occupational Health Nursing</option>
<option value="bjob">Occupational Therapy: the Official Journal of the Association of Occupational Therapists</option>
<option value="omea">OMEGA - Journal of Death and Dying</option>
<option value="ojca">Open Journal of Cardiovascular Surgery</option>
<option value="opca">Ophthalmology @ Point of Care</option>
<option value="oeda">Ophthalmology and Eye Diseases</option>
<option value="orga">Organization</option>
<option value="oaec">Organization &amp; Environment</option>
<option value="jmec">Organizational Behavior Teaching Review</option>
<option value="opra">Organizational Psychology Review</option>
<option value="orma">Organizational Research Methods</option>
<option value="ossa">Organization Studies</option>
<option value="otta">Organization Theory</option>
<option value="ojsa">Orthopaedic Journal of Sports Medicine</option>
<option value="otjb">OTJR: Occupation, Participation and Health</option>
<option value="otof">Otolaryngology</option>
<option value="otoj">Otolaryngology–Head and Neck Surgery</option>
<option value="opna">OTO Open</option>
<option value="oaga">Outlook on Agriculture</option>
<option value="paaa">Pacifica</option>
<option value="spxa">Pacific Sociological Review</option>
<option value="pcra">Palliative Care: Research and Treatment</option>
<option value="pcrb">Palliative Care and Social Practice</option>
<option value="pmja">Palliative Medicine</option>
<option value="para">Paradigm</option>
<option value="ppqa">Party Politics</option>
<option value="veta">Pathologia veterinaria</option>
<option value="phpa">Pedagogy in Health Promotion</option>
<option value="pdpa">Pediatric and Developmental Pathology</option>
<option value="peca">Perception</option>
<option value="pmsb">Perceptual and Motor Skills</option>
<option value="pmsa">Perceptual and Motor Skills Research Exchange</option>
<option value="prfa">Perfusion</option>
<option value="ptda">Peritoneal Dialysis International</option>
<option value="pspc">Personality and Social Psychology Bulletin</option>
<option value="psra">Personality and Social Psychology Review</option>
<option value="ppma">Personnel Administration</option>
<option value="ppmc">Personnel Administration and Public Personnel Review</option>
<option value="pmda">Perspectives in Medicinal Chemistry</option>
<option value="rshi">Perspectives in Public Health</option>
<option value="pvsa">Perspectives in Vascular Surgery and Endovascular Therapy</option>
<option value="ppsa">Perspectives on Psychological Science</option>
<option value="pdka">Phi Delta Kappan</option>
<option value="pscb">Philosophy &amp; Social Criticism</option>
<option value="posa">Philosophy of the Social Sciences</option>
<option value="phla">Phlebology</option>
<option value="plta">Planning Theory</option>
<option value="psga">Plastic Surgery</option>
<option value="pcsa">Plastic Surgery Case Studies</option>
<option value="plra">PLEURA</option>
<option value="pqxa">Police Quarterly</option>
<option value="ppna">Policy, Politics, &amp; Nursing Practice</option>
<option value="pfea">Policy Futures in Education</option>
<option value="bbsa">Policy Insights from the Behavioral and Brain Sciences</option>
<option value="plia">Political Insight</option>
<option value="absa">Political Research, Organization and Design</option>
<option value="prqb">Political Research Quarterly</option>
<option value="pnzb">Political Science</option>
<option value="psxa">Political Studies</option>
<option value="pswa">Political Studies Review</option>
<option value="ptxa">Political Theory</option>
<option value="pola">Politics</option>
<option value="ppea">Politics, Philosophy &amp; Economics</option>
<option value="pasa">Politics &amp; Society</option>
<option value="ipta">Politics and Ethics Review</option>
<option value="ppca">Polymers and Polymer Composites</option>
<option value="prra">Polymers from Renewable Resources</option>
<option value="minc">Post Reproductive Health</option>
<option value="avbd">Poultry and Avian Biology Reviews</option>
<option value="avbc">Poultry Science Reviews</option>
<option value="paea">Power and Education</option>
<option value="misa">Practical Anthropology</option>
<option value="prdb">Primary Dental Care</option>
<option value="prda">Primary Dental Journal</option>
<option value="prba">Probation</option>
<option value="prbb">Probation Journal</option>
<option value="psha">Proceedings of Singapore Healthcare</option>
<option value="lrxa">Proceedings of Southwest Reading Conference for Colleges and Universities</option>
<option value="proa">Proceedings of the Annual Meeting of the Human Factors Society</option>
<option value="acba">Proceedings of the Association of Clinical Biochemists</option>
<option value="pspa">Proceedings of the Division of Personality and Society Psychology</option>
<option value="proe">Proceedings of the Human Factors and Ergonomics Society Annual Meeting</option>
<option value="prob">Proceedings of the Human Factors Society Annual Meeting</option>
<option value="paua">Proceedings of the Institution of Automobile Engineers</option>
<option value="pmea">Proceedings of the Institution of Mechanical Engineers</option>
<option value="pcpa">Proceedings of the Institution of Mechanical Engineers, Conference Proceedings</option>
<option value="piac">Proceedings of the Institution of Mechanical Engineers, Part A: Journal of Power and Energy</option>
<option value="piab">Proceedings of the Institution of Mechanical Engineers, Part A: Journal of Power Engineering</option>
<option value="piaa">Proceedings of the Institution of Mechanical Engineers, Part A: Power and Process Engineering</option>
<option value="pibb">Proceedings of the Institution of Mechanical Engineers, Part B: Journal of Engineering Manufacture</option>
<option value="piba">Proceedings of the Institution of Mechanical Engineers, Part B: Management and engineering manufacture</option>
<option value="picb">Proceedings of the Institution of Mechanical Engineers, Part C: Journal of Mechanical Engineering Science</option>
<option value="pica">Proceedings of the Institution of Mechanical Engineers, Part C: Mechanical Engineering Science</option>
<option value="pidb">Proceedings of the Institution of Mechanical Engineers, Part D: Journal of Automobile Engineering</option>
<option value="pida">Proceedings of the Institution of Mechanical Engineers, Part D: Transport Engineering</option>
<option value="piea">Proceedings of the Institution of Mechanical Engineers, Part E: Journal of Process Mechanical Engineering</option>
<option value="pifa">Proceedings of the Institution of Mechanical Engineers, Part F: Journal of Rail and Rapid Transit</option>
<option value="piga">Proceedings of the Institution of Mechanical Engineers, Part G: Journal of Aerospace Engineering</option>
<option value="pihb">Proceedings of the Institution of Mechanical Engineers, Part H: Journal of Engineering in Medicine</option>
<option value="piia">Proceedings of the Institution of Mechanical Engineers, Part I: Journal of Systems and Control Engineering</option>
<option value="pija">Proceedings of the Institution of Mechanical Engineers, Part J: Journal of Engineering Tribology</option>
<option value="pika">Proceedings of the Institution of Mechanical Engineers, Part K: Journal of Multi-body Dynamics</option>
<option value="pila">Proceedings of the Institution of Mechanical Engineers, Part L: Journal of Materials: Design and Applications</option>
<option value="pima">Proceedings of the Institution of Mechanical Engineers, Part M: Journal of Engineering for the Maritime Environment</option>
<option value="pina">Proceedings of the Institution of Mechanical Engineers, Part N: Journal of Nanoengineering and Nanosystems</option>
<option value="pinb">Proceedings of the Institution of Mechanical Engineers, Part N: Journal of Nanomaterials, Nanoengineering and Nanosystems</option>
<option value="pioa">Proceedings of the Institution of Mechanical Engineers, Part O: Journal of Risk and Reliability</option>
 <option value="pipa">Proceedings of the Institution of Mechanical Engineers, Part P: Journal of Sports Engineering and Technology</option>
<option value="pada">Proceedings of the Institution of Mechanical Engineers: Automobile Division</option>
<option value="hcsa">Proceedings of the International Symposium on Human Factors and Ergonomics in Health Care</option>
<option value="jrsa">Proceedings of the Royal Society of Medicine</option>
<option value="ebma">Proceedings of the Society for Experimental Biology and Medicine</option>
<option value="otoi">Proceedings of the Western Ophthalmologic and Oto-Laryngologic Association</option>
<option value="prea">Pro Ecclesia</option>
<option value="pcxa">Professional School Counseling</option>
<option value="pdja">Progress in Development Studies</option>
<option value="phga">Progress in Geography</option>
<option value="phgb">Progress in Human Geography</option>
<option value="ppga">Progress in Physical Geography: Earth and Environment</option>
<option value="rasa">Progress in Public Administration</option>
<option value="prkb">Progress in Reaction Kinetics</option>
<option value="prka">Progress in Reaction Kinetics and Mechanism</option>
<option value="prpa">Progress in Rubber, Plastics and Recycling Technology</option>
<option value="prpd">Progress in Rubber and Plastics Technology</option>
<option value="pitb">Progress in Transplantation</option>
<option value="prpc">Progress of Rubber Technology</option>
<option value="prpb">Progress of Rubber Technology. Annual Report</option>
<option value="pmxa">Project Management Journal</option>
<option value="peda">Promotion &amp; Education</option>
<option value="poia">Prosthetics and Orthotics International</option>
<option value="prta">Proteomics Insights</option>
<option value="joaa">Prufrock Journal</option>
<option value="jpsb">Psoriasis Forum</option>
<option value="ijpa">Psychiatry in Medicine</option>
<option value="prxa">Psychological Reports</option>
<option value="pssa">Psychological Science</option>
<option value="psia">Psychological Science in the Public Interest</option>
<option value="pdsa">Psychology and Developing Societies</option>
<option value="plja">Psychology Learning &amp; Teaching</option>
<option value="poma">Psychology of Music</option>
<option value="pwqa">Psychology of Women Quarterly</option>
<option value="eppb">Psychopathology Review</option>
<option value="pfra">Public Finance Quarterly</option>
<option value="pfrb">Public Finance Review</option>
<option value="mcra">Public Health Economics</option>
<option value="mcrb">Public Health Economics and Medical Care Abstracts</option>
<option value="phrg">Public Health Reports</option>
<option value="phrf">Public Health Reports</option>
<option value="ppmd">Public Personnel Management</option>
<option value="ppmb">Public Personnel Review</option>
<option value="ppaa">Public Policy and Administration</option>
<option value="pria">Public Relations Inquiry</option>
<option value="pusa">Public Understanding of Science</option>
<option value="pwma">Public Works Management &amp; Policy</option>
<option value="pula">Pulmonary Circulation</option>
<option value="puna">Punishment &amp; Society</option>
<option value="qhra">Qualitative Health Research</option>
<option value="qixa">Qualitative Inquiry</option>
<option value="qrja">Qualitative Research</option>
<option value="qswa">Qualitative Social Work</option>
<option value="ajma">Quality Assurance and Utilization Review</option>
<option value="qjpd">Quarterly Journal of Experimental Psychology</option>
<option value="qjpa">Quarterly Journal of Experimental Psychology</option>
<option value="raca">Race</option>
<option value="racb">Race &amp; Class</option>
<option value="raja">Race and Justice</option>
<option value="rtua">Rare Tumors</option>
<option value="rssa">Rationality and Society</option>
<option value="rmea">Recherche et Applications en Marketing (English Edition)</option>
<option value="rama">Recherche et Applications en Marketing (French Edition)</option>
<option value="rsja">Recreational Sports Journal</option>
<option value="rcba">Rehabilitation Counseling Bulletin</option>
<option value="rpoa">Rehabilitation Process and Outcome</option>
<option value="rela">RELC Journal</option>
<option value="rsed">Remedial and Special Education</option>
<option value="crub">Reports of the International Commission on Radiation Units and Measurements</option>
<option value="rsxb">Reproductive Sciences</option>
<option value="rapa">Research &amp; Politics</option>
<option value="rpsd">Research and Practice for Persons with Severe Disabilities</option>
<option value="reab">Research Ethics</option>
<option value="rcia">Research in Comparative and International Education</option>
<option value="riea">Research in Education</option>
<option value="rmma">Research Methods in Medicine &amp; Health Sciences</option>
<option value="roaa">Research on Aging</option>
<option value="rswa">Research on Social Work Practice</option>
<option value="rsma">Research Studies in Music Education</option>
<option value="rrna">Reuse/Recycle Newsletter</option>
<option value="raeb">Review &amp; Expositor</option>
 <option value="tpsb">Review and Newsletter, Transcultural Research in Mental Health Problems</option>
<option value="rbpa">The Review of Black Political Economy</option>
<option value="rdca">Review of Development and Change</option>
<option value="rera">Review of Educational Research</option>
<option value="rgpa">Review of General Psychology</option>
<option value="rmia">Review of Market Integration</option>
<option value="ropa">Review of Public Personnel Administration</option>
<option value="rrpa">Review of Radical Political Economics</option>
<option value="rrea">Review of Research in Education</option>
<option value="bjpa">Reviews in Pain</option>
<option value="reva">Reviews of Human Factors and Ergonomics</option>
<option value="fstb">Revista Espanola de Ciencia y Tecnologia de Alimentos</option>
<option value="rima">Revista Internacional de Educaci�n Musical</option>
<option value="rpra">Rheumatology Practice and Research</option>
<option value="neua">Rivista di Neuroradiologia</option>
<option value="rshc">Royal Society of Health Journal</option>
<option value="rsqa">Rural Special Education Quarterly</option>
<option value="sgoa">SAGE Open</option>
<option value="scoa">SAGE Open Medical Case Reports</option>
<option value="smoa">SAGE Open Medicine</option>
<option value="sona">SAGE Open Nursing</option>
<option value="sjpc">Scandinavian Journal of Public Health</option>
<option value="sjpa">Scandinavian Journal of Social Medicine</option>
<option value="sjsb">Scandinavian Journal of Surgery</option>
<option value="sbha">Scars, Burns &amp; Healing</option>
<option value="trea">School Field</option>
<option value="jsna">School Nurse</option>
<option value="spia">School Psychology International</option>
<option value="sthd">Science, Technology, &amp; Human Values</option>
<option value="stsa">Science, Technology and Society</option>
<option value="scxb">Science Communication</option>
<option value="scia">Science Progress</option>
<option value="sssa">Science Studies</option>
<option value="scma">Scottish Medical Journal</option>
<option value="srxa">Sculpture Review</option>
<option value="slrb">Second Language Research</option>
<option value="sdib">Security Dialogue</option>
<option value="sdea">SEDME (Small Enterprises Development, Management &amp; Extension Journal)</option>
<option value="scva">Seminars in Cardiothoracic and Vascular Anesthesia</option>
<option value="sria">Seminars in Laparoscopic Surgery</option>
<option value="saxb">Sexual Abuse</option>
<option value="sexa">Sexualities</option>
<option value="smea">Sexualization, Media, &amp; Society</option>
<option value="sela">Shoulder &amp; Elbow</option>
<option value="stia">Signal Transduction Insights</option>
<option value="simb">SIMULATION</option>
<option value="saga">Simulation &amp; Games</option>
<option value="sagb">Simulation &amp; Gaming</option>
<option value="jbxb">SLAS DISCOVERY: Advancing the Science of Drug Discovery</option>
<option value="jlad">SLAS TECHNOLOGY: Translating Life Sciences Innovation</option>
<option value="sgrb">Small Group Behavior</option>
<option value="sgrd">Small Group Research</option>
<option value="slsa">Social &amp; Legal Studies</option>
<option value="fisd">Social Casework</option>
<option value="scha">Social Change</option>
<option value="scpa">Social Compass</option>
<option value="scua">Social Currents</option>
<option value="smqa">Social Marketing Quarterly</option>
<option value="smsa">Social Media + Society</option>
<option value="sppa">Social Psychological and Personality Science</option>
<option value="spqb">Social Psychology</option>
<option value="spqc">Social Psychology Quarterly</option>
<option value="ssce">Social Science Computer Review</option>
<option value="ssic">Social Science Information</option>
<option value="sscd">Social Science Microcomputer Review</option>
<option value="sscb">Social Science Micro Review</option>
<option value="ssib">Social Sciences Information</option>
<option value="sssb">Social Studies of Science</option>
<option value="iswa">Social Welfare in South-East Asia</option>
<option value="scsa">Society and Culture in South Asia</option>
<option value="smha">Society and Mental Health</option>
<option value="soba">Sociological Bulletin</option>
<option value="smxa">Sociological Methodology</option>
<option value="smra">Sociological Methods &amp; Research</option>
<option value="spxb">Sociological Perspectives</option>
<option value="jaxb">Sociological Practice</option>
<option value="sroa">Sociological Research Online</option>
<option value="stxa">Sociological Theory</option>
<option value="soca">Sociology</option>
<option value="soea">Sociology of Education</option>
<option value="srea">Sociology of Race and Ethnicity</option>
<option value="woxa">Sociology of Work and Occupations</option>
<option value="spqa">Sociometry</option>
<option value="srda">Socius</option>
<option value="gmta">Soundings (Reston, VA)</option>
<option value="sapc">South African Journal of Psychology</option>
<option value="saea">South Asia Economic Journal</option>
<option value="bmca">South Asian Journal of Business and Management Cases</option>
<option value="hrma">South Asian Journal of Human Resources Management</option>
<option value="smpa">South Asian Journal of Macroeconomics and Public Finance</option>
<option value="sasa">South Asian Survey</option>
<option value="sara">South Asia Research</option>
<option value="sera">South East Asia Research</option>
<option value="iprc">Soviet Plastics</option>
<option value="iprb">Soviet Rubber Technology</option>
<option value="saca">Space and Culture</option>
<option value="spha">Sports Health</option>
<option value="slgb">State and Local Government Review</option>
<option value="spaa">State Politics &amp; Policy Quarterly</option>
<option value="smma">Statistical Methods in Medical Research</option>
<option value="smja">Statistical Modelling</option>
<option value="soqa">Strategic Organization</option>
<option value="srja">String Research Journal</option>
<option value="shma">Structural Health Monitoring</option>
<option value="stla">Studia Liturgica</option>
<option value="scea">Studies in Christian Ethics</option>
<option value="siha">Studies in History</option>
<option value="inpa">Studies in Indian Politics</option>
<option value="mica">Studies in Microeconomics</option>
<option value="sipa">Studies in People's History</option>
<option value="sira">Studies in Religion/Sciences Religieuses</option>
<option value="sata">Substance Abuse: Research and Treatment</option>
<option value="srib">Surgical Innovation</option>
<option value="jega">Talents and Gifts</option>
<option value="tesa">Teacher Education and Special Education</option>
<option value="tcxa">TEACHING Exceptional Children</option>
<option value="topa">Teaching of Psychology</option>
<option value="tpaa">Teaching Public Administration</option>
<option value="tsoa">Teaching Sociology</option>
<option value="tcta">Technology in Cancer Research &amp; Treatment</option>
<option value="tvna">Television &amp; New Media</option>
<option value="trjb">Textile Research</option>
<option value="trjc">Textile Research Journal</option>
<option value="jobb">The ABCA Journal of Business Communication</option>
<option value="wafh">The Advocate of Peace</option>
<option value="wafe">The Advocate of Peace and Universal Brotherhood</option>
<option value="wafg">The American Advocate of Peace and Arbitration</option>
<option value="aexb">The American Economist</option>
<option value="acsa">The American Journal of Cosmetic Surgery</option>
<option value="ajsb">The American Journal of Sports Medicine</option>
<option value="arpb">The American Review of Public Administration</option>
<option value="asua">The American Surgeon</option>
<option value="anna">The ANNALS of the American Academy of Political and Social Science</option>
<option value="abxa">The Antitrust Bulletin</option>
<option value="josa">The Australian and New Zealand Journal of Sociology</option>
<option value="tbtd">The Bible Translator</option>
<option value="htha">The British Journal of Hand Therapy</option>
<option value="jhra">The Bulletin of Historical Research in Music Education</option>
<option value="bcqc">The Bulletin of the Association for Business Communication</option>
<option value="bulc">The bulletin of the National Association of Secondary School Principals</option>
<option value="tpxa">The Bulletin of the Society of Pharmacological and Environmental Pathologists</option>
<option value="wafb">The Calumet</option>
<option value="cpab">The Canadian Journal of Psychiatry</option>
<option value="cpca">The Cleft Palate-Craniofacial Journal</option>
<option value="tcpa">The Counseling Psychologist</option>
<option value="tdea">The Diabetes Educator</option>
<option value="tdra">The Downside Review</option>
<option value="elra">The Economic and Labour Relations Review</option>
<option value="exta">The Expository Times</option>
<option value="fisb">The Family</option>
<option value="tfja">The Family Journal</option>
<option value="hola">The Holocene</option>
<option value="iera">The Indian Economic &amp; Social History Review</option>
<option value="ieja">The Indian Economic Journal</option>
<option value="ahdb">The International Journal of Aging and Human Development</option>
<option value="jaoa">The International Journal of Artificial Organs</option>
<option value="jbmb">The International Journal of Biological Markers</option>
<option value="coda">The International Journal of Community and Social Development</option>
<option value="ijea">The International Journal of Electrical Engineering &amp; Education</option>
<option value="epja">The International Journal of Evidence &amp; Proof</option>
<option value="hpcc">The International Journal of High Performance Computing Applications</option>
<option value="ocsa">The International Journal of Ocean and Climate Systems</option>
<option value="hijb">The International Journal of Press/Politics</option>
<option value="ijpb">The International Journal of Psychiatry in Medicine</option>
<option value="ijra">The International Journal of Robotics Research</option>
<option value="hpcb">The International Journal of Supercomputer Applications and High Performance Computing</option>
<option value="hpca">The International Journal of Supercomputing Applications</option>
<option value="mrxb">The International Migration Digest</option>
<option value="jmca">The Journalism Educator</option>
<option value="jaba">The Journal of Applied Behavioral Science</option>
<option value="jobc">The Journal of Business Communication (1973)</option>
<option value="jcla">The Journal of Commonwealth Literature</option>
<option value="cmfa">The Journal of Computational Multiphase Flows</option>
<option value="clja">The Journal of Criminal Law</option>
<option value="jeaa">The Journal of Early Adolescence</option>
<option value="egaa">The Journal of Egyptian Archaeology</option>
<option value="joea">The Journal of Entrepreneurship</option>
<option value="jeda">The Journal of Environment &amp; Development</option>
<option value="lmec">The Journal of Law, Medicine &amp; Ethics</option>
<option value="mena">The Journal of Men’s Studies</option>
<option value="plxa">The Journal of Psychiatry &amp; Law</option>
<option value="fisc">The Journal of Social Casework</option>
<option value="seda">The Journal of Special Education</option>
<option value="ajsa">The Journal of Sports Medicine</option>
<option value="sdjb">The Journal of Strain Analysis for Engineering Design</option>
<option value="jthc">The Journal of Transport History</option>
<option value="jvaa">The Journal of Vascular Access</option>
<option value="lqra">The Linacre Quarterly</option>
<option value="mhja">The Medieval History Journal</option>
<option value="nhoa">The Neurohospitalist</option>
<option value="neub">The Neuroradiology Journal</option>
<option value="nroa">The Neuroscientist</option>
<option value="otja">The Occupational Therapy Journal of Research</option>
<option value="tsja">Theological Studies</option>
<option value="tjxa">Theology</option>
<option value="tsea">Theology &amp; Sexuality</option>
<option value="ttja">Theology Today</option>
<option value="tcra">Theoretical Criminology</option>
<option value="oana">The Oriental Anthropologist</option>
<option value="tcsa">Theory, Culture &amp; Society</option>
<option value="tapa">Theory &amp; Psychology</option>
<option value="treb">Theory and Research in Education</option>
<option value="pjxa">The Police Journal</option>
<option value="tpjd">The Prison Journal</option>
<option value="qjpb">The Quarterly Journal of Experimental Psychology Section A</option>
<option value="qjpc">The Quarterly Journal of Experimental Psychology Section B</option>
<option value="taka">Therapeutic Advances in Cardiovascular Disease</option>
<option value="taja">Therapeutic Advances in Chronic Disease</option>
<option value="tawa">Therapeutic Advances in Drug Safety</option>
<option value="taea">Therapeutic Advances in Endocrinology and Metabolism</option>
<option value="taga">Therapeutic Advances in Gastroenterology</option>
<option value="cmgc">Therapeutic Advances in Gastrointestinal Endoscopy</option>
<option value="taha">Therapeutic Advances in Hematology</option>
<option value="taia">Therapeutic Advances in Infectious Disease</option>
<option value="tama">Therapeutic Advances in Medical Oncology</option>
<option value="taba">Therapeutic Advances in Musculoskeletal Disease</option>
<option value="tana">Therapeutic Advances in Neurological Disorders</option>
<option value="oedb">Therapeutic Advances in Ophthalmology</option>
<option value="tppa">Therapeutic Advances in Psychopharmacology</option>
<option value="trda">Therapeutic Advances in Rare Disease</option>
<option value="rehc">Therapeutic Advances in Reproductive Health</option>
<option value="tara">Therapeutic Advances in Respiratory Disease</option>
<option value="taua">Therapeutic Advances in Urology</option>
<option value="tava">Therapeutic Advances in Vaccines</option>
<option value="tavb">Therapeutic Advances in Vaccines and Immunotherapy</option>
<option value="dijc">Therapeutic Innovation &amp; Regulatory Science</option>
<option value="thea">Thesis Eleven</option>
<option value="sora">The Sociological Review</option>
<option value="soma">The Sociological Review Monographs</option>
<option value="stja">The Stata Journal</option>
<option value="jmea">The Teaching of Organizational Behavior</option>
<option value="tmxa">The Traumaxilla</option>
<option value="lrxc">The Yearbook of the National Reading Conference</option>
<option value="tasa">Time &amp; Society</option>
<option value="tuia">Tobacco Use Insights</option>
<option value="teca">Topics in Early Childhood Special Education</option>
<option value="jgpa">Topics in geriatrics</option>
<option value="rsec">Topics in Learning &amp; Learning Disabilities</option>
<option value="thrb">Tourism and Hospitality Research</option>
<option value="teua">Tourism Economics</option>
<option value="toua">Tourist Studies</option>
<option value="tpxb">Toxicologic Pathology</option>
<option value="tiha">Toxicology and Industrial Health</option>
<option value="tora">Toxicology Research and Application</option>
<option value="taxa">Transactional Analysis Bulletin</option>
<option value="taxb">Transactional Analysis Journal</option>
<option value="otod">Transactions: Section on Otolaryngology</option>
<option value="otoc">Transactions - American Academy of Ophthalmology and Otolaryngology</option>
<option value="lrta">Transactions of the Illuminating Engineering Society</option>
<option value="tima">Transactions of the Institute of Measurement and Control</option>
<option value="mlja">Transactions of the Medico-Legal Society for the yearÖ</option>
<option value="otoa">Transactions of the Ophthalmological Division of the American Academy of Ophthalmology and Otolaryngology</option>
<option value="otoh">Transactions of the Ophthalmological of the Western Ophthalmological and Oto-Laryngologic Association</option>
<option value="rshg">Transactions of the Sanitary Institute</option>
<option value="rshf">Transactions of the Sanitary Institute of Great Britain</option>
<option value="sima">Transactions of the Society for Computer Simulation</option>
<option value="otob">Transactions of the … annual meeting of the American Academy of Ophthalmology and Otolaryngology</option>
<option value="tpsd">Transcultural Psychiatric Research Review</option>
<option value="tpsc">Transcultural Psychiatric Research Review and Newsletter</option>
<option value="tpse">Transcultural Psychiatry</option>
<option value="trsa">Transfer: European Review of Labour and Research</option>
<option value="trna">Transformation</option>
<option value="bsab">Translational Neuroscience and Clinics</option>
<option value="tooa">Translational Research in Oral Oncology</option>
<option value="trra">Transportation Research Record</option>
<option value="traa">Trauma</option>
<option value="tvaa">Trauma, Violence, &amp; Abuse</option>
<option value="tmta">Traumatology</option>
<option value="jtra">Travel Research Bulletin</option>
<option value="tiaa">Trends in Amplification</option>
<option value="tiab">Trends in Hearing</option>
<option value="trca">Tropical Conservation Science</option>
<option value="tdoa">Tropical Doctor</option>
<option value="tuba">Tumor Biology</option>
<option value="tmja">Tumori Journal</option>
<option value="uixa">Ultrasonic Imaging</option>
<option value="ultb">Ultrasound</option>
<option value="intb">Union Seminary Magazine</option>
<option value="inta">Union Seminary Review</option>
<option value="uega">United European Gastroenterology Journal</option>
<option value="upda">Update: Applications of Research in Music Education</option>
<option value="uara">Urban Affairs Quarterly</option>
<option value="uarb">Urban Affairs Review</option>
<option value="uexa">Urban Education</option>
<option value="urba">Urbanisation</option>
<option value="jceb">Urban Life</option>
<option value="jcea">Urban Life and Culture</option>
<option value="usja">Urban Studies</option>
<option value="urja">Urologia Journal</option>
<option value="njnb">Vård i Norden</option>
<option value="vasb">Vascular</option>
<option value="vesb">Vascular and Endovascular Surgery</option>
<option value="vmjc">Vascular Medicine</option>
<option value="vmjb">Vascular Medicine Review</option>
<option value="vesa">Vascular Surgery</option>
<option value="jova">Veterinary Dentistry</option>
<option value="vetb">Veterinary Pathology</option>
<option value="vika">Vikalpa</option>
<option value="vioa">Violence: An International Journal</option>
<option value="vawa">Violence Against Women</option>
<option value="vrta">Virology: Research and Treatment</option>
<option value="visa">Vision</option>
<option value="vcja">Visual Communication</option>
<option value="wiha">War in History</option>
<option value="wmra">Waste Management &amp; Research</option>
<option value="phrd">Weekly Abstract of Sanitary Reports</option>
<option value="wjna">Western Journal of Nursing Research</option>
<option value="prqa">Western Political Quarterly</option>
<option value="wiea">Wind Engineering</option>
<option value="whea">Women's Health</option>
<option value="woma">Word of Mouth</option>
<option value="wesa">Work, Employment and Society</option>
<option value="woxb">Work and Occupations</option>
<option value="whsd">Workplace Health &amp; Safety</option>
<option value="wafj">World Affairs</option>
<option value="wfra">World Futures Review</option>
<option value="pcha">World Journal for Pediatric and Congenital Heart Surgery</option>
<option value="wcxa">Written Communication</option>
<option value="bula">Yearbook of the National Association of Secondary-School Principals</option>
<option value="lrxb">Yearbook of the Southwest Reading Conference for Colleges and Universities</option>
<option value="youa">YOUNG</option>
<option value="yeca">Young Exceptional Children</option>
<option value="yasa">Youth &amp; Society</option>
<option value="yjja">Youth Justice</option>
<option value="yvja">Youth Violence and Juvenile Justice</option>
<option value="lina">Yu yan ji yu yan xue</option>
</select>
<div class="citation-details float-right">
<input type="hidden" name="quickLink" value="true" /><input class="search-term smallTextInput" type="text" name="quickLinkYear" value="" size="15" autocomplete="false" placeholder="Year" /><input class="search-term smallTextInput" type="text" name="quickLinkVolume" value="" size="15" autocomplete="false" placeholder="Volume" /><input class="search-term smallTextInput" type="text" name="quickLinkIssue" value="" size="15" autocomplete="false" placeholder="Issue" /><input class="search-term fist-page-input smallTextInput" type="text" name="quickLinkPage" value="" size="15" autocomplete="false" placeholder="Page" />
</div>
<div class=" submitRow float-right clear">
<input id="citationSearchSubmitButton" class="searchButtons pointer" title="Search" type="submit" value="Search" disabled="disabled" />
</div>
</fieldset></form>
</div></div>
</div>
</div>
</div>
</div>
<div class="col-md-1-3 ">
<div class="contents" data-pb-dropzone="contents1">
<div class="widget general-rich-text none advanced-search-sidebar widget-none" id="0a98afb0-4959-447b-97c5-fc2a86260301">
<div class="wrapped ">
<div class="widget-body body body-none "><div id="rich-text-0a98afb0-4959-447b-97c5-fc2a86260301" class="pb-rich-text">
<h2>Search Terms and Keywords</h2>
<p>Select multiple fields to refine your search. Press the 'enter' key at any time to run a search. Improve your search using AND, OR, NOT and search phrases using "..."&nbsp;</p>
<p></p>
<p><a href="/page/help/search/boolean" title="Search help: boolean search" target="_blank">More information about search on SAGE Journals</a></p>
</div></div>
</div>
</div>
</div>
</div>
</div>
</div></div>
</div>
</div>
</div>
</div></div>
</div>
</div>
<div class="widget layout-one-column none page-footer-divider widget-none  widget-compact-all" id="02555f61-8272-46aa-928d-70d0a3542f35">
<div class="wrapped " id='SAGEPageFooterDivider'>
<div class="widget-body body body-none  body-compact-all"><div class="pb-columns row-fluid">
<div class="width_1_1">
<div data-pb-dropzone="center">
</div>
</div>
</div></div>
</div>
</div>
<div class="widget general-html-asset none  widget-none  widget-compact-all" id="ad33bbde-fc41-4c1b-8fef-01a1aacd0924">
<div class="wrapped ">
<div class="widget-body body body-none  body-compact-all"><script>
if (""!=="")
    $('div.Article.information div:first-of-type').prepend("<i>,</i>");
</script>
<script>
// Here we keep the JS functions that use context sensitive parameters, since these are not working outside of HTML assets (e.g. in js files)
function removeTlaFromTaxonomyFacet() { //SAGE-2005
    $("li.ConceptID.parentFacets").each(function(){
        let $link = $(this).find(".facet-link-container a");
        if ($link.length) {
            if ($link[0].innerHTML.toLowerCase().trim() === "".toLowerCase()) {
                $(this).css("display", "none"); // hide this 
                //console.debug("Removed TLA code from taxonomy filter");
                if ($(this).parents(".hiddenChildrenFacets").length) { // If TLA code found in hidden facets, change the More(n) text to More(n-1)
                    $(this).parents("div.facetContainer").find("div.toggleMoreFacets a.facet-link").each(function(){
                        if (this.innerHTML.toLowerCase().indexOf("more (") !== -1) {
                            let moreNumber = this.innerHTML.match(/\d+/)[0];
                            if (moreNumber > 1)
                                $(this).text($(this).text().replace(moreNumber, moreNumber - 1));
                            else // if only one was hidden, no need to expand
                                $(this).parent().css("display", "none");
                        }
                    });
                }
            }
        }
    });
}
function cpTitlesDates() {
    if (''==='cp' || ''==='cpv') {
        $('.pubDate-left').addClass('not-show-important');
    }
}
function deniedPdfAccess() {
    //console.debug('Denial PDF button clicked');
    if ($('#accessOptionsTop').length > 0) { // clicked on page with access denial bar
        toggleDenialBar(true);
        $('#accessOptionsTop input[name="login"]').focus();
    } else { // no access denial bar
        window.location = '/doi/pdf/';
    }
}
function accesibilityImageAltText() {
    $('.moreFromThisJournalModules img').each(function(){
        if ($(this).attr('alt')===undefined) $(this).attr('alt', '');
    });
    $('.portalResourcesContainer img, .tellUsImage img, img.relatedJournalsImageContainer').attr('alt', '');
    $('.relatedJournalsTextContainer').each(function(){
        let $journalText = $(this);
        $journalText.closest('.relatedJournalsColumn>a').append($journalText.text());
        $journalText.remove();
    });
    $('.relatedJournalsImageContainer img').each(function(){
        let $coverImage = $(this);
        let $parent = $(this).parent();
        $coverImage.addClass('relatedJournalsImageContainer');
        $coverImage.prependTo($coverImage.closest('.relatedJournalsColumn>a'));
        $parent.remove();
    });
    $('td.savedSearch.savedResult:nth-child(4) img').attr('alt', function() {
        return $(this).attr('alt').replace('alert type', 'saved date');
    })

    $('td.savedSearch.savedResult:nth-child(5) img').attr('alt', function() {
        return $(this).attr('alt').replace('alert type', 'last run date');
    })
}
function checkJournalHomeLinks(){ //SAGE-4019
    if (inJournalHome()){
        if ($('.journalBoardViewAllButton a').length && $('.journalBoardViewAllButton a').attr('href').indexOf('/connected/')!=-1){
            $('.journalBoardViewAllButton a').attr('href', '/editorial-board/');
        }
        if ($('.journalPublishViewAllButton a').length && $('.journalPublishViewAllButton a').attr('href').indexOf('{}')!=-1){
            let link=$('.menuXml.journalMenus a[data-item-name="view-submit-paper"]').attr('href');
            if (link==="#")
                link=$('.menuXml.journalMenus a[data-item-name="Submit Now"]').attr('href');
            if (link===undefined)
                link=$('.menuXml.journalMenus a[data-item-name="Submit Now "]').attr('href');
            if (link!==undefined)
                $('.journalPublishViewAllButton a').attr('href', link);
        }
        $('.journalCarouselTextButton a').each(function (){
            if ($(this).attr('href').indexOf('/connected/')!=-1 && $(this).text().indexOf('More')!==-1){
                $(this).attr('href', '/description/');
            }
        });
    }
}
if ($('.creative-commons-badge.cc-by').length){
	console.debug('Hiding permissions button due to CC-BY type of article.');
	$('a.permissionsTool').closest('div').css('display', 'none');
}
else 
    $('a.permissionsTool').closest('div').css('display', 'flex');

// display denial access bar if user not authenticated or in PB edit mode
try {
    if (!hasArticleAccessHeuristic() || $('.pb-wrap.pb-widget').length > 0) 
        $('.pb-ui .accessOptionsBar').css('display', 'block');
    else
        $('.pb-ui .accessOptionsBar').hide();
}
catch(e){
    $('.pb-ui .accessOptionsBar').hide();
}

if ($('span.related-Article-wrapper span').length===0) 
    $('span.related-Article-wrapper').hide();

cpTitlesDates();

// Add data module attributes in related journals HTML widget
$(".otherSociety").attr("data-module-name", "related-journals");
$(".otherSocietyButton #viewMoreText").attr("data-item-name", "view-more");
$(".otherSocietyButton #viewLessText").attr("data-item-name", "view-fewer");
$(".otherSocietyButton #viewFewerText").attr("data-item-name", "view-fewer");

$('#share-tabs ul li a[title="show Social Media"]').attr("data-item-name", "view-social-media");
$('#share-tabs ul li a[title="show Email"]').attr("data-item-name", "view-email");
$('#share-tabs ul li a[title="show Share Access"]').attr("data-item-name", "view-share-access");

//Move related asrticles indication into proper place:
$('span.related-Article-wrapper').insertAfter('div.articleInformation');

$('.related-article-title').text(function() {
    return $(this).text().replace(/\s*:/, ': ');
});
$('.online-pub-date').text(function() {
    return $(this).text().replace(/-/g, ' ');
});
$('.contentItemVol').text(function() {
    return $(this).text().replace('Vol 0,', '').replace('Vol.', 'Vol ').replace(/\s*,/, ',');
});
$('.issueFormat').text(function() {
    return $(this).text().replace('issue', 'Issue').replace('vol.', 'Vol').replace(/\s*,/, ',');
});
//Remove trailing dot from a.deleteAccountLink
$('a.deleteAccountLink').text('Delete your account');

//Remove trailing dot from a.deleteAccountLink
$('a#copyToClipBoard').text('Copy to Clipboard');

// Rename "Views" to "Views and downloads"
$('.view-count').text(function() {
    if (inJournalScope())
        return $(this).text().replace('Views:', 'Views & downloads:');
    else
        return $(this).text();
});

// Keep only anchor element if already in citedBy page
if ($('.view-all-citedBy a').attr('href') === window.location.pathname)
    $('.view-all-citedBy a').attr('href', '');
// Add #top-content-scroll on 'View All' citedBy link
$('.view-all-citedBy a').attr('href', $('.view-all-citedBy a').attr('href') + '#top-content-scroll');

// Change MR/MC panel text
$('#mostReadCitedPage .online-pub-date').text(function() {
    return $(this).text().replace("Online publication date", "First published");
});

//Wait for images to load, before deciding whteher to move the related journals 
$('.journalHomeFourRight').imagesLoaded().always(function(){
    moveRelatedJournals();
    //console.debug('Ad(right) image is loaded');
});

if (!inJournalScope() && $('#mainSearchBar select.filterOption option[disabled]').length>0){
    $('#mainSearchBar select.filterOption').attr('disabled','');
}

// Fix for 'more...' label falling into 2nd line
if ($('.authors .more-than').length && $('.authors .more-than').offset().left <= $('.authors .hlFld-ContribAuthor').offset().left) $('.authors .more-than').addClass('not-show-important');

$('.related-articles').each(function(){
    if($(this).find('.multi-related-article').length)
        $(this).addClass('multi-related-articles');

})
// Use proper roles for tabbed OF/MR/MC section on journal home page
$('ul.tab-nav').attr('role', 'tablist');
$('ul.tab-nav>li').attr('role', 'tab');

// Show lean library banner only if user has full access
if ($('.articleBadges .accessIcon.openAccess, .articleBadges .accessIcon.freeAccess').length>0) $('.lean-library-ft p.ll-message-oa').removeClass('doNotShow');
else if ($('.articleBadges .accessIcon.fullAccess').length>0) $('.lean-library-ft p.ll-message').removeClass('doNotShow');
if ($('.PDFTool.pdf-no-access').length===0) $('div.lean-library-ft').removeClass('doNotShow'); 
/*
try{
    var observer = new MutationObserver(function(mutations) {
        mutations.forEach(function(mutationRecord) {
            if (mutationRecord.type == 'childList') {
                //console.log('A child node has been added or removed.');
                let refPopup=document.getElementById('openBalloon');
                if (refPopup!==null){
                    if (refPopup.style.right==='0px') {
                        addClass('openBalloon', 'flip-balloon');
                        //let ref=$(refPopup).closest('span.ref').prev('a.ref')[0];
                        //if ($(ref).width()>250 || ref.getBoundingClientRect().left<0.6*window.innerWidth)
                        //    addClass('openBalloon', 'pull-left');
                    }
                }
            }
        });
    });

    var target = document.getElementById('25e8d4fe-c5d2-4686-bdef-3b125e01db4b');
    if (target)
        observer.observe(target, {attributes:false, childList:true, subtree:true });
} catch(e) {
}
*/

initLoginBox();
//specialCollectionDuplicate();
removeTlaFromTaxonomyFacet();
moveRelatedJournals();
rearrangeMostReadCitedPage();
accesibilityImageAltText();
removeDuplicateIds();
checkJournalHomeLinks();

if (pbPreviewOn===1 && !inMicrositeScope()){
    //console.debug('Running document ready JS...');
    docReady();
}
/////////////////////////////////////////////
$(window).bind('orientationchange', function(event){
    try {
		$('input[name=AllField]').autocomplete('close'); 
	} catch(e) {}
});

$(window).scroll(function(){
    let scroll = $(window).scrollTop();
    try {
        if(scroll>1)
            $('input[name=AllField]').autocomplete('close');
    }
    catch(e) {}
 });
 //console.debug('Journal: , Issue: , Article: ');
</script></div>
</div>
</div>
<div class="widget pageFooter none  widget-none  widget-compact-all" id="6fb92b62-7dea-47a0-9cc8-47eb89502f6b">
<div class="wrapped ">
<div class="widget-body body body-none  body-compact-all"><footer class="page-footer">
<div data-pb-dropzone="main">
<div class="widget general-html-asset none  widget-none  widget-compact-all" id="73236743-087c-416d-97bd-8aeae29f25fc">
<div class="wrapped ">
<div class="widget-body body body-none  body-compact-all"><div class="moreSAGEProductsOuterContainer">
<main role="main">
<div class="moreSAGEProducts" role="region" aria-labelledby="cp-footer-label">
<h2 id="cp-footer-label">Also from SAGE Publishing</h2>
<ul data-id="cross-product-footer" data-module-name="cross-product-footer">
<li data-id="cross-product-footer-card-cqlibrary" data-item-name="cross-product-footer-card-cqlibrary">
<a href="https://library.cqpress.com/index.php?utm_source=cross-product-footer&amp;utm_medium=cross-product" target="_blank" rel="noopener" class="cqlibrary">
<span class="product-name">CQ Library</span> American political resources <span class="offscreen">opens in new tab</span>
</a>
</li>
<li data-id="cross-product-footer-card-dataplanet" data-item-name="cross-product-footer-card-dataplanet">
<a href="https://www.data-planet.com?utm_source=cross-product-footer&amp;utm_medium=cross-product" target="_blank" rel="noopener" class="dataplanet">
<span class="product-name">Data Planet</span> A universe of data <span class="offscreen">opens in new tab</span>
</a>
</li>
<li data-id="cross-product-footer-card-leanlibrary" data-item-name="cross-product-footer-card-leanlibrary">
<a href="https://www.leanlibrary.com?utm_source=cross-product-footer&amp;utm_medium=cross-product" target="_blank" rel="noopener" class="leanlibrary">
<span class="product-name">Lean Library</span> Increase the visibility of your library <span class="offscreen">opens in new tab</span>
</a>
</li>
<li data-id="cross-product-footer-card-sagebusinesscases" data-item-name="cross-product-footer-card-sagebusinesscases">
<a href="https://sk.sagepub.com/cases?utm_source=cross-product-footer&amp;utm_medium=cross-product" target="_blank" rel="noopener" class="sagebusinesscases">
<span class="product-name">SAGE Business Cases</span> Real-world cases at your fingertips <span class="offscreen">opens in new tab</span>
</a>
</li>
<li data-id="cross-product-footer-card-sageknowlwdge" data-item-name="cross-product-footer-card-sageknowlwdge">
<a href="https://sk.sagepub.com?utm_source=cross-product-footer&amp;utm_medium=cross-product" target="_blank" rel="noopener" class="sageknowlwdge">
<span class="product-name">SAGE Knowledge</span> The ultimate social science library <span class="offscreen">opens in new tab</span>
</a>
</li>
<li data-id="cross-product-footer-card-sageresearchmethods" data-item-name="cross-product-footer-card-sageresearchmethods">
<a href="https://methods.sagepub.com?utm_source=cross-product-footer&amp;utm_medium=cross-product" target="_blank" rel="noopener" class="sageresearchmethods">
<span class="product-name">SAGE Research Methods</span> The ultimate methods library <span class="offscreen">opens in new tab</span>
</a>
</li>
<li data-id="cross-product-footer-card-sagestats" data-item-name="cross-product-footer-card-sagestats">
<a href="https://data.sagepub.com/sagestats?utm_source=cross-product-footer&amp;utm_medium=cross-product" target="_blank" rel="noopener" class="sagestats">
<span class="product-name">SAGE Stats</span> Data on demand <span class="offscreen">opens in new tab</span>
</a>
</li>
<li data-id="cross-product-footer-card-sagevideo" data-item-name="cross-product-footer-card-sagevideo">
<a href="https://sk.sagepub.com/video?utm_source=cross-product-footer&utm_medium=cross-product" target="_blank" rel="noopener" class="sagevideo">
<span class="product-name">SAGE Video</span> Streaming video collections <span class="offscreen">opens in new tab</span>
</a>
</li>
</ul>
</div>
</main>
</div></div>
</div>
</div>

<div class="widget general-html none  widget-none  widget-compact-all" id="4c8a6b02-2938-4d47-8324-a3ffe9c0abdd">
<div class="wrapped ">
<div class="widget-body body body-none  body-compact-all"><div class="SAGEFooterOuterContainer">
<div class="SAGEFooterContainer smallFont">
<div class="topLeftFooter">
<h2>SAGE Journals</h2>
<a href="http://www.sagepub.com/journals.nav">
<span>About</span><br>
</a>
<a href="https://us.sagepub.com/en-us/nam/privacy-policy">
<span>Privacy Policy</span><br>
</a>
<a href="/page/policies/terms-of-use">
<span>Terms of Use</span><br>
</a>
<a href="/page/contact/home">
<span>Contact Us</span><br>
</a>
<a href="https://journalssolutions.sagepub.com/support/home">
<span>Help</span><br>
</a>
<a href="/page/help/accessibility">
<span>Accessibility</span><br>
</a>
</div>
<div class="topRightFooter">
<h2>Browse</h2>
<a href="/action/showPublications?category=10.1177%2Fhealth-sciences">
<span>Health Sciences</span><br>
</a>
<a href="/action/showPublications?category=10.1177%2Flife-and-biomedical-sciences">
<span>Life Sciences</span><br>
</a>
<a href="/action/showPublications?category=10.1177%2Fmaterials-science-and-engineering">
<span>Materials Science & Engineering</span><br>
</a>
<a href="/action/showPublications?category=10.1177%2Fsocial-sciences-and-humanities">
<span>Social Sciences & Humanities</span><br>
</a>
<a href="/action/showPublications?alphabetRange=A">
<span>Journals A-Z</span><br>
</a>
<a href="https://journals.sagepub.com/disciplines">
<span>Discipline Hubs</span><br>
</a>
</div>
<div class="bottomLeftFooter">
<h2>Resources</h2>
<a href="https://sagepub.com/journal-author-gateway">
<span>Authors</span><br>
</a>
<a href="https://sagepub.com/journal-editor-gateway">
<span>Editors</span><br>
</a>
<a href="https://journalssolutions.sagepub.com/support/solutions/folders/7000040676">
<span>Reviewers</span><br>
</a>
<a href="https://journalssolutions.sagepub.com/support/home">
<span>Librarians</span><br>
</a>
<a href="https://journalssolutions.sagepub.com/support/solutions/folders/7000040675">
<span>Researchers</span><br>
</a>
<a href="https://journalssolutions.sagepub.com/support/solutions/folders/7000040677">
<span>Societies</span><br>
</a>
</div>
<div class="bottomRightFooter">
<h2>Opportunities</h2>
<a href="https://us.sagepub.com/en-us/nam/ratecards">
<span>Advertising</span><br>
</a>
<a href="http://www.uk.sagepub.com/rate-reprints.cp">
<span>Reprints</span><br>
</a>
<a href="https://us.sagepub.com/en-us/nam/content-sponsorship">
<span>Content Sponsorships</span><br>
</a>
<a href="http://www.sagepub.com/journalsPermissions.nav">
<span>Permissions</span><br>
</a>
<a href="https://journals.sagepub.com/opportunities/microsites">
<span>Microsites</span><br>
</a>
</div>
<div class="issnFooter">
<br>
<br>
</div>
<div class="SAGECopyright">
<span class="copyrightText">Copyright © 2020 by </span>
<span class="copyrightSAGELink">SAGE Publications</span>
</div>
</div>
</div></div>
</div>
</div>
</div>
</footer></div>
</div>
</div>
</main></div>
</div>
</div>

<div class="widget literatumAd none  widget-none  widget-compact-all" id="89674502-522e-4db9-a0ea-49c2d920ba90">
<div class="wrapped ">
<div class="widget-body body body-none  body-compact-all"><div class="pb-ad">
<img id="ad-blocker-test-image" src="data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7" alt="">
<script src="/pb-assets/JS/ads-1586946825630.js" type="text/javascript"></script>
</div></div>
</div>
</div>
<div class="widget cookiePolicy none  widget-none  widget-compact-all" id="5c3f5caa-a39a-4a6f-9775-625fa6703ced">
<div class="wrapped ">
<div class="widget-body body body-none  body-compact-all"><div id="cookieBanner" class="cookieBanner">
<h4 class="b-header">Cookies Notification</h4>
<div class="b-body" tabindex="0" style="padding-bottom: 5px;">
This site uses cookies. By continuing to browse
the site you are agreeing to our use of cookies.
<a href="/page/cookie-policy" title="Learn more about cookies">Find out more.</a>
<br>
<input id="accept-cookie-policy" type="button" title="Dismiss cookie message" value="Accept" />
</div>
</div>
<script type="text/javascript">
    $("#accept-cookie-policy").click(function() {
        $.get('/action/cookiePolicy?response=accept', function(data) {
            $(".cookiePolicy").remove();
        });

    });
</script></div>
</div>
</div>
</div>
</div>
</body>
</html>
'''