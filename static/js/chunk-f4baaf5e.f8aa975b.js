(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-f4baaf5e"],{"1b1c":function(t,e,a){"use strict";var s=function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("div",{staticClass:"relative bg-green-600 md:pt-32 pb-32 pt-12"},[a("div",{staticClass:"px-4 md:px-10 mx-auto w-full"},[a("div",[a("div",{staticClass:"flex flex-wrap"},[a("div",{staticClass:"w-full lg:w-6/12 xl:w-3/12 px-4"},[a("card-stats",{attrs:{statSubtitle:"TRAFFIC",statTitle:"350,897",statArrow:"up",statPercent:"3.48",statPercentColor:"text-green-500",statDescripiron:"Since last month",statIconName:"far fa-chart-bar",statIconColor:"bg-red-500"}})],1),a("div",{staticClass:"w-full lg:w-6/12 xl:w-3/12 px-4"},[a("card-stats",{attrs:{statSubtitle:"NEW USERS",statTitle:"2,356",statArrow:"down",statPercent:"3.48",statPercentColor:"text-red-500",statDescripiron:"Since last week",statIconName:"fas fa-chart-pie",statIconColor:"bg-orange-500"}})],1),a("div",{staticClass:"w-full lg:w-6/12 xl:w-3/12 px-4"},[a("card-stats",{attrs:{statSubtitle:"SALES",statTitle:"924",statArrow:"down",statPercent:"1.10",statPercentColor:"text-orange-500",statDescripiron:"Since yesterday",statIconName:"fas fa-users",statIconColor:"bg-pink-500"}})],1),a("div",{staticClass:"w-full lg:w-6/12 xl:w-3/12 px-4"},[a("card-stats",{attrs:{statSubtitle:"PERFORMANCE",statTitle:"49,65%",statArrow:"up",statPercent:"12",statPercentColor:"text-green-500",statDescripiron:"Since last month",statIconName:"fas fa-percent",statIconColor:"bg-green-500"}})],1)])])])])},r=[],l=function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("div",{staticClass:"relative flex flex-col min-w-0 break-words bg-white rounded mb-6 xl:mb-0 shadow-lg"},[a("div",{staticClass:"flex-auto p-4"},[a("div",{staticClass:"flex flex-wrap"},[a("div",{staticClass:"relative w-full pr-4 max-w-full flex-grow flex-1"},[a("h5",{staticClass:"text-gray-500 uppercase font-bold text-xs"},[t._v(" "+t._s(t.statSubtitle)+" ")]),a("span",{staticClass:"font-semibold text-xl text-gray-800"},[t._v(" "+t._s(t.statTitle)+" ")])]),a("div",{staticClass:"relative w-auto pl-4 flex-initial"},[a("div",{staticClass:"text-white p-3 text-center inline-flex items-center justify-center w-12 h-12 shadow-lg rounded-full",class:[t.statIconColor]},[a("i",{class:[t.statIconName]})])])])])])},o=[],n=(a("c975"),{name:"card-stats",props:{statSubtitle:{type:String,default:"Traffic"},statTitle:{type:String,default:"350,897"},statArrow:{default:"up",validator:function(t){return-1!==["up","down"].indexOf(t)}},statPercent:{type:String,default:"3.48"},statPercentColor:{type:String,default:"text-green-500"},statDescripiron:{type:String,default:"Since last month"},statIconName:{type:String,default:"far fa-chart-bar"},statIconColor:{type:String,default:"bg-red-500"}}}),i=n,c=a("2877"),d=Object(c["a"])(i,l,o,!1,null,null,null),p=d.exports,u={components:{CardStats:p}},f=u,m=Object(c["a"])(f,s,r,!1,null,null,null);e["a"]=m.exports},"227a":function(t,e,a){"use strict";var s=function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("div",[a("a",{ref:"btnDropdownRef",staticClass:"text-gray-600 block py-1 px-3",on:{click:function(e){return t.toggleDropdown(e)}}},[a("i",{staticClass:"fas fa-bell"})]),a("div",{ref:"popoverDropdownRef",staticClass:"bg-white text-base z-50 float-left py-2 list-none text-left rounded shadow-lg min-w-48",class:{hidden:!t.dropdownPopoverShow,block:t.dropdownPopoverShow}},[a("a",{staticClass:"text-sm py-2 px-4 font-normal block w-full whitespace-no-wrap bg-transparent text-gray-800",attrs:{href:"javascript:void(0);"}},[t._v(" Action ")]),a("a",{staticClass:"text-sm py-2 px-4 font-normal block w-full whitespace-no-wrap bg-transparent text-gray-800",attrs:{href:"javascript:void(0);"}},[t._v(" Another action ")]),a("a",{staticClass:"text-sm py-2 px-4 font-normal block w-full whitespace-no-wrap bg-transparent text-gray-800",attrs:{href:"javascript:void(0);"}},[t._v(" Something else here ")]),a("div",{staticClass:"h-0 my-2 border border-solid border-gray-200"}),a("a",{staticClass:"text-sm py-2 px-4 font-normal block w-full whitespace-no-wrap bg-transparent text-gray-800",attrs:{href:"javascript:void(0);"}},[t._v(" Seprated link ")])])])},r=[],l=a("39c3"),o={data:function(){return{dropdownPopoverShow:!1}},methods:{toggleDropdown:function(t){t.preventDefault(),this.dropdownPopoverShow?this.dropdownPopoverShow=!1:(this.dropdownPopoverShow=!0,Object(l["a"])(this.$refs.btnDropdownRef,this.$refs.popoverDropdownRef,{placement:"bottom-start"}))}}},n=o,i=a("2877"),c=Object(i["a"])(n,s,r,!1,null,null,null);e["a"]=c.exports},"59ac":function(t,e,a){"use strict";var s=function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("footer",{staticClass:"pb-6",class:[t.absolute?"absolute w-full bottom-0 ":"relative"]},[t._m(0)])},r=[function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("div",{staticClass:"container mx-auto px-4"},[a("hr",{staticClass:"mb-6 border-b-1 border-gray-400"}),a("div",{staticClass:"flex flex-wrap items-center md:justify-between justify-center"},[a("div",{staticClass:"w-full md:w-4/12 px-4"},[a("div",{staticClass:"text-sm text-gray-400 font-semibold py-1 text-center md:text-left"},[t._v(" ลิขสิทธิ์ © 2563 "),a("a",{staticClass:"text-white hover:text-gray-400 text-sm font-semibold py-1",attrs:{href:"https://plan.up.ac.th/"}},[t._v(" กองแผนงาน มหาวิทยาลัยพะเยา ")])])]),a("div",{staticClass:"w-full md:w-8/12 px-4"})])])}],l={data:function(){return{date:(new Date).getFullYear()}},props:{absolute:{type:Boolean,default:!1}}},o=l,n=a("2877"),i=Object(n["a"])(o,s,r,!1,null,null,null);e["a"]=i.exports},"6d4c":function(t,e,a){"use strict";a("977d")},7532:function(t,e,a){"use strict";a.r(e);var s=function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("div",[a("sidebar"),a("svg",{staticClass:"absolute top-0",staticStyle:{"z-index":"1"},attrs:{xmlns:"http://www.w3.org/2000/svg",viewBox:"0 0 1440 320"}},[a("path",{attrs:{fill:"#96e0ce","fill-opacity":"1",d:"M0,160L15,138.7C30,117,60,75,90,53.3C120,32,150,32,180,64C210,96,240,160,270,197.3C300,235,330,245,360,218.7C390,192,420,128,450,106.7C480,85,510,107,540,149.3C570,192,600,256,630,245.3C660,235,690,149,720,144C750,139,780,213,810,224C840,235,870,181,900,181.3C930,181,960,235,990,218.7C1020,203,1050,117,1080,96C1110,75,1140,117,1170,133.3C1200,149,1230,139,1260,133.3C1290,128,1320,128,1350,122.7C1380,117,1410,107,1425,101.3L1440,96L1440,0L1425,0C1410,0,1380,0,1350,0C1320,0,1290,0,1260,0C1230,0,1200,0,1170,0C1140,0,1110,0,1080,0C1050,0,1020,0,990,0C960,0,930,0,900,0C870,0,840,0,810,0C780,0,750,0,720,0C690,0,660,0,630,0C600,0,570,0,540,0C510,0,480,0,450,0C420,0,390,0,360,0C330,0,300,0,270,0C240,0,210,0,180,0C150,0,120,0,90,0C60,0,30,0,15,0L0,0Z"}})]),a("div",{staticClass:"relative md:ml-64 bg-gray-200"},[a("admin-navbar"),a("div",{staticClass:"px-4 md:px-10 mx-auto w-full -m-24"},[a("router-view"),a("footer-admin")],1)],1)],1)},r=[],l=(a("ac1f"),a("5319"),a("96cf"),a("1da1")),o=a("d4ec"),n=a("bee2"),i=a("262e"),c=a("2caf"),d=a("9ab4"),p=function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("nav",{staticClass:"absolute top-0 left-0 w-full z-10 bg-transparent md:flex-row md:flex-no-wrap md:justify-start flex items-center p-4"},[a("div",{staticClass:"w-full mx-autp items-center flex justify-between md:flex-no-wrap flex-wrap md:px-10 px-4"},[a("a",{staticClass:" text-sm uppercase hidden lg:inline-block font-semibold",attrs:{href:"javascript:void(0)"}},[t._v(" Dashboard ")]),t._m(0),a("ul",{staticClass:"flex-col md:flex-row list-none items-center hidden md:flex"},[a("user-dropdown")],1)])])},u=[function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("form",{staticClass:"md:flex hidden flex-row flex-wrap items-center lg:ml-auto mr-3"},[a("div",{staticClass:"relative flex w-full flex-wrap items-stretch"},[a("span",{staticClass:"z-10 h-full leading-snug font-normal absolute text-center text-gray-400 absolute bg-transparent rounded text-base items-center justify-center w-8 pl-3 py-3"},[a("i",{staticClass:"fas fa-search"})]),a("input",{staticClass:"px-3 py-3 placeholder-gray-400 text-gray-700 relative bg-white bg-white rounded text-sm shadow outline-none focus:outline-none focus:shadow-outline w-full pl-10",attrs:{type:"text",placeholder:"Search here..."}})])])}],f=a("cf74"),m={components:{UserDropdown:f["a"]}},x=m,w=a("2877"),b=Object(w["a"])(x,p,u,!1,null,null,null),h=b.exports,v=function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("nav",{staticClass:"md:left-0 md:block md:fixed md:top-0 md:bottom-0 md:overflow-y-auto md:flex-row md:flex-no-wrap md:overflow-hidden shadow-xl bg-blue-600 flex flex-wrap items-center justify-between relative md:w-64 z-10 py-4 px-6"},[a("div",{staticClass:"md:flex-col md:items-stretch md:min-h-full md:flex-no-wrap px-0 flex flex-wrap items-center justify-between w-full mx-auto"},[a("button",{staticClass:"cursor-pointer text-black opacity-50 md:hidden px-3 py-1 text-xl leading-none bg-transparent rounded border border-solid border-transparent",attrs:{type:"button"},on:{click:function(e){return t.toggleCollapseShow("bg-white m-2 py-3 px-6")}}},[a("i",{staticClass:"fas fa-bars"})]),a("router-link",{staticClass:"md:block text-left md:pb-2   mr-0 inline-block whitespace-no-wrap text-xl cv-font uppercase font-bold p-4 px-0 text-white",attrs:{to:"/"}},[t._v(" UP ITA (Admin) ")]),a("div",{staticClass:"md:flex md:flex-col md:items-stretch md:opacity-100 md:relative md:mt-4 md:shadow-none shadow absolute top-0 left-0 right-0 z-40 overflow-y-auto overflow-x-hidden h-auto items-center flex-1 rounded",class:t.collapseShow},[a("div",{staticClass:"md:min-w-full md:hidden block pb-4 mb-4 border-b border-solid border-gray-300"},[a("div",{staticClass:"flex flex-wrap"},[a("div",{staticClass:"w-6/12"},[a("router-link",{staticClass:"md:block text-left md:pb-2 text-gray-700 mr-0 inline-block whitespace-no-wrap text-sm uppercase font-bold p-4 px-0",attrs:{to:"/"}},[t._v(" UP ITA (Admin) ")])],1),a("div",{staticClass:"w-6/12 flex justify-end"},[a("button",{staticClass:"cursor-pointer text-black opacity-50 md:hidden px-3 py-1 text-xl leading-none bg-transparent rounded border border-solid border-transparent",attrs:{type:"button"},on:{click:function(e){return t.toggleCollapseShow("hidden")}}},[a("i",{staticClass:"fas fa-times"})])])])]),a("hr",{staticClass:"my-4 md:min-w-full"}),a("h6",{staticClass:"md:min-w-full text-white text-xs uppercase font-bold block pt-1 pb-4 no-underline"},[t._v(" ภาพรวม ")]),a("ul",{staticClass:"md:flex-col md:min-w-full flex flex-col list-none"},[a("li",{staticClass:"items-center"},[a("router-link",{attrs:{to:"/admin/home"},scopedSlots:t._u([{key:"default",fn:function(e){var s=e.href,r=(e.route,e.navigate),l=e.isActive;return[a("a",{staticClass:"text-xs uppercase py-3  block",class:[l?"text-green-300 hover:text-green-300":"text-white hover:text-gray-600"],attrs:{href:s},on:{click:r}},[a("i",{staticClass:"mdi mdi-book  mr-2 text-sm",class:[l?"opacity-75":"text-gray-400"]}),t._v(" ผลการประเมิน ")])]}}])})],1)]),a("hr",{staticClass:"my-4 md:min-w-full"}),a("h6",{staticClass:"md:min-w-full text-white text-xs uppercase font-bold block pt-1 pb-4 no-underline"},[t._v(" ระบบ OIT ")]),a("ul",{staticClass:"md:flex-col md:min-w-full flex flex-col list-none"},[a("li",{staticClass:"items-center"},[a("router-link",{attrs:{to:"/admin/oit/all"},scopedSlots:t._u([{key:"default",fn:function(e){var s=e.href,r=(e.route,e.navigate),l=e.isActive;return[a("a",{staticClass:"text-xs uppercase py-3  block",class:[l?"text-green-300 hover:text-green-300":"text-white hover:text-gray-600"],attrs:{href:s},on:{click:r}},[a("i",{staticClass:"mdi mdi-book  mr-2 text-sm",class:[l?"opacity-75":"text-gray-400"]}),t._v(" การตรวจและรายงานผล ")])]}}])})],1)]),a("hr",{staticClass:"my-4 md:min-w-full"}),a("h6",{staticClass:"md:min-w-full text-white text-xs uppercase font-bold block pt-1 pb-4 no-underline"},[t._v(" ระบบ IIT ")]),a("ul",{staticClass:"md:flex-col md:min-w-full flex flex-col list-none md:mb-4"},[a("li",{staticClass:"items-center"},[a("router-link",{attrs:{to:"/admin/iit/all"},scopedSlots:t._u([{key:"default",fn:function(e){var s=e.href,r=(e.route,e.navigate),l=e.isActive;return[a("a",{staticClass:"text-xs uppercase py-3   block",class:[l?"text-green-300 hover:text-green-300":"text-gray-800 md:text-white hover:text-gray-600"],attrs:{href:s},on:{click:r}},[a("i",{staticClass:"mdi mdi-notebook mr-2 text-base",class:[l?"opacity-75":"text-gray-400"]}),t._v(" รายงานผลของหน่วยงาน ")])]}}])})],1)]),a("hr",{staticClass:"my-4 md:min-w-full"}),a("h6",{staticClass:"md:min-w-full text-white text-xs uppercase font-bold block pt-1 pb-4 no-underline"},[t._v(" ระบบ EIT ")]),a("ul",{staticClass:"md:flex-col md:min-w-full flex flex-col list-none md:mb-4"},[a("li",{staticClass:"items-center"},[a("router-link",{attrs:{to:"/admin/eit/all"},scopedSlots:t._u([{key:"default",fn:function(e){var s=e.href,r=(e.route,e.navigate),l=e.isActive;return[a("a",{staticClass:"text-xs uppercase py-3   block",class:[l?"text-green-300 hover:text-green-300":"text-gray-800 md:text-white hover:text-gray-600"],attrs:{href:s},on:{click:r}},[a("i",{staticClass:"mdi mdi-notebook mr-2 text-base",class:[l?"opacity-75":"text-gray-400"]}),t._v(" รายงานผลของหน่วยงาน ")])]}}])})],1)]),a("hr",{staticClass:"my-4 md:min-w-full"}),a("h6",{staticClass:"md:min-w-full text-white text-xs uppercase font-bold block pt-1 pb-4 no-underline"},[t._v(" ผู้ใช้ ")]),a("ul",{staticClass:"md:flex-col md:min-w-full flex flex-col list-none md:mb-4"},[a("li",{staticClass:"inline-flex"},[a("a",{staticClass:"text-gray-800 hover:text-gray-600 text-sm block mb-4 no-underline font-semibold",attrs:{href:"#"},on:{click:t.logout}},[a("i",{staticClass:"mdi mdi-login mr-2 text-gray-400 text-base"}),t._v(" ออกจากระบบ ")])])])])],1)])},g=[],C=a("227a"),y=a("3951"),k=a("21d1"),_={data:function(){return{collapseShow:"hidden"}},watch:{path:function(t){this.collapseShow="hidden"}},computed:{path:function(){return this.$route.path}},methods:{change:function(){},toggleCollapseShow:function(t){this.collapseShow=t},logout:function(){return Object(l["a"])(regeneratorRuntime.mark((function t(){var e;return regeneratorRuntime.wrap((function(t){while(1)switch(t.prev=t.next){case 0:return t.next=2,k["a"].getUser();case 2:return e=t.sent,console.log(e),t.next=6,y["a"].logout();case 6:return"microsoft.com"==e.register_type&&window.open("https://login.microsoftonline.com/logout.srf","_blank"),t.next=9,location.reload();case 9:case"end":return t.stop()}}),t)})))()}},components:{NotificationDropdown:C["a"],UserDropdown:f["a"]}},S=_,j=(a("6d4c"),Object(w["a"])(S,v,g,!1,null,null,null)),P=j.exports,D=a("1b1c"),O=a("59ac"),A=a("60a3"),I=function(t){Object(i["a"])(a,t);var e=Object(c["a"])(a);function a(){return Object(o["a"])(this,a),e.apply(this,arguments)}return Object(n["a"])(a,[{key:"created",value:function(){var t=Object(l["a"])(regeneratorRuntime.mark((function t(){return regeneratorRuntime.wrap((function(t){while(1)switch(t.prev=t.next){case 0:return t.next=2,y["a"].checkToken();case 2:return t.next=4,k["a"].loadUser();case 4:if("/"!=k["a"].routeUser&&"/admin/"!=k["a"].routeUser){t.next=7;break}return t.next=7,this.$router.replace(k["a"].routeUser);case 7:case"end":return t.stop()}}),t,this)})));function e(){return t.apply(this,arguments)}return e}()}]),a}(A["b"]);I=Object(d["c"])([Object(A["a"])({components:{AdminNavbar:h,Sidebar:P,HeaderStats:D["a"],FooterAdmin:O["a"]},computed:{}})],I);var R=I,E=R,$=Object(w["a"])(E,s,r,!1,null,null,null);e["default"]=$.exports},"977d":function(t,e,a){},cf74:function(t,e,a){"use strict";var s=function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("div",[a("a",{ref:"btnDropdownRef",staticClass:"text-gray-600 block",attrs:{href:"#pablo"},on:{click:function(e){return t.toggleDropdown(e)}}},[a("div",{staticClass:"items-center flex"},[a("span",{staticClass:"w-12 h-12 text-sm text-white bg-gray-300 inline-flex items-center justify-center rounded-full"},[a("img",{staticClass:"w-full rounded-full align-middle border-none shadow-lg",attrs:{alt:"...",src:t.image}})])])]),a("div",{ref:"popoverDropdownRef",staticClass:"bg-white text-base z-50 float-left py-2 list-none text-left rounded shadow-lg min-w-48",class:{hidden:!t.dropdownPopoverShow,block:t.dropdownPopoverShow}},[a("a",{staticClass:"text-sm py-2 px-4 font-normal block w-full whitespace-no-wrap bg-transparent text-gray-800",attrs:{href:"javascript:void(0);"}},[t._v(" ข้อมูลส่วนตัว ")]),a("a",{staticClass:"text-sm py-2 px-4 font-normal block w-full whitespace-no-wrap bg-transparent text-gray-800",attrs:{href:"javascript:void(0);"}},[t._v(" ข้อมูลเกษตรกร ")]),a("a",{staticClass:"text-sm py-2 px-4 font-normal block w-full whitespace-no-wrap bg-transparent text-gray-800",attrs:{href:"javascript:void(0);"}},[t._v(" ข้อมูลควาย ")]),a("div",{staticClass:"h-0 my-2 border border-solid border-gray-200"}),a("a",{staticClass:"text-sm py-2 px-4 font-normal block w-full whitespace-no-wrap bg-transparent text-gray-800",attrs:{href:"javascript:void(0);"},on:{click:function(e){return t.logout()}}},[t._v(" ออกจากระบบ ")])])])},r=[],l=(a("96cf"),a("1da1")),o=a("39c3"),n=a("3951"),i={data:function(){return{dropdownPopoverShow:!1,image:image}},methods:{toggleDropdown:function(t){t.preventDefault(),this.dropdownPopoverShow?this.dropdownPopoverShow=!1:(this.dropdownPopoverShow=!0,Object(o["a"])(this.$refs.btnDropdownRef,this.$refs.popoverDropdownRef,{placement:"bottom-start"}))},logout:function(){return Object(l["a"])(regeneratorRuntime.mark((function t(){return regeneratorRuntime.wrap((function(t){while(1)switch(t.prev=t.next){case 0:return t.next=2,n["a"].logout();case 2:return t.next=4,location.reload();case 4:case"end":return t.stop()}}),t)})))()}}},c=i,d=a("2877"),p=Object(d["a"])(c,s,r,!1,null,null,null);e["a"]=p.exports}}]);
//# sourceMappingURL=chunk-f4baaf5e.f8aa975b.js.map