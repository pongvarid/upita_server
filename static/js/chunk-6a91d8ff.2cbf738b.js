(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-6a91d8ff"],{"0789":function(e,t,s){"use strict";s.d(t,"f",(function(){return c})),s.d(t,"e",(function(){return u})),s.d(t,"c",(function(){return d})),s.d(t,"d",(function(){return h})),s.d(t,"a",(function(){return p})),s.d(t,"b",(function(){return f}));var r=s("d9f7");function i(e=[],...t){return Array().concat(e,...t)}function n(e,t="top center 0",s){return{name:e,functional:!0,props:{group:{type:Boolean,default:!1},hideOnLeave:{type:Boolean,default:!1},leaveAbsolute:{type:Boolean,default:!1},mode:{type:String,default:s},origin:{type:String,default:t}},render(t,s){const n="transition"+(s.props.group?"-group":""),a={props:{name:e,mode:s.props.mode},on:{beforeEnter(e){e.style.transformOrigin=s.props.origin,e.style.webkitTransformOrigin=s.props.origin}}};return s.props.leaveAbsolute&&(a.on.leave=i(a.on.leave,e=>e.style.position="absolute")),s.props.hideOnLeave&&(a.on.leave=i(a.on.leave,e=>e.style.display="none")),t(n,Object(r["a"])(s.data,a),s.children)}}}function a(e,t,s="in-out"){return{name:e,functional:!0,props:{mode:{type:String,default:s}},render(s,i){return s("transition",Object(r["a"])(i.data,{props:{name:e},on:t}),i.children)}}}var o=s("80d2"),l=function(e="",t=!1){const s=t?"width":"height",r="offset"+Object(o["w"])(s);return{beforeEnter(e){e._parent=e.parentNode,e._initialStyle={transition:e.style.transition,overflow:e.style.overflow,[s]:e.style[s]}},enter(t){const i=t._initialStyle;t.style.setProperty("transition","none","important"),t.style.overflow="hidden";const n=t[r]+"px";t.style[s]="0",t.offsetHeight,t.style.transition=i.transition,e&&t._parent&&t._parent.classList.add(e),requestAnimationFrame(()=>{t.style[s]=n})},afterEnter:n,enterCancelled:n,leave(e){e._initialStyle={transition:"",overflow:e.style.overflow,[s]:e.style[s]},e.style.overflow="hidden",e.style[s]=e[r]+"px",e.offsetHeight,requestAnimationFrame(()=>e.style[s]="0")},afterLeave:i,leaveCancelled:i};function i(t){e&&t._parent&&t._parent.classList.remove(e),n(t)}function n(e){const t=e._initialStyle[s];e.style.overflow=e._initialStyle.overflow,null!=t&&(e.style[s]=t),delete e._initialStyle}};n("carousel-transition"),n("carousel-reverse-transition");const c=n("tab-transition"),u=n("tab-reverse-transition"),d=(n("menu-transition"),n("fab-transition","center center","out-in"),n("dialog-transition"),n("dialog-bottom-transition"),n("fade-transition")),h=(n("scale-transition"),n("scroll-x-transition"),n("scroll-x-reverse-transition"),n("scroll-y-transition"),n("scroll-y-reverse-transition"),n("slide-x-transition")),p=(n("slide-x-reverse-transition"),n("slide-y-transition"),n("slide-y-reverse-transition"),a("expand-transition",l())),f=a("expand-x-transition",l("",!0))},"10d2":function(e,t,s){"use strict";var r=s("8dd9");t["a"]=r["a"]},"1c87":function(e,t,s){"use strict";var r=s("2b0e"),i=s("5607"),n=s("80d2");t["a"]=r["default"].extend({name:"routable",directives:{Ripple:i["a"]},props:{activeClass:String,append:Boolean,disabled:Boolean,exact:{type:Boolean,default:void 0},exactActiveClass:String,link:Boolean,href:[String,Object],to:[String,Object],nuxt:Boolean,replace:Boolean,ripple:{type:[Boolean,Object],default:null},tag:String,target:String},data:()=>({isActive:!1,proxyClass:""}),computed:{classes(){const e={};return this.to||(this.activeClass&&(e[this.activeClass]=this.isActive),this.proxyClass&&(e[this.proxyClass]=this.isActive)),e},computedRipple(){var e;return null!=(e=this.ripple)?e:!this.disabled&&this.isClickable},isClickable(){return!this.disabled&&Boolean(this.isLink||this.$listeners.click||this.$listeners["!click"]||this.$attrs.tabindex)},isLink(){return this.to||this.href||this.link},styles:()=>({})},watch:{$route:"onRouteChange"},methods:{click(e){this.$emit("click",e)},generateRouteLink(){let e,t=this.exact;const s={attrs:{tabindex:"tabindex"in this.$attrs?this.$attrs.tabindex:void 0},class:this.classes,style:this.styles,props:{},directives:[{name:"ripple",value:this.computedRipple}],[this.to?"nativeOn":"on"]:{...this.$listeners,click:this.click},ref:"link"};if("undefined"===typeof this.exact&&(t="/"===this.to||this.to===Object(this.to)&&"/"===this.to.path),this.to){let r=this.activeClass,i=this.exactActiveClass||r;this.proxyClass&&(r=`${r} ${this.proxyClass}`.trim(),i=`${i} ${this.proxyClass}`.trim()),e=this.nuxt?"nuxt-link":"router-link",Object.assign(s.props,{to:this.to,exact:t,activeClass:r,exactActiveClass:i,append:this.append,replace:this.replace})}else e=(this.href?"a":this.tag)||"div","a"===e&&this.href&&(s.attrs.href=this.href);return this.target&&(s.attrs.target=this.target),{tag:e,data:s}},onRouteChange(){if(!this.to||!this.$refs.link||!this.$route)return;const e=`${this.activeClass} ${this.proxyClass||""}`.trim(),t="_vnode.data.class."+e;this.$nextTick(()=>{Object(n["l"])(this.$refs.link,t)&&this.toggle()})},toggle:()=>{}}})},"21d1":function(e,t,s){"use strict";s.d(t,"a",(function(){return p}));s("96cf");var r=s("1da1"),i=s("d4ec"),n=s("bee2"),a=s("262e"),o=s("2caf"),l=s("9ab4"),c=s("8d27"),u=s("dcc8"),d=s("0613"),h=function(e){Object(a["a"])(s,e);var t=Object(o["a"])(s);function s(){var e;return Object(i["a"])(this,s),e=t.apply(this,arguments),e.user=null,e.permission=null,e.routeUser="/",e}return Object(n["a"])(s,[{key:"autoCreateProfile",value:function(){var e=Object(r["a"])(regeneratorRuntime.mark((function e(t){return regeneratorRuntime.wrap((function(e){while(1)switch(e.prev=e.next){case 0:return e.abrupt("return",u["a"].postHttp("/api/profile/create/",t));case 1:case"end":return e.stop()}}),e)})));function t(t){return e.apply(this,arguments)}return t}()},{key:"loadUser",value:function(){var e=Object(r["a"])(regeneratorRuntime.mark((function e(){var t;return regeneratorRuntime.wrap((function(e){while(1)switch(e.prev=e.next){case 0:return e.next=2,u["a"].getHttp("/api/ita/v2/user/");case 2:t=e.sent,this.user=t,this.permission=t.is_staff,1==t.is_staff||0==t.is_staff?this.routeUser=t.is_staff?"/admin/":"/user/":this.routeUser="/";case 6:case"end":return e.stop()}}),e,this)})));function t(){return e.apply(this,arguments)}return t}()},{key:"getUser",value:function(){var e=Object(r["a"])(regeneratorRuntime.mark((function e(){return regeneratorRuntime.wrap((function(e){while(1)switch(e.prev=e.next){case 0:return e.next=2,u["a"].getHttp("/api/ita/v2/user/");case 2:return e.abrupt("return",e.sent);case 3:case"end":return e.stop()}}),e)})));function t(){return e.apply(this,arguments)}return t}()}]),s}(c["b"]);h=Object(l["c"])([Object(c["a"])({generateMutationSetters:!0})],h);var p=new h({store:d["a"],name:"User"})},"25a8":function(e,t,s){},"297c":function(e,t,s){"use strict";var r=s("2b0e"),i=s("37c6");t["a"]=r["default"].extend().extend({name:"loadable",props:{loading:{type:[Boolean,String],default:!1},loaderHeight:{type:[Number,String],default:2}},methods:{genProgress(){return!1===this.loading?null:this.$slots.progress||this.$createElement(i["a"],{props:{absolute:!0,color:!0===this.loading||""===this.loading?this.color||"primary":this.loading,height:this.loaderHeight,indeterminate:!0}})}}})},"2fa4":function(e,t,s){"use strict";s("20f6");var r=s("80d2");t["a"]=Object(r["g"])("spacer","div","v-spacer")},3408:function(e,t,s){},"37c6":function(e,t,s){"use strict";var r=s("8e36");t["a"]=r["a"]},"4de4":function(e,t,s){"use strict";var r=s("23e7"),i=s("b727").filter,n=s("1dde"),a=s("ae40"),o=n("filter"),l=a("filter");r({target:"Array",proto:!0,forced:!o||!l},{filter:function(e){return i(this,e,arguments.length>1?arguments[1]:void 0)}})},5607:function(e,t,s){"use strict";s("7435");var r=s("80d2");const i=80;function n(e,t){e.style.transform=t,e.style.webkitTransform=t}function a(e,t){e.style.opacity=t.toString()}function o(e){return"TouchEvent"===e.constructor.name}function l(e){return"KeyboardEvent"===e.constructor.name}const c=(e,t,s={})=>{let r=0,i=0;if(!l(e)){const s=t.getBoundingClientRect(),n=o(e)?e.touches[e.touches.length-1]:e;r=n.clientX-s.left,i=n.clientY-s.top}let n=0,a=.3;t._ripple&&t._ripple.circle?(a=.15,n=t.clientWidth/2,n=s.center?n:n+Math.sqrt((r-n)**2+(i-n)**2)/4):n=Math.sqrt(t.clientWidth**2+t.clientHeight**2)/2;const c=(t.clientWidth-2*n)/2+"px",u=(t.clientHeight-2*n)/2+"px",d=s.center?c:r-n+"px",h=s.center?u:i-n+"px";return{radius:n,scale:a,x:d,y:h,centerX:c,centerY:u}},u={show(e,t,s={}){if(!t._ripple||!t._ripple.enabled)return;const r=document.createElement("span"),i=document.createElement("span");r.appendChild(i),r.className="v-ripple__container",s.class&&(r.className+=" "+s.class);const{radius:o,scale:l,x:u,y:d,centerX:h,centerY:p}=c(e,t,s),f=2*o+"px";i.className="v-ripple__animation",i.style.width=f,i.style.height=f,t.appendChild(r);const v=window.getComputedStyle(t);v&&"static"===v.position&&(t.style.position="relative",t.dataset.previousPosition="static"),i.classList.add("v-ripple__animation--enter"),i.classList.add("v-ripple__animation--visible"),n(i,`translate(${u}, ${d}) scale3d(${l},${l},${l})`),a(i,0),i.dataset.activated=String(performance.now()),setTimeout(()=>{i.classList.remove("v-ripple__animation--enter"),i.classList.add("v-ripple__animation--in"),n(i,`translate(${h}, ${p}) scale3d(1,1,1)`),a(i,.25)},0)},hide(e){if(!e||!e._ripple||!e._ripple.enabled)return;const t=e.getElementsByClassName("v-ripple__animation");if(0===t.length)return;const s=t[t.length-1];if(s.dataset.isHiding)return;s.dataset.isHiding="true";const r=performance.now()-Number(s.dataset.activated),i=Math.max(250-r,0);setTimeout(()=>{s.classList.remove("v-ripple__animation--in"),s.classList.add("v-ripple__animation--out"),a(s,0),setTimeout(()=>{const t=e.getElementsByClassName("v-ripple__animation");1===t.length&&e.dataset.previousPosition&&(e.style.position=e.dataset.previousPosition,delete e.dataset.previousPosition),s.parentNode&&e.removeChild(s.parentNode)},300)},i)}};function d(e){return"undefined"===typeof e||!!e}function h(e){const t={},s=e.currentTarget;if(s&&s._ripple&&!s._ripple.touched){if(o(e))s._ripple.touched=!0,s._ripple.isTouch=!0;else if(s._ripple.isTouch)return;if(t.center=s._ripple.centered||l(e),s._ripple.class&&(t.class=s._ripple.class),o(e)){if(s._ripple.showTimerCommit)return;s._ripple.showTimerCommit=()=>{u.show(e,s,t)},s._ripple.showTimer=window.setTimeout(()=>{s&&s._ripple&&s._ripple.showTimerCommit&&(s._ripple.showTimerCommit(),s._ripple.showTimerCommit=null)},i)}else u.show(e,s,t)}}function p(e){const t=e.currentTarget;if(t&&t._ripple){if(window.clearTimeout(t._ripple.showTimer),"touchend"===e.type&&t._ripple.showTimerCommit)return t._ripple.showTimerCommit(),t._ripple.showTimerCommit=null,void(t._ripple.showTimer=setTimeout(()=>{p(e)}));window.setTimeout(()=>{t._ripple&&(t._ripple.touched=!1)}),u.hide(t)}}function f(e){const t=e.currentTarget;t&&t._ripple&&(t._ripple.showTimerCommit&&(t._ripple.showTimerCommit=null),window.clearTimeout(t._ripple.showTimer))}let v=!1;function m(e){v||e.keyCode!==r["r"].enter&&e.keyCode!==r["r"].space||(v=!0,h(e))}function g(e){v=!1,p(e)}function b(e,t,s){const r=d(t.value);r||u.hide(e),e._ripple=e._ripple||{},e._ripple.enabled=r;const i=t.value||{};i.center&&(e._ripple.centered=!0),i.class&&(e._ripple.class=t.value.class),i.circle&&(e._ripple.circle=i.circle),r&&!s?(e.addEventListener("touchstart",h,{passive:!0}),e.addEventListener("touchend",p,{passive:!0}),e.addEventListener("touchmove",f,{passive:!0}),e.addEventListener("touchcancel",p),e.addEventListener("mousedown",h),e.addEventListener("mouseup",p),e.addEventListener("mouseleave",p),e.addEventListener("keydown",m),e.addEventListener("keyup",g),e.addEventListener("dragstart",p,{passive:!0})):!r&&s&&y(e)}function y(e){e.removeEventListener("mousedown",h),e.removeEventListener("touchstart",h),e.removeEventListener("touchend",p),e.removeEventListener("touchmove",f),e.removeEventListener("touchcancel",p),e.removeEventListener("mouseup",p),e.removeEventListener("mouseleave",p),e.removeEventListener("keydown",m),e.removeEventListener("keyup",g),e.removeEventListener("dragstart",p)}function _(e,t,s){b(e,t,!1)}function x(e){delete e._ripple,y(e)}function w(e,t){if(t.value===t.oldValue)return;const s=d(t.oldValue);b(e,t,s)}const C={bind:_,unbind:x,update:w};t["a"]=C},"615b":function(e,t,s){},"6ece":function(e,t,s){},7435:function(e,t,s){},"7e2b":function(e,t,s){"use strict";var r=s("2b0e");function i(e){return function(t,s){for(const r in s)Object.prototype.hasOwnProperty.call(t,r)||this.$delete(this.$data[e],r);for(const r in t)this.$set(this.$data[e],r,t[r])}}t["a"]=r["default"].extend({data:()=>({attrs$:{},listeners$:{}}),created(){this.$watch("$attrs",i("attrs$"),{immediate:!0}),this.$watch("$listeners",i("listeners$"),{immediate:!0})}})},8212:function(e,t,s){"use strict";s("3408");var r=s("a9ad"),i=s("24b2"),n=s("a236"),a=s("80d2"),o=s("58df");t["a"]=Object(o["a"])(r["a"],i["a"],n["a"]).extend({name:"v-avatar",props:{left:Boolean,right:Boolean,size:{type:[Number,String],default:48}},computed:{classes(){return{"v-avatar--left":this.left,"v-avatar--right":this.right,...this.roundedClasses}},styles(){return{height:Object(a["f"])(this.size),minWidth:Object(a["f"])(this.size),width:Object(a["f"])(this.size),...this.measurableStyles}}},render(e){const t={staticClass:"v-avatar",class:this.classes,style:this.styles,on:this.$listeners};return e("div",this.setBackgroundColor(this.color,t),this.$slots.default)}})},8418:function(e,t,s){"use strict";var r=s("c04e"),i=s("9bf2"),n=s("5c6c");e.exports=function(e,t,s){var a=r(t);a in e?i.f(e,a,n(0,s)):e[a]=s}},"8dd9":function(e,t,s){"use strict";s("25a8");var r=s("7e2b"),i=s("a9ad"),n=s("2b0e"),a=n["default"].extend({name:"elevatable",props:{elevation:[Number,String]},computed:{computedElevation(){return this.elevation},elevationClasses(){const e=this.computedElevation;return null==e||isNaN(parseInt(e))?{}:{["elevation-"+this.elevation]:!0}}}}),o=s("24b2"),l=s("a236"),c=s("7560"),u=s("58df");t["a"]=Object(u["a"])(r["a"],i["a"],a,o["a"],l["a"],c["a"]).extend({name:"v-sheet",props:{outlined:Boolean,shaped:Boolean,tag:{type:String,default:"div"}},computed:{classes(){return{"v-sheet":!0,"v-sheet--outlined":this.outlined,"v-sheet--shaped":this.shaped,...this.themeClasses,...this.elevationClasses,...this.roundedClasses}},styles(){return this.measurableStyles}},render(e){const t={class:this.classes,style:this.styles,on:this.listeners$};return e(this.tag,this.setBackgroundColor(this.color,t),this.$slots.default)}})},"8e36":function(e,t,s){"use strict";s("6ece");var r=s("0789"),i=s("a9ad"),n=s("fe6c"),a=s("a452"),o=s("7560"),l=s("80d2"),c=s("58df");const u=Object(c["a"])(i["a"],Object(n["b"])(["absolute","fixed","top","bottom"]),a["a"],o["a"]);t["a"]=u.extend({name:"v-progress-linear",props:{active:{type:Boolean,default:!0},backgroundColor:{type:String,default:null},backgroundOpacity:{type:[Number,String],default:null},bufferValue:{type:[Number,String],default:100},color:{type:String,default:"primary"},height:{type:[Number,String],default:4},indeterminate:Boolean,query:Boolean,reverse:Boolean,rounded:Boolean,stream:Boolean,striped:Boolean,value:{type:[Number,String],default:0}},data(){return{internalLazyValue:this.value||0}},computed:{__cachedBackground(){return this.$createElement("div",this.setBackgroundColor(this.backgroundColor||this.color,{staticClass:"v-progress-linear__background",style:this.backgroundStyle}))},__cachedBar(){return this.$createElement(this.computedTransition,[this.__cachedBarType])},__cachedBarType(){return this.indeterminate?this.__cachedIndeterminate:this.__cachedDeterminate},__cachedBuffer(){return this.$createElement("div",{staticClass:"v-progress-linear__buffer",style:this.styles})},__cachedDeterminate(){return this.$createElement("div",this.setBackgroundColor(this.color,{staticClass:"v-progress-linear__determinate",style:{width:Object(l["f"])(this.normalizedValue,"%")}}))},__cachedIndeterminate(){return this.$createElement("div",{staticClass:"v-progress-linear__indeterminate",class:{"v-progress-linear__indeterminate--active":this.active}},[this.genProgressBar("long"),this.genProgressBar("short")])},__cachedStream(){return this.stream?this.$createElement("div",this.setTextColor(this.color,{staticClass:"v-progress-linear__stream",style:{width:Object(l["f"])(100-this.normalizedBuffer,"%")}})):null},backgroundStyle(){const e=null==this.backgroundOpacity?this.backgroundColor?1:.3:parseFloat(this.backgroundOpacity);return{opacity:e,[this.isReversed?"right":"left"]:Object(l["f"])(this.normalizedValue,"%"),width:Object(l["f"])(this.normalizedBuffer-this.normalizedValue,"%")}},classes(){return{"v-progress-linear--absolute":this.absolute,"v-progress-linear--fixed":this.fixed,"v-progress-linear--query":this.query,"v-progress-linear--reactive":this.reactive,"v-progress-linear--reverse":this.isReversed,"v-progress-linear--rounded":this.rounded,"v-progress-linear--striped":this.striped,...this.themeClasses}},computedTransition(){return this.indeterminate?r["c"]:r["d"]},isReversed(){return this.$vuetify.rtl!==this.reverse},normalizedBuffer(){return this.normalize(this.bufferValue)},normalizedValue(){return this.normalize(this.internalLazyValue)},reactive(){return Boolean(this.$listeners.change)},styles(){const e={};return this.active||(e.height=0),this.indeterminate||100===parseFloat(this.normalizedBuffer)||(e.width=Object(l["f"])(this.normalizedBuffer,"%")),e}},methods:{genContent(){const e=Object(l["n"])(this,"default",{value:this.internalLazyValue});return e?this.$createElement("div",{staticClass:"v-progress-linear__content"},e):null},genListeners(){const e=this.$listeners;return this.reactive&&(e.click=this.onClick),e},genProgressBar(e){return this.$createElement("div",this.setBackgroundColor(this.color,{staticClass:"v-progress-linear__indeterminate",class:{[e]:!0}}))},onClick(e){if(!this.reactive)return;const{width:t}=this.$el.getBoundingClientRect();this.internalValue=e.offsetX/t*100},normalize(e){return e<0?0:e>100?100:parseFloat(e)}},render(e){const t={staticClass:"v-progress-linear",attrs:{role:"progressbar","aria-valuemin":0,"aria-valuemax":this.normalizedBuffer,"aria-valuenow":this.indeterminate?void 0:this.normalizedValue},class:this.classes,style:{bottom:this.bottom?0:void 0,height:this.active?Object(l["f"])(this.height):0,top:this.top?0:void 0},on:this.genListeners()};return e("div",t,[this.__cachedStream,this.__cachedBackground,this.__cachedBuffer,this.__cachedBar,this.genContent()])}})},9187:function(e,t,s){"use strict";s.r(t);var r=function(){var e=this,t=e.$createElement,s=e._self._c||t;return s("div",{staticClass:"relative md:pt-32 pb-32 pt-12  "},[s("div",{staticClass:"relative  flex flex-col min-w-0 break-words w-full mb-6  "},[s("div",{staticClass:"rounded-t mb-0 px-4 py-3 border-0 "},[e._m(0),s("div",{staticClass:"w-full "},[s("div",{staticClass:"flex flex-wrap justify-center"},e._l(e.assessment,(function(t,r){return s("button",{key:r,class:"bg-green-600 p-2 rounded shadow-lg m-1 text-white",on:{click:function(s){return e.getDataIssue(t.id)}}},[e._v(e._s(t.name))])})),0)]),s("div",[e.suggestion?s("v-card",{staticClass:"m-2"},[s("v-card-title",{attrs:{"primary-title":""}},[s("h2",{staticClass:"text-sm font-bold "},[e._v("ข้อเสนอแนะ")])]),s("v-card-text",e._l(e.suggestion,(function(t,r){return s("div",{key:r,staticClass:"flex p-2 "},[e._v(" "+e._s(t.suggestion)+" ")])})),0)],1):s("div",e._l(e.data,(function(t,r){return s("v-card",{key:r,staticClass:"m-2"},[s("v-card-title",{attrs:{"primary-title":""}},[s("h2",{staticClass:"text-sm font-bold"},[s("v-avatar",{staticClass:"bg-teal-500 text-white",attrs:{size:"36"}},[e._v(" i"+e._s(t.value[0].issue.order)+" ")]),e._v(" "+e._s(t.value[0].issue.name)+" ")],1)]),s("v-card-text",e._l(e.getValue(t.value),(function(t,r){return s("div",{staticClass:"flex  p-2 ",attrs:{index:r}},[e._v(" "+e._s(t.name)+" "),s("v-spacer"),e._v(" "+e._s(t.notting)+" / "+e._s(t.low)+" / "+e._s(t.many)+" /"+e._s(t.very)+" / "+e._s(t.have)+" / "+e._s(t.nohave)+" ")],1)})),0)],1)})),1)],1)])])])},i=[function(){var e=this,t=e.$createElement,s=e._self._c||t;return s("div",{staticClass:"relative w-full mt-4 mb-4 max-w-full flex-grow flex-1 px-2 py-2"},[s("h3",{staticClass:"  text-2xl text-gray-800"},[s("span",{staticClass:"em em-briefcase text-2xl",attrs:{"aria-role":"presentation","aria-label":""}}),e._v(" ข้อมูลของหน่วยงาน ")])])}],n=(s("99af"),s("4de4"),s("d81d"),s("96cf"),s("1da1")),a=s("d4ec"),o=s("bee2"),l=s("262e"),c=s("2caf"),u=s("9ab4"),d=s("60a3"),h=s("b14a"),p=s("dcc8"),f=s("21d1"),v=s("2ef0"),m=s.n(v),g=function(e){Object(l["a"])(s,e);var t=Object(c["a"])(s);function s(){var e;return Object(a["a"])(this,s),e=t.apply(this,arguments),e.assessment=null,e.raw=null,e.suggestion=null,e.data=null,e.user={},e.years=null,e.response=!1,e}return Object(o["a"])(s,[{key:"getValue",value:function(e){for(var t=m()(e).groupBy("issueDetail_pk").map((function(e,t){return{type:t,val:e}})).value(),s=[],r=0;r<t.length;r++)console.log(r,"----------------------------"),s.push({name:t[r].val[0].issueDetail.sub_name,notting:this.sumChoice(t[r].val,"น้อยที่สุดหรือไม่มีเลย"),low:this.sumChoice(t[r].val,"น้อย"),very:this.sumChoice(t[r].val,"มาก"),many:this.sumChoice(t[r].val,"มากที่สุด"),have:this.sumChoice(t[r].val,"มี"),nohave:this.sumChoice(t[r].val,"ไม่มี")});return s}},{key:"sumChoice",value:function(e,t){var s=m.a.filter(e,{value_by:t});return console.log(s,e.length,t),s.length}},{key:"created",value:function(){var e=Object(n["a"])(regeneratorRuntime.mark((function e(){return regeneratorRuntime.wrap((function(e){while(1)switch(e.prev=e.next){case 0:return e.next=2,f["a"].getUser();case 2:return this.user=e.sent,e.next=5,p["a"].getHttp("/api/iit/v2/year/".concat(this.$route.query.year,"/"));case 5:return this.years=e.sent,e.next=8,p["a"].getHttp("/api/iit/v2/assessmentissues/?&year=".concat(this.years.id));case 8:return this.assessment=e.sent,e.next=11,this.getDataIssue(this.assessment[0].id);case 11:this.response=!0;case 12:case"end":return e.stop()}}),e,this)})));function t(){return e.apply(this,arguments)}return t}()},{key:"getDataIssue",value:function(){var e=Object(n["a"])(regeneratorRuntime.mark((function e(t){return regeneratorRuntime.wrap((function(e){while(1)switch(e.prev=e.next){case 0:return e.next=2,p["a"].getHttp("/api/iit/v2/answerissue-report/?agency=".concat(this.user.ext_link.agency,"&assessmentIssues=").concat(t));case 2:if(this.raw=e.sent,!(this.raw.length>0)){e.next=9;break}return e.next=6,this.convertData();case 6:this.suggestion=null,e.next=12;break;case 9:return e.next=11,p["a"].getHttp("/api/iit/v2/answersuggestion/?agency=".concat(this.user.ext_link.agency,"&year=").concat(this.years.id));case 11:this.suggestion=e.sent;case 12:case"end":return e.stop()}}),e,this)})));function t(t){return e.apply(this,arguments)}return t}()},{key:"convertData",value:function(){var e=Object(n["a"])(regeneratorRuntime.mark((function e(){var t;return regeneratorRuntime.wrap((function(e){while(1)switch(e.prev=e.next){case 0:return t=this.raw,e.next=3,m.a.chain(t).groupBy("issue_pk").map((function(e,t){return{group:t,value:e}})).value();case 3:t=e.sent,this.data=t;case 5:case"end":return e.stop()}}),e,this)})));function t(){return e.apply(this,arguments)}return t}()},{key:"convertDataAssign",value:function(){var e=Object(n["a"])(regeneratorRuntime.mark((function e(){var t;return regeneratorRuntime.wrap((function(e){while(1)switch(e.prev=e.next){case 0:return t=this.raw,e.next=3,m.a.chain(t).groupBy("issue_pk").map((function(e,t){return{group:t,value:e}})).value();case 3:t=e.sent,this.data=t;case 5:case"end":return e.stop()}}),e,this)})));function t(){return e.apply(this,arguments)}return t}()}]),s}(d["b"]);g=Object(u["c"])([Object(d["a"])({components:{CardStats:h["a"]}})],g);var b=g,y=b,_=(s("db07"),s("2877")),x=s("6544"),w=s.n(x),C=s("8212"),k=s("b0af"),O=s("99d9"),B=s("2fa4"),j=Object(_["a"])(y,r,i,!1,null,null,null);t["default"]=j.exports;w()(j,{VAvatar:C["a"],VCard:k["a"],VCardText:O["b"],VCardTitle:O["c"],VSpacer:B["a"]})},"99af":function(e,t,s){"use strict";var r=s("23e7"),i=s("d039"),n=s("e8b5"),a=s("861d"),o=s("7b0b"),l=s("50c4"),c=s("8418"),u=s("65f0"),d=s("1dde"),h=s("b622"),p=s("2d00"),f=h("isConcatSpreadable"),v=9007199254740991,m="Maximum allowed index exceeded",g=p>=51||!i((function(){var e=[];return e[f]=!1,e.concat()[0]!==e})),b=d("concat"),y=function(e){if(!a(e))return!1;var t=e[f];return void 0!==t?!!t:n(e)},_=!g||!b;r({target:"Array",proto:!0,forced:_},{concat:function(e){var t,s,r,i,n,a=o(this),d=u(a,0),h=0;for(t=-1,r=arguments.length;t<r;t++)if(n=-1===t?a:arguments[t],y(n)){if(i=l(n.length),h+i>v)throw TypeError(m);for(s=0;s<i;s++,h++)s in n&&c(d,h,n[s])}else{if(h>=v)throw TypeError(m);c(d,h++,n)}return d.length=h,d}})},"99d9":function(e,t,s){"use strict";s.d(t,"a",(function(){return n})),s.d(t,"b",(function(){return o})),s.d(t,"c",(function(){return l}));var r=s("b0af"),i=s("80d2");const n=Object(i["g"])("v-card__actions"),a=Object(i["g"])("v-card__subtitle"),o=Object(i["g"])("v-card__text"),l=Object(i["g"])("v-card__title");r["a"]},a236:function(e,t,s){"use strict";var r=s("2b0e");t["a"]=r["default"].extend({name:"roundable",props:{rounded:[Boolean,String],tile:Boolean},computed:{roundedClasses(){const e=[],t="string"===typeof this.rounded?String(this.rounded):!0===this.rounded;if(this.tile)e.push("rounded-0");else if("string"===typeof t){const s=t.split(" ");for(const t of s)e.push("rounded-"+t)}else t&&e.push("rounded");return e.length>0?{[e.join(" ")]:!0}:{}}}})},a452:function(e,t,s){"use strict";var r=s("2b0e");function i(e="value",t="change"){return r["default"].extend({name:"proxyable",model:{prop:e,event:t},props:{[e]:{required:!1}},data(){return{internalLazyValue:this[e]}},computed:{internalValue:{get(){return this.internalLazyValue},set(e){e!==this.internalLazyValue&&(this.internalLazyValue=e,this.$emit(t,e))}}},watch:{[e](e){this.internalLazyValue=e}}})}const n=i();t["a"]=n},a640:function(e,t,s){"use strict";var r=s("d039");e.exports=function(e,t){var s=[][e];return!!s&&r((function(){s.call(null,t||function(){throw 1},1)}))}},a9ad:function(e,t,s){"use strict";var r=s("2b0e"),i=s("d9bd"),n=s("7bc6");t["a"]=r["default"].extend({name:"colorable",props:{color:String},methods:{setBackgroundColor(e,t={}){return"string"===typeof t.style?(Object(i["b"])("style must be an object",this),t):"string"===typeof t.class?(Object(i["b"])("class must be an object",this),t):(Object(n["d"])(e)?t.style={...t.style,"background-color":""+e,"border-color":""+e}:e&&(t.class={...t.class,[e]:!0}),t)},setTextColor(e,t={}){if("string"===typeof t.style)return Object(i["b"])("style must be an object",this),t;if("string"===typeof t.class)return Object(i["b"])("class must be an object",this),t;if(Object(n["d"])(e))t.style={...t.style,color:""+e,"caret-color":""+e};else if(e){const[s,r]=e.toString().trim().split(" ",2);t.class={...t.class,[s+"--text"]:!0},r&&(t.class["text--"+r]=!0)}return t}}})},b0af:function(e,t,s){"use strict";s("615b");var r=s("10d2"),i=s("297c"),n=s("1c87"),a=s("58df");t["a"]=Object(a["a"])(i["a"],n["a"],r["a"]).extend({name:"v-card",props:{flat:Boolean,hover:Boolean,img:String,link:Boolean,loaderHeight:{type:[Number,String],default:4},raised:Boolean},computed:{classes(){return{"v-card":!0,...n["a"].options.computed.classes.call(this),"v-card--flat":this.flat,"v-card--hover":this.hover,"v-card--link":this.isClickable,"v-card--loading":this.loading,"v-card--disabled":this.disabled,"v-card--raised":this.raised,...r["a"].options.computed.classes.call(this)}},styles(){const e={...r["a"].options.computed.styles.call(this)};return this.img&&(e.background=`url("${this.img}") center center / cover no-repeat`),e}},methods:{genProgress(){const e=i["a"].options.methods.genProgress.call(this);return e?this.$createElement("div",{staticClass:"v-card__progress",key:"progress"},[e]):null}},render(e){const{tag:t,data:s}=this.generateRouteLink();return s.style=this.styles,this.isClickable&&(s.attrs=s.attrs||{},s.attrs.tabindex=0),e(t,this.setBackgroundColor(this.color,s),[this.genProgress(),this.$slots.default])}})},b14a:function(e,t,s){"use strict";var r=function(){var e=this,t=e.$createElement,s=e._self._c||t;return s("div",{staticClass:"relative flex flex-col min-w-0 break-words bg-white rounded-lg  shadow-xl mb-6 xl:mb-0 shadow-lg border-b-4 border-green-600"},[s("div",{staticClass:"flex-auto p-4"},[s("div",{staticClass:"flex flex-wrap"},[s("div",{staticClass:"relative w-full pr-4 max-w-full flex-grow flex-1"},[s("span",{staticClass:"font-semibold text-xl text-gray-800"},[e._v(" "+e._s(e.statTitle)+" ")]),s("h5",{staticClass:"text-gray-500 uppercase font-bold text-xs"},[e._v(" "+e._s(e.statSubtitle)+" ")]),s("div",{},[s("button",{staticClass:"mt-2 text-green-600 font-bold text-tiny",on:{click:function(t){return e.$router.push(e.statRoute)}}},[e._v("ดูรายระเอียด")])])]),s("div",{staticClass:"relative w-auto pl-4 flex-initial"},[s("div",{staticClass:"text-white p-3 text-center inline-flex items-center justify-center w-12 h-12 shadow-lg rounded-full text-xl",class:[e.statIconColor]},[s("i",{class:[e.statIconName]})])])])])])},i=[],n=(s("c975"),{name:"card-stats",props:{statSubtitle:{type:String,default:"Traffic"},statArrow:{default:"up",validator:function(e){return-1!==["up","down"].indexOf(e)}},statPercent:{type:String,default:"3.48"},statPercentColor:{type:String,default:"text-green-500"},statTitle:{type:String,default:"350,897"},statDescripiron:{type:String,default:"Since last month"},statIconName:{type:String,default:"far fa-chart-bar"},statIconColor:{type:String,default:"bg-red-500"},statRoute:{type:String,default:"#"}}}),a=n,o=s("2877"),l=Object(o["a"])(a,r,i,!1,null,null,null);t["a"]=l.exports},c975:function(e,t,s){"use strict";var r=s("23e7"),i=s("4d64").indexOf,n=s("a640"),a=s("ae40"),o=[].indexOf,l=!!o&&1/[1].indexOf(1,-0)<0,c=n("indexOf"),u=a("indexOf",{ACCESSORS:!0,1:0});r({target:"Array",proto:!0,forced:l||!c||!u},{indexOf:function(e){return l?o.apply(this,arguments)||0:i(this,e,arguments.length>1?arguments[1]:void 0)}})},db07:function(e,t,s){"use strict";s("db94")},db94:function(e,t,s){},fe6c:function(e,t,s){"use strict";s.d(t,"b",(function(){return a}));var r=s("2b0e"),i=s("80d2");const n={absolute:Boolean,bottom:Boolean,fixed:Boolean,left:Boolean,right:Boolean,top:Boolean};function a(e=[]){return r["default"].extend({name:"positionable",props:e.length?Object(i["j"])(n,e):n})}t["a"]=a()}}]);
//# sourceMappingURL=chunk-6a91d8ff.2cbf738b.js.map