(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-55e64c53"],{"0481":function(t,e,n){"use strict";var a=n("23e7"),r=n("a2bf"),i=n("7b0b"),s=n("50c4"),o=n("a691"),c=n("65f0");a({target:"Array",proto:!0},{flat:function(){var t=arguments.length?arguments[0]:void 0,e=i(this),n=s(e.length),a=c(e,0);return a.length=r(a,e,e,n,0,void 0===t?1:o(t)),a}})},"0789":function(t,e,n){"use strict";n.d(e,"f",(function(){return u})),n.d(e,"e",(function(){return d})),n.d(e,"c",(function(){return h})),n.d(e,"d",(function(){return p})),n.d(e,"a",(function(){return f})),n.d(e,"b",(function(){return v}));n("99af");var a=n("d9f7");function r(){for(var t,e=arguments.length>0&&void 0!==arguments[0]?arguments[0]:[],n=arguments.length,a=new Array(n>1?n-1:0),r=1;r<n;r++)a[r-1]=arguments[r];return(t=Array()).concat.apply(t,[e].concat(a))}function i(t){var e=arguments.length>1&&void 0!==arguments[1]?arguments[1]:"top center 0",n=arguments.length>2?arguments[2]:void 0;return{name:t,functional:!0,props:{group:{type:Boolean,default:!1},hideOnLeave:{type:Boolean,default:!1},leaveAbsolute:{type:Boolean,default:!1},mode:{type:String,default:n},origin:{type:String,default:e}},render:function(e,n){var i="transition".concat(n.props.group?"-group":""),s={props:{name:t,mode:n.props.mode},on:{beforeEnter:function(t){t.style.transformOrigin=n.props.origin,t.style.webkitTransformOrigin=n.props.origin}}};return n.props.leaveAbsolute&&(s.on.leave=r(s.on.leave,(function(t){return t.style.position="absolute"}))),n.props.hideOnLeave&&(s.on.leave=r(s.on.leave,(function(t){return t.style.display="none"}))),e(i,Object(a["a"])(n.data,s),n.children)}}}function s(t,e){var n=arguments.length>2&&void 0!==arguments[2]?arguments[2]:"in-out";return{name:t,functional:!0,props:{mode:{type:String,default:n}},render:function(n,r){return n("transition",Object(a["a"])(r.data,{props:{name:t},on:e}),r.children)}}}var o=n("ade3"),c=n("80d2"),l=function(){var t=arguments.length>0&&void 0!==arguments[0]?arguments[0]:"",e=arguments.length>1&&void 0!==arguments[1]&&arguments[1],n=e?"width":"height",a="offset".concat(Object(c["w"])(n));return{beforeEnter:function(t){t._parent=t.parentNode,t._initialStyle=Object(o["a"])({transition:t.style.transition,overflow:t.style.overflow},n,t.style[n])},enter:function(e){var r=e._initialStyle;e.style.setProperty("transition","none","important"),e.style.overflow="hidden";var i="".concat(e[a],"px");e.style[n]="0",e.offsetHeight,e.style.transition=r.transition,t&&e._parent&&e._parent.classList.add(t),requestAnimationFrame((function(){e.style[n]=i}))},afterEnter:i,enterCancelled:i,leave:function(t){t._initialStyle=Object(o["a"])({transition:"",overflow:t.style.overflow},n,t.style[n]),t.style.overflow="hidden",t.style[n]="".concat(t[a],"px"),t.offsetHeight,requestAnimationFrame((function(){return t.style[n]="0"}))},afterLeave:r,leaveCancelled:r};function r(e){t&&e._parent&&e._parent.classList.remove(t),i(e)}function i(t){var e=t._initialStyle[n];t.style.overflow=t._initialStyle.overflow,null!=e&&(t.style[n]=e),delete t._initialStyle}},u=(i("carousel-transition"),i("carousel-reverse-transition"),i("tab-transition")),d=i("tab-reverse-transition"),h=(i("menu-transition"),i("fab-transition","center center","out-in"),i("dialog-transition"),i("dialog-bottom-transition"),i("fade-transition")),p=(i("scale-transition"),i("scroll-x-transition"),i("scroll-x-reverse-transition"),i("scroll-y-transition"),i("scroll-y-reverse-transition"),i("slide-x-transition")),f=(i("slide-x-reverse-transition"),i("slide-y-transition"),i("slide-y-reverse-transition"),s("expand-transition",l())),v=s("expand-x-transition",l("",!0))},"10d2":function(t,e,n){"use strict";var a=n("8dd9");e["a"]=a["a"]},"1c87":function(t,e,n){"use strict";n("99af"),n("ac1f"),n("5319"),n("498a"),n("9911");var a=n("ade3"),r=n("5530"),i=n("2b0e"),s=n("5607"),o=n("80d2");e["a"]=i["default"].extend({name:"routable",directives:{Ripple:s["a"]},props:{activeClass:String,append:Boolean,disabled:Boolean,exact:{type:Boolean,default:void 0},exactActiveClass:String,link:Boolean,href:[String,Object],to:[String,Object],nuxt:Boolean,replace:Boolean,ripple:{type:[Boolean,Object],default:null},tag:String,target:String},data:function(){return{isActive:!1,proxyClass:""}},computed:{classes:function(){var t={};return this.to||(this.activeClass&&(t[this.activeClass]=this.isActive),this.proxyClass&&(t[this.proxyClass]=this.isActive)),t},computedRipple:function(){var t;return null!=(t=this.ripple)?t:!this.disabled&&this.isClickable},isClickable:function(){return!this.disabled&&Boolean(this.isLink||this.$listeners.click||this.$listeners["!click"]||this.$attrs.tabindex)},isLink:function(){return this.to||this.href||this.link},styles:function(){return{}}},watch:{$route:"onRouteChange"},methods:{click:function(t){this.$emit("click",t)},generateRouteLink:function(){var t,e,n=this.exact,i=(t={attrs:{tabindex:"tabindex"in this.$attrs?this.$attrs.tabindex:void 0},class:this.classes,style:this.styles,props:{},directives:[{name:"ripple",value:this.computedRipple}]},Object(a["a"])(t,this.to?"nativeOn":"on",Object(r["a"])(Object(r["a"])({},this.$listeners),{},{click:this.click})),Object(a["a"])(t,"ref","link"),t);if("undefined"===typeof this.exact&&(n="/"===this.to||this.to===Object(this.to)&&"/"===this.to.path),this.to){var s=this.activeClass,o=this.exactActiveClass||s;this.proxyClass&&(s="".concat(s," ").concat(this.proxyClass).trim(),o="".concat(o," ").concat(this.proxyClass).trim()),e=this.nuxt?"nuxt-link":"router-link",Object.assign(i.props,{to:this.to,exact:n,activeClass:s,exactActiveClass:o,append:this.append,replace:this.replace})}else e=(this.href?"a":this.tag)||"div","a"===e&&this.href&&(i.attrs.href=this.href);return this.target&&(i.attrs.target=this.target),{tag:e,data:i}},onRouteChange:function(){var t=this;if(this.to&&this.$refs.link&&this.$route){var e="".concat(this.activeClass," ").concat(this.proxyClass||"").trim(),n="_vnode.data.class.".concat(e);this.$nextTick((function(){Object(o["l"])(t.$refs.link,n)&&t.toggle()}))}},toggle:function(){}}})},"21d1":function(t,e,n){"use strict";n.d(e,"a",(function(){return p}));n("96cf");var a=n("1da1"),r=n("d4ec"),i=n("bee2"),s=n("262e"),o=n("2caf"),c=n("9ab4"),l=n("8d27"),u=n("dcc8"),d=n("0613"),h=function(t){Object(s["a"])(n,t);var e=Object(o["a"])(n);function n(){var t;return Object(r["a"])(this,n),t=e.apply(this,arguments),t.user=null,t.permission=null,t.routeUser="/",t}return Object(i["a"])(n,[{key:"autoCreateProfile",value:function(){var t=Object(a["a"])(regeneratorRuntime.mark((function t(e){return regeneratorRuntime.wrap((function(t){while(1)switch(t.prev=t.next){case 0:return t.abrupt("return",u["a"].postHttp("/api/profile/create/",e));case 1:case"end":return t.stop()}}),t)})));function e(e){return t.apply(this,arguments)}return e}()},{key:"loadUser",value:function(){var t=Object(a["a"])(regeneratorRuntime.mark((function t(){var e;return regeneratorRuntime.wrap((function(t){while(1)switch(t.prev=t.next){case 0:return t.next=2,u["a"].getHttp("/api/ita/v2/user/");case 2:e=t.sent,this.user=e,this.permission=e.is_staff,1==e.is_staff||0==e.is_staff?this.routeUser=e.is_staff?"/admin/":"/user/":this.routeUser="/";case 6:case"end":return t.stop()}}),t,this)})));function e(){return t.apply(this,arguments)}return e}()},{key:"getUser",value:function(){var t=Object(a["a"])(regeneratorRuntime.mark((function t(){return regeneratorRuntime.wrap((function(t){while(1)switch(t.prev=t.next){case 0:return t.next=2,u["a"].getHttp("/api/ita/v2/user/");case 2:return t.abrupt("return",t.sent);case 3:case"end":return t.stop()}}),t)})));function e(){return t.apply(this,arguments)}return e}()}]),n}(l["b"]);h=Object(c["c"])([Object(l["a"])({generateMutationSetters:!0})],h);var p=new h({store:d["a"],name:"User"})},"25a8":function(t,e,n){},"297c":function(t,e,n){"use strict";n("a9e3");var a=n("2b0e"),r=n("37c6");e["a"]=a["default"].extend().extend({name:"loadable",props:{loading:{type:[Boolean,String],default:!1},loaderHeight:{type:[Number,String],default:2}},methods:{genProgress:function(){return!1===this.loading?null:this.$slots.progress||this.$createElement(r["a"],{props:{absolute:!0,color:!0===this.loading||""===this.loading?this.color||"primary":this.loading,height:this.loaderHeight,indeterminate:!0}})}}})},"2fa4":function(t,e,n){"use strict";n("20f6");var a=n("80d2");e["a"]=Object(a["g"])("spacer","div","v-spacer")},3408:function(t,e,n){},"37c6":function(t,e,n){"use strict";var a=n("8e36");e["a"]=a["a"]},4069:function(t,e,n){var a=n("44d2");a("flat")},5607:function(t,e,n){"use strict";n("99af"),n("b0c0"),n("a9e3"),n("d3b7"),n("25f0"),n("7435");var a=n("80d2"),r=80;function i(t,e){t.style.transform=e,t.style.webkitTransform=e}function s(t,e){t.style.opacity=e.toString()}function o(t){return"TouchEvent"===t.constructor.name}function c(t){return"KeyboardEvent"===t.constructor.name}var l=function(t,e){var n=arguments.length>2&&void 0!==arguments[2]?arguments[2]:{},a=0,r=0;if(!c(t)){var i=e.getBoundingClientRect(),s=o(t)?t.touches[t.touches.length-1]:t;a=s.clientX-i.left,r=s.clientY-i.top}var l=0,u=.3;e._ripple&&e._ripple.circle?(u=.15,l=e.clientWidth/2,l=n.center?l:l+Math.sqrt(Math.pow(a-l,2)+Math.pow(r-l,2))/4):l=Math.sqrt(Math.pow(e.clientWidth,2)+Math.pow(e.clientHeight,2))/2;var d="".concat((e.clientWidth-2*l)/2,"px"),h="".concat((e.clientHeight-2*l)/2,"px"),p=n.center?d:"".concat(a-l,"px"),f=n.center?h:"".concat(r-l,"px");return{radius:l,scale:u,x:p,y:f,centerX:d,centerY:h}},u={show:function(t,e){var n=arguments.length>2&&void 0!==arguments[2]?arguments[2]:{};if(e._ripple&&e._ripple.enabled){var a=document.createElement("span"),r=document.createElement("span");a.appendChild(r),a.className="v-ripple__container",n.class&&(a.className+=" ".concat(n.class));var o=l(t,e,n),c=o.radius,u=o.scale,d=o.x,h=o.y,p=o.centerX,f=o.centerY,v="".concat(2*c,"px");r.className="v-ripple__animation",r.style.width=v,r.style.height=v,e.appendChild(a);var m=window.getComputedStyle(e);m&&"static"===m.position&&(e.style.position="relative",e.dataset.previousPosition="static"),r.classList.add("v-ripple__animation--enter"),r.classList.add("v-ripple__animation--visible"),i(r,"translate(".concat(d,", ").concat(h,") scale3d(").concat(u,",").concat(u,",").concat(u,")")),s(r,0),r.dataset.activated=String(performance.now()),setTimeout((function(){r.classList.remove("v-ripple__animation--enter"),r.classList.add("v-ripple__animation--in"),i(r,"translate(".concat(p,", ").concat(f,") scale3d(1,1,1)")),s(r,.25)}),0)}},hide:function(t){if(t&&t._ripple&&t._ripple.enabled){var e=t.getElementsByClassName("v-ripple__animation");if(0!==e.length){var n=e[e.length-1];if(!n.dataset.isHiding){n.dataset.isHiding="true";var a=performance.now()-Number(n.dataset.activated),r=Math.max(250-a,0);setTimeout((function(){n.classList.remove("v-ripple__animation--in"),n.classList.add("v-ripple__animation--out"),s(n,0),setTimeout((function(){var e=t.getElementsByClassName("v-ripple__animation");1===e.length&&t.dataset.previousPosition&&(t.style.position=t.dataset.previousPosition,delete t.dataset.previousPosition),n.parentNode&&t.removeChild(n.parentNode)}),300)}),r)}}}}};function d(t){return"undefined"===typeof t||!!t}function h(t){var e={},n=t.currentTarget;if(n&&n._ripple&&!n._ripple.touched){if(o(t))n._ripple.touched=!0,n._ripple.isTouch=!0;else if(n._ripple.isTouch)return;if(e.center=n._ripple.centered||c(t),n._ripple.class&&(e.class=n._ripple.class),o(t)){if(n._ripple.showTimerCommit)return;n._ripple.showTimerCommit=function(){u.show(t,n,e)},n._ripple.showTimer=window.setTimeout((function(){n&&n._ripple&&n._ripple.showTimerCommit&&(n._ripple.showTimerCommit(),n._ripple.showTimerCommit=null)}),r)}else u.show(t,n,e)}}function p(t){var e=t.currentTarget;if(e&&e._ripple){if(window.clearTimeout(e._ripple.showTimer),"touchend"===t.type&&e._ripple.showTimerCommit)return e._ripple.showTimerCommit(),e._ripple.showTimerCommit=null,void(e._ripple.showTimer=setTimeout((function(){p(t)})));window.setTimeout((function(){e._ripple&&(e._ripple.touched=!1)})),u.hide(e)}}function f(t){var e=t.currentTarget;e&&e._ripple&&(e._ripple.showTimerCommit&&(e._ripple.showTimerCommit=null),window.clearTimeout(e._ripple.showTimer))}var v=!1;function m(t){v||t.keyCode!==a["r"].enter&&t.keyCode!==a["r"].space||(v=!0,h(t))}function g(t){v=!1,p(t)}function b(t,e,n){var a=d(e.value);a||u.hide(t),t._ripple=t._ripple||{},t._ripple.enabled=a;var r=e.value||{};r.center&&(t._ripple.centered=!0),r.class&&(t._ripple.class=e.value.class),r.circle&&(t._ripple.circle=r.circle),a&&!n?(t.addEventListener("touchstart",h,{passive:!0}),t.addEventListener("touchend",p,{passive:!0}),t.addEventListener("touchmove",f,{passive:!0}),t.addEventListener("touchcancel",p),t.addEventListener("mousedown",h),t.addEventListener("mouseup",p),t.addEventListener("mouseleave",p),t.addEventListener("keydown",m),t.addEventListener("keyup",g),t.addEventListener("dragstart",p,{passive:!0})):!a&&n&&y(t)}function y(t){t.removeEventListener("mousedown",h),t.removeEventListener("touchstart",h),t.removeEventListener("touchend",p),t.removeEventListener("touchmove",f),t.removeEventListener("touchcancel",p),t.removeEventListener("mouseup",p),t.removeEventListener("mouseleave",p),t.removeEventListener("keydown",m),t.removeEventListener("keyup",g),t.removeEventListener("dragstart",p)}function _(t,e,n){b(t,e,!1)}function x(t){delete t._ripple,y(t)}function w(t,e){if(e.value!==e.oldValue){var n=d(e.oldValue);b(t,e,n)}}var C={bind:_,unbind:x,update:w};e["a"]=C},"615b":function(t,e,n){},"6ece":function(t,e,n){},7435:function(t,e,n){},"7e2b":function(t,e,n){"use strict";var a=n("2b0e");function r(t){return function(e,n){for(var a in n)Object.prototype.hasOwnProperty.call(e,a)||this.$delete(this.$data[t],a);for(var r in e)this.$set(this.$data[t],r,e[r])}}e["a"]=a["default"].extend({data:function(){return{attrs$:{},listeners$:{}}},created:function(){this.$watch("$attrs",r("attrs$"),{immediate:!0}),this.$watch("$listeners",r("listeners$"),{immediate:!0})}})},8212:function(t,e,n){"use strict";n("a9e3");var a=n("5530"),r=(n("3408"),n("a9ad")),i=n("24b2"),s=n("a236"),o=n("80d2"),c=n("58df");e["a"]=Object(c["a"])(r["a"],i["a"],s["a"]).extend({name:"v-avatar",props:{left:Boolean,right:Boolean,size:{type:[Number,String],default:48}},computed:{classes:function(){return Object(a["a"])({"v-avatar--left":this.left,"v-avatar--right":this.right},this.roundedClasses)},styles:function(){return Object(a["a"])({height:Object(o["f"])(this.size),minWidth:Object(o["f"])(this.size),width:Object(o["f"])(this.size)},this.measurableStyles)}},render:function(t){var e={staticClass:"v-avatar",class:this.classes,style:this.styles,on:this.$listeners};return t("div",this.setBackgroundColor(this.color,e),this.$slots.default)}})},"8dd9":function(t,e,n){"use strict";var a=n("5530"),r=(n("25a8"),n("7e2b")),i=n("a9ad"),s=(n("a9e3"),n("ade3")),o=n("2b0e"),c=o["default"].extend({name:"elevatable",props:{elevation:[Number,String]},computed:{computedElevation:function(){return this.elevation},elevationClasses:function(){var t=this.computedElevation;return null==t||isNaN(parseInt(t))?{}:Object(s["a"])({},"elevation-".concat(this.elevation),!0)}}}),l=n("24b2"),u=n("a236"),d=n("7560"),h=n("58df");e["a"]=Object(h["a"])(r["a"],i["a"],c,l["a"],u["a"],d["a"]).extend({name:"v-sheet",props:{outlined:Boolean,shaped:Boolean,tag:{type:String,default:"div"}},computed:{classes:function(){return Object(a["a"])(Object(a["a"])(Object(a["a"])({"v-sheet":!0,"v-sheet--outlined":this.outlined,"v-sheet--shaped":this.shaped},this.themeClasses),this.elevationClasses),this.roundedClasses)},styles:function(){return this.measurableStyles}},render:function(t){var e={class:this.classes,style:this.styles,on:this.listeners$};return t(this.tag,this.setBackgroundColor(this.color,e),this.$slots.default)}})},"8e36":function(t,e,n){"use strict";n("a9e3"),n("c7cd");var a=n("5530"),r=n("ade3"),i=(n("6ece"),n("0789")),s=n("a9ad"),o=n("fe6c"),c=n("a452"),l=n("7560"),u=n("80d2"),d=n("58df"),h=Object(d["a"])(s["a"],Object(o["b"])(["absolute","fixed","top","bottom"]),c["a"],l["a"]);e["a"]=h.extend({name:"v-progress-linear",props:{active:{type:Boolean,default:!0},backgroundColor:{type:String,default:null},backgroundOpacity:{type:[Number,String],default:null},bufferValue:{type:[Number,String],default:100},color:{type:String,default:"primary"},height:{type:[Number,String],default:4},indeterminate:Boolean,query:Boolean,reverse:Boolean,rounded:Boolean,stream:Boolean,striped:Boolean,value:{type:[Number,String],default:0}},data:function(){return{internalLazyValue:this.value||0}},computed:{__cachedBackground:function(){return this.$createElement("div",this.setBackgroundColor(this.backgroundColor||this.color,{staticClass:"v-progress-linear__background",style:this.backgroundStyle}))},__cachedBar:function(){return this.$createElement(this.computedTransition,[this.__cachedBarType])},__cachedBarType:function(){return this.indeterminate?this.__cachedIndeterminate:this.__cachedDeterminate},__cachedBuffer:function(){return this.$createElement("div",{staticClass:"v-progress-linear__buffer",style:this.styles})},__cachedDeterminate:function(){return this.$createElement("div",this.setBackgroundColor(this.color,{staticClass:"v-progress-linear__determinate",style:{width:Object(u["f"])(this.normalizedValue,"%")}}))},__cachedIndeterminate:function(){return this.$createElement("div",{staticClass:"v-progress-linear__indeterminate",class:{"v-progress-linear__indeterminate--active":this.active}},[this.genProgressBar("long"),this.genProgressBar("short")])},__cachedStream:function(){return this.stream?this.$createElement("div",this.setTextColor(this.color,{staticClass:"v-progress-linear__stream",style:{width:Object(u["f"])(100-this.normalizedBuffer,"%")}})):null},backgroundStyle:function(){var t,e=null==this.backgroundOpacity?this.backgroundColor?1:.3:parseFloat(this.backgroundOpacity);return t={opacity:e},Object(r["a"])(t,this.isReversed?"right":"left",Object(u["f"])(this.normalizedValue,"%")),Object(r["a"])(t,"width",Object(u["f"])(this.normalizedBuffer-this.normalizedValue,"%")),t},classes:function(){return Object(a["a"])({"v-progress-linear--absolute":this.absolute,"v-progress-linear--fixed":this.fixed,"v-progress-linear--query":this.query,"v-progress-linear--reactive":this.reactive,"v-progress-linear--reverse":this.isReversed,"v-progress-linear--rounded":this.rounded,"v-progress-linear--striped":this.striped},this.themeClasses)},computedTransition:function(){return this.indeterminate?i["c"]:i["d"]},isReversed:function(){return this.$vuetify.rtl!==this.reverse},normalizedBuffer:function(){return this.normalize(this.bufferValue)},normalizedValue:function(){return this.normalize(this.internalLazyValue)},reactive:function(){return Boolean(this.$listeners.change)},styles:function(){var t={};return this.active||(t.height=0),this.indeterminate||100===parseFloat(this.normalizedBuffer)||(t.width=Object(u["f"])(this.normalizedBuffer,"%")),t}},methods:{genContent:function(){var t=Object(u["n"])(this,"default",{value:this.internalLazyValue});return t?this.$createElement("div",{staticClass:"v-progress-linear__content"},t):null},genListeners:function(){var t=this.$listeners;return this.reactive&&(t.click=this.onClick),t},genProgressBar:function(t){return this.$createElement("div",this.setBackgroundColor(this.color,{staticClass:"v-progress-linear__indeterminate",class:Object(r["a"])({},t,!0)}))},onClick:function(t){if(this.reactive){var e=this.$el.getBoundingClientRect(),n=e.width;this.internalValue=t.offsetX/n*100}},normalize:function(t){return t<0?0:t>100?100:parseFloat(t)}},render:function(t){var e={staticClass:"v-progress-linear",attrs:{role:"progressbar","aria-valuemin":0,"aria-valuemax":this.normalizedBuffer,"aria-valuenow":this.indeterminate?void 0:this.normalizedValue},class:this.classes,style:{bottom:this.bottom?0:void 0,height:this.active?Object(u["f"])(this.height):0,top:this.top?0:void 0},on:this.genListeners()};return t("div",e,[this.__cachedStream,this.__cachedBackground,this.__cachedBuffer,this.__cachedBar,this.genContent()])}})},9187:function(t,e,n){"use strict";n.r(e);var a=function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("div",{staticClass:"relative md:pt-32 pb-32 pt-12  "},[n("div",{staticClass:"relative  flex flex-col min-w-0 break-words w-full mb-6  "},[n("div",{staticClass:"rounded-t mb-0 px-4 py-3 border-0 "},[t._m(0),n("div",{staticClass:"w-full "},[n("div",{staticClass:"flex flex-wrap justify-center"},t._l(t.assessment,(function(e,a){return n("button",{key:a,class:"bg-green-600 p-2 rounded shadow-lg m-1 text-white",on:{click:function(n){return t.getDataIssue(e.id)}}},[t._v(t._s(e.name))])})),0)]),n("div",[t.suggestion?n("v-card",{staticClass:"m-2"},[n("v-card-title",{attrs:{"primary-title":""}},[n("h2",{staticClass:"text-sm font-bold "},[t._v("ข้อเสนอแนะ")])]),n("v-card-text",t._l(t.suggestion,(function(e,a){return n("div",{key:a,staticClass:"flex p-2 "},[t._v(" "+t._s(e.suggestion)+" ")])})),0)],1):n("div",t._l(t.data,(function(e,a){return n("v-card",{key:a,staticClass:"m-2"},[n("v-card-title",{attrs:{"primary-title":""}},[n("h2",{staticClass:"text-sm font-bold"},[n("v-avatar",{staticClass:"bg-teal-500 text-white",attrs:{size:"36"}},[t._v(" i"+t._s(e.value[0].issue.order)+" ")]),t._v(" "+t._s(e.value[0].issue.name)+" ")],1)]),n("v-card-text",t._l(t.getValue(e.value),(function(e,a){return n("div",{staticClass:"flex  p-2 ",attrs:{index:a}},[t._v(" "+t._s(e.name)+" "),n("v-spacer"),t._v(" "+t._s(e.notting)+" / "+t._s(e.low)+" / "+t._s(e.many)+" /"+t._s(e.very)+" / "+t._s(e.have)+" / "+t._s(e.nohave)+" ")],1)})),0)],1)})),1)],1)])])])},r=[function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("div",{staticClass:"relative w-full mt-4 mb-4 max-w-full flex-grow flex-1 px-2 py-2"},[n("h3",{staticClass:"  text-2xl text-gray-800"},[n("span",{staticClass:"em em-briefcase text-2xl",attrs:{"aria-role":"presentation","aria-label":""}}),t._v(" ข้อมูลของหน่วยงาน ")])])}],i=(n("99af"),n("4de4"),n("d81d"),n("96cf"),n("1da1")),s=n("d4ec"),o=n("bee2"),c=n("262e"),l=n("2caf"),u=n("9ab4"),d=n("60a3"),h=n("b14a"),p=n("dcc8"),f=n("21d1"),v=n("2ef0"),m=n.n(v),g=function(t){Object(c["a"])(n,t);var e=Object(l["a"])(n);function n(){var t;return Object(s["a"])(this,n),t=e.apply(this,arguments),t.assessment=null,t.raw=null,t.suggestion=null,t.data=null,t.user={},t.years=null,t.response=!1,t}return Object(o["a"])(n,[{key:"getValue",value:function(t){for(var e=m()(t).groupBy("issueDetail_pk").map((function(t,e){return{type:e,val:t}})).value(),n=[],a=0;a<e.length;a++)console.log(a,"----------------------------"),n.push({name:e[a].val[0].issueDetail.sub_name,notting:this.sumChoice(e[a].val,"น้อยที่สุดหรือไม่มีเลย"),low:this.sumChoice(e[a].val,"น้อย"),very:this.sumChoice(e[a].val,"มาก"),many:this.sumChoice(e[a].val,"มากที่สุด"),have:this.sumChoice(e[a].val,"มี"),nohave:this.sumChoice(e[a].val,"ไม่มี")});return n}},{key:"sumChoice",value:function(t,e){var n=m.a.filter(t,{value_by:e});return console.log(n,t.length,e),n.length}},{key:"created",value:function(){var t=Object(i["a"])(regeneratorRuntime.mark((function t(){return regeneratorRuntime.wrap((function(t){while(1)switch(t.prev=t.next){case 0:return t.next=2,f["a"].getUser();case 2:return this.user=t.sent,t.next=5,p["a"].getHttp("/api/iit/v2/year/".concat(this.$route.query.year,"/"));case 5:return this.years=t.sent,t.next=8,p["a"].getHttp("/api/iit/v2/assessmentissues/?&year=".concat(this.years.id));case 8:return this.assessment=t.sent,t.next=11,this.getDataIssue(this.assessment[0].id);case 11:this.response=!0;case 12:case"end":return t.stop()}}),t,this)})));function e(){return t.apply(this,arguments)}return e}()},{key:"getDataIssue",value:function(){var t=Object(i["a"])(regeneratorRuntime.mark((function t(e){return regeneratorRuntime.wrap((function(t){while(1)switch(t.prev=t.next){case 0:return t.next=2,p["a"].getHttp("/api/iit/v2/answerissue-report/?agency=".concat(this.user.ext_link.agency,"&assessmentIssues=").concat(e));case 2:if(this.raw=t.sent,!(this.raw.length>0)){t.next=9;break}return t.next=6,this.convertData();case 6:this.suggestion=null,t.next=12;break;case 9:return t.next=11,p["a"].getHttp("/api/iit/v2/answersuggestion/?agency=".concat(this.user.ext_link.agency,"&year=").concat(this.years.id));case 11:this.suggestion=t.sent;case 12:case"end":return t.stop()}}),t,this)})));function e(e){return t.apply(this,arguments)}return e}()},{key:"convertData",value:function(){var t=Object(i["a"])(regeneratorRuntime.mark((function t(){var e;return regeneratorRuntime.wrap((function(t){while(1)switch(t.prev=t.next){case 0:return e=this.raw,t.next=3,m.a.chain(e).groupBy("issue_pk").map((function(t,e){return{group:e,value:t}})).value();case 3:e=t.sent,this.data=e;case 5:case"end":return t.stop()}}),t,this)})));function e(){return t.apply(this,arguments)}return e}()},{key:"convertDataAssign",value:function(){var t=Object(i["a"])(regeneratorRuntime.mark((function t(){var e;return regeneratorRuntime.wrap((function(t){while(1)switch(t.prev=t.next){case 0:return e=this.raw,t.next=3,m.a.chain(e).groupBy("issue_pk").map((function(t,e){return{group:e,value:t}})).value();case 3:e=t.sent,this.data=e;case 5:case"end":return t.stop()}}),t,this)})));function e(){return t.apply(this,arguments)}return e}()}]),n}(d["b"]);g=Object(u["c"])([Object(d["a"])({components:{CardStats:h["a"]}})],g);var b=g,y=b,_=(n("db07"),n("2877")),x=n("6544"),w=n.n(x),C=n("8212"),O=n("b0af"),j=n("99d9"),k=n("2fa4"),B=Object(_["a"])(y,a,r,!1,null,null,null);e["default"]=B.exports;w()(B,{VAvatar:C["a"],VCard:O["a"],VCardText:j["b"],VCardTitle:j["c"],VSpacer:k["a"]})},9911:function(t,e,n){"use strict";var a=n("23e7"),r=n("857a"),i=n("af03");a({target:"String",proto:!0,forced:i("link")},{link:function(t){return r(this,"a","href",t)}})},"99d9":function(t,e,n){"use strict";n.d(e,"a",(function(){return i})),n.d(e,"b",(function(){return o})),n.d(e,"c",(function(){return c}));var a=n("b0af"),r=n("80d2"),i=Object(r["g"])("v-card__actions"),s=Object(r["g"])("v-card__subtitle"),o=Object(r["g"])("v-card__text"),c=Object(r["g"])("v-card__title");a["a"]},a236:function(t,e,n){"use strict";n("a15b"),n("ac1f"),n("1276");var a=n("ade3"),r=n("b85c"),i=n("2b0e");e["a"]=i["default"].extend({name:"roundable",props:{rounded:[Boolean,String],tile:Boolean},computed:{roundedClasses:function(){var t=[],e="string"===typeof this.rounded?String(this.rounded):!0===this.rounded;if(this.tile)t.push("rounded-0");else if("string"===typeof e){var n,i=e.split(" "),s=Object(r["a"])(i);try{for(s.s();!(n=s.n()).done;){var o=n.value;t.push("rounded-".concat(o))}}catch(c){s.e(c)}finally{s.f()}}else e&&t.push("rounded");return t.length>0?Object(a["a"])({},t.join(" "),!0):{}}}})},a2bf:function(t,e,n){"use strict";var a=n("e8b5"),r=n("50c4"),i=n("0366"),s=function(t,e,n,o,c,l,u,d){var h,p=c,f=0,v=!!u&&i(u,d,3);while(f<o){if(f in n){if(h=v?v(n[f],f,e):n[f],l>0&&a(h))p=s(t,e,h,r(h.length),p,l-1)-1;else{if(p>=9007199254740991)throw TypeError("Exceed the acceptable array length");t[p]=h}p++}f++}return p};t.exports=s},a452:function(t,e,n){"use strict";var a=n("ade3"),r=n("2b0e");function i(){var t=arguments.length>0&&void 0!==arguments[0]?arguments[0]:"value",e=arguments.length>1&&void 0!==arguments[1]?arguments[1]:"change";return r["default"].extend({name:"proxyable",model:{prop:t,event:e},props:Object(a["a"])({},t,{required:!1}),data:function(){return{internalLazyValue:this[t]}},computed:{internalValue:{get:function(){return this.internalLazyValue},set:function(t){t!==this.internalLazyValue&&(this.internalLazyValue=t,this.$emit(e,t))}}},watch:Object(a["a"])({},t,(function(t){this.internalLazyValue=t}))})}var s=i();e["a"]=s},a9ad:function(t,e,n){"use strict";n("d3b7"),n("ac1f"),n("25f0"),n("1276"),n("498a");var a=n("3835"),r=n("ade3"),i=n("5530"),s=n("2b0e"),o=n("d9bd"),c=n("7bc6");e["a"]=s["default"].extend({name:"colorable",props:{color:String},methods:{setBackgroundColor:function(t){var e=arguments.length>1&&void 0!==arguments[1]?arguments[1]:{};return"string"===typeof e.style?(Object(o["b"])("style must be an object",this),e):"string"===typeof e.class?(Object(o["b"])("class must be an object",this),e):(Object(c["d"])(t)?e.style=Object(i["a"])(Object(i["a"])({},e.style),{},{"background-color":"".concat(t),"border-color":"".concat(t)}):t&&(e.class=Object(i["a"])(Object(i["a"])({},e.class),{},Object(r["a"])({},t,!0))),e)},setTextColor:function(t){var e=arguments.length>1&&void 0!==arguments[1]?arguments[1]:{};if("string"===typeof e.style)return Object(o["b"])("style must be an object",this),e;if("string"===typeof e.class)return Object(o["b"])("class must be an object",this),e;if(Object(c["d"])(t))e.style=Object(i["a"])(Object(i["a"])({},e.style),{},{color:"".concat(t),"caret-color":"".concat(t)});else if(t){var n=t.toString().trim().split(" ",2),s=Object(a["a"])(n,2),l=s[0],u=s[1];e.class=Object(i["a"])(Object(i["a"])({},e.class),{},Object(r["a"])({},l+"--text",!0)),u&&(e.class["text--"+u]=!0)}return e}}})},b0af:function(t,e,n){"use strict";n("0481"),n("4069"),n("a9e3");var a=n("5530"),r=(n("615b"),n("10d2")),i=n("297c"),s=n("1c87"),o=n("58df");e["a"]=Object(o["a"])(i["a"],s["a"],r["a"]).extend({name:"v-card",props:{flat:Boolean,hover:Boolean,img:String,link:Boolean,loaderHeight:{type:[Number,String],default:4},raised:Boolean},computed:{classes:function(){return Object(a["a"])(Object(a["a"])({"v-card":!0},s["a"].options.computed.classes.call(this)),{},{"v-card--flat":this.flat,"v-card--hover":this.hover,"v-card--link":this.isClickable,"v-card--loading":this.loading,"v-card--disabled":this.disabled,"v-card--raised":this.raised},r["a"].options.computed.classes.call(this))},styles:function(){var t=Object(a["a"])({},r["a"].options.computed.styles.call(this));return this.img&&(t.background='url("'.concat(this.img,'") center center / cover no-repeat')),t}},methods:{genProgress:function(){var t=i["a"].options.methods.genProgress.call(this);return t?this.$createElement("div",{staticClass:"v-card__progress",key:"progress"},[t]):null}},render:function(t){var e=this.generateRouteLink(),n=e.tag,a=e.data;return a.style=this.styles,this.isClickable&&(a.attrs=a.attrs||{},a.attrs.tabindex=0),t(n,this.setBackgroundColor(this.color,a),[this.genProgress(),this.$slots.default])}})},b14a:function(t,e,n){"use strict";var a=function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("div",{staticClass:"relative flex flex-col min-w-0 break-words bg-white rounded-lg  shadow-xl mb-6 xl:mb-0 shadow-lg border-b-4 border-green-600"},[n("div",{staticClass:"flex-auto p-4"},[n("div",{staticClass:"flex flex-wrap"},[n("div",{staticClass:"relative w-full pr-4 max-w-full flex-grow flex-1"},[n("span",{staticClass:"font-semibold text-xl text-gray-800"},[t._v(" "+t._s(t.statTitle)+" ")]),n("h5",{staticClass:"text-gray-500 uppercase font-bold text-xs"},[t._v(" "+t._s(t.statSubtitle)+" ")]),n("div",{},[n("button",{staticClass:"mt-2 text-green-600 font-bold text-tiny",on:{click:function(e){return t.$router.push(t.statRoute)}}},[t._v("ดูรายระเอียด")])])]),n("div",{staticClass:"relative w-auto pl-4 flex-initial"},[n("div",{staticClass:"text-white p-3 text-center inline-flex items-center justify-center w-12 h-12 shadow-lg rounded-full text-xl",class:[t.statIconColor]},[n("i",{class:[t.statIconName]})])])])])])},r=[],i=(n("c975"),{name:"card-stats",props:{statSubtitle:{type:String,default:"Traffic"},statArrow:{default:"up",validator:function(t){return-1!==["up","down"].indexOf(t)}},statPercent:{type:String,default:"3.48"},statPercentColor:{type:String,default:"text-green-500"},statTitle:{type:String,default:"350,897"},statDescripiron:{type:String,default:"Since last month"},statIconName:{type:String,default:"far fa-chart-bar"},statIconColor:{type:String,default:"bg-red-500"},statRoute:{type:String,default:"#"}}}),s=i,o=n("2877"),c=Object(o["a"])(s,a,r,!1,null,null,null);e["a"]=c.exports},c7cd:function(t,e,n){"use strict";var a=n("23e7"),r=n("857a"),i=n("af03");a({target:"String",proto:!0,forced:i("fixed")},{fixed:function(){return r(this,"tt","","")}})},db07:function(t,e,n){"use strict";n("db94")},db94:function(t,e,n){},fe6c:function(t,e,n){"use strict";n.d(e,"b",(function(){return s}));var a=n("2b0e"),r=n("80d2"),i={absolute:Boolean,bottom:Boolean,fixed:Boolean,left:Boolean,right:Boolean,top:Boolean};function s(){var t=arguments.length>0&&void 0!==arguments[0]?arguments[0]:[];return a["default"].extend({name:"positionable",props:t.length?Object(r["j"])(i,t):i})}e["a"]=s()}}]);
//# sourceMappingURL=chunk-55e64c53.64158578.js.map