(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-50fe24c6"],{"21d1":function(t,e,r){"use strict";r.d(e,"a",(function(){return d}));r("96cf");var a=r("1da1"),s=r("d4ec"),n=r("bee2"),i=r("262e"),l=r("2caf"),c=r("9ab4"),u=r("8d27"),o=r("dcc8"),f=r("0613"),p=function(t){Object(i["a"])(r,t);var e=Object(l["a"])(r);function r(){var t;return Object(s["a"])(this,r),t=e.apply(this,arguments),t.user=null,t.permission=null,t.routeUser="/",t}return Object(n["a"])(r,[{key:"autoCreateProfile",value:function(){var t=Object(a["a"])(regeneratorRuntime.mark((function t(e){return regeneratorRuntime.wrap((function(t){while(1)switch(t.prev=t.next){case 0:return t.abrupt("return",o["a"].postHttp("/api/profile/create/",e));case 1:case"end":return t.stop()}}),t)})));function e(e){return t.apply(this,arguments)}return e}()},{key:"loadUser",value:function(){var t=Object(a["a"])(regeneratorRuntime.mark((function t(){var e;return regeneratorRuntime.wrap((function(t){while(1)switch(t.prev=t.next){case 0:return t.next=2,o["a"].getHttp("/api/ita/v2/user/");case 2:e=t.sent,this.user=e,this.permission=e.is_staff,1==e.is_staff||0==e.is_staff?this.routeUser=e.is_staff?"/admin/":"/user/":this.routeUser="/";case 6:case"end":return t.stop()}}),t,this)})));function e(){return t.apply(this,arguments)}return e}()},{key:"getUser",value:function(){var t=Object(a["a"])(regeneratorRuntime.mark((function t(){return regeneratorRuntime.wrap((function(t){while(1)switch(t.prev=t.next){case 0:return t.next=2,o["a"].getHttp("/api/ita/v2/user/");case 2:return t.abrupt("return",t.sent);case 3:case"end":return t.stop()}}),t)})));function e(){return t.apply(this,arguments)}return e}()}]),r}(u["b"]);p=Object(c["c"])([Object(u["a"])({generateMutationSetters:!0})],p);var d=new p({store:f["a"],name:"User"})},b14a:function(t,e,r){"use strict";var a=function(){var t=this,e=t.$createElement,r=t._self._c||e;return r("div",{staticClass:"relative flex flex-col min-w-0 break-words bg-white rounded-lg  shadow-xl mb-6 xl:mb-0 shadow-lg border-b-4 border-green-600"},[r("div",{staticClass:"flex-auto p-4"},[r("div",{staticClass:"flex flex-wrap"},[r("div",{staticClass:"relative w-full pr-4 max-w-full flex-grow flex-1"},[r("span",{staticClass:"font-semibold text-xl text-gray-800"},[t._v(" "+t._s(t.statTitle)+" ")]),r("h5",{staticClass:"text-gray-500 uppercase font-bold text-xs"},[t._v(" "+t._s(t.statSubtitle)+" ")]),r("div",{},[r("button",{staticClass:"mt-2 text-green-600 font-bold text-tiny",on:{click:function(e){return t.$router.push(t.statRoute)}}},[t._v("ดูรายระเอียด")])])]),r("div",{staticClass:"relative w-auto pl-4 flex-initial"},[r("div",{staticClass:"text-white p-3 text-center inline-flex items-center justify-center w-12 h-12 shadow-lg rounded-full text-xl",class:[t.statIconColor]},[r("i",{class:[t.statIconName]})])])])])])},s=[],n=(r("c975"),{name:"card-stats",props:{statSubtitle:{type:String,default:"Traffic"},statArrow:{default:"up",validator:function(t){return-1!==["up","down"].indexOf(t)}},statPercent:{type:String,default:"3.48"},statPercentColor:{type:String,default:"text-green-500"},statTitle:{type:String,default:"350,897"},statDescripiron:{type:String,default:"Since last month"},statIconName:{type:String,default:"far fa-chart-bar"},statIconColor:{type:String,default:"bg-red-500"},statRoute:{type:String,default:"#"}}}),i=n,l=r("2877"),c=Object(l["a"])(i,a,s,!1,null,null,null);e["a"]=c.exports},f717:function(t,e,r){"use strict";r.r(e);var a=function(){var t=this,e=t.$createElement,r=t._self._c||e;return r("div",{staticClass:"relative md:pt-32 pb-32 pt-12 ",staticStyle:{"z-index":"1"}},[r("div",{staticClass:"relative  flex flex-col min-w-0 break-words w-full mb-6  "},[r("div",{staticClass:"rounded-t mb-0 px-4 py-3 border-0 "},[t._m(0),t.response?r("div",{staticClass:"relative w-full mt-4 mb-4 max-w-full flex-grow flex-1 px-2 py-2"},[r("div",{staticClass:"flex flex-wrap"},t._l(t.years,(function(e,a){return r("div",{key:a,staticClass:"w-full md:w-3/12 p-2"},[r("card-stats",{attrs:{statRoute:"/admin/paper?year="+e.id+"&id="+t.$route.query.id,statSubtitle:"การให้ข้อมูล ( "+e.result+" / "+e.rate+" )",statTitle:e.year,statArrow:"up",statPercent:"12",statPercentColor:"text-green-500",statDescripiron:"Since last month",statIconName:"mdi mdi-file-document-multiple",statIconColor:"bg-green-500"}})],1)})),0)]):t._e()])]),r("br"),r("br"),r("br"),r("br"),t._v(" "),r("br"),t._v(" "),r("br"),t._v(" "),r("br"),r("br"),r("br"),r("br"),r("br"),t._v(" "),r("br"),t._v(" "),r("br"),t._v(" "),r("br"),r("br")])},s=[function(){var t=this,e=t.$createElement,r=t._self._c||e;return r("div",{staticClass:"relative w-full mt-4 mb-4 max-w-full flex-grow flex-1 px-2 py-2"},[r("h3",{staticClass:"font-semibold text-3xl text-gray-800"},[r("i",{staticClass:"em em-lower_left_ballpoint_pen",attrs:{"aria-role":"presentation","aria-label":""}}),t._v(" ข้อมูลของหน่วยงาน ")]),r("hr",{staticClass:"border-gray-600 border-2 mt-2"})])}],n=(r("99af"),r("96cf"),r("1da1")),i=r("d4ec"),l=r("bee2"),c=r("262e"),u=r("2caf"),o=r("9ab4"),f=r("60a3"),p=r("b14a"),d=r("dcc8"),b=r("21d1"),v=function(t){Object(c["a"])(r,t);var e=Object(u["a"])(r);function r(){var t;return Object(i["a"])(this,r),t=e.apply(this,arguments),t.user={},t.years=[],t.response=!1,t}return Object(l["a"])(r,[{key:"created",value:function(){var t=Object(n["a"])(regeneratorRuntime.mark((function t(){var e,r,a;return regeneratorRuntime.wrap((function(t){while(1)switch(t.prev=t.next){case 0:return t.next=2,b["a"].getUser();case 2:return this.user=t.sent,t.next=5,d["a"].getHttp("/api/ita/v2/year/");case 5:this.years=t.sent,e=0;case 7:if(!(e<this.years.length)){t.next=19;break}return t.next=10,d["a"].getHttp("/api/ita/v1/rateresult/?rate__year=".concat(this.years[e].id,"&agency=").concat(this.$route.query.id));case 10:return r=t.sent,t.next=13,d["a"].getHttp("/api/ita/v2/rate/".concat(this.years[e].id,"/"));case 13:a=t.sent,this.years[e].result=r.length,this.years[e].rate=a.length;case 16:e++,t.next=7;break;case 19:this.response=!0,console.log(this.years);case 21:case"end":return t.stop()}}),t,this)})));function e(){return t.apply(this,arguments)}return e}()}]),r}(f["b"]);v=Object(o["c"])([Object(f["a"])({components:{CardStats:p["a"]}})],v);var x=v,m=x,h=r("2877"),w=Object(h["a"])(m,a,s,!1,null,null,null);e["default"]=w.exports}}]);
//# sourceMappingURL=chunk-50fe24c6.41050a49.js.map