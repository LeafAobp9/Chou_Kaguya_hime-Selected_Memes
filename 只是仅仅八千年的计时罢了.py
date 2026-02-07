import time
import random

remaining_time = 252288000000
#8000年=252288000000秒
runami_yachiyo_sexual_repression = 123 + 784
#在七八测量网站“ https://kk.140.icu/192/#1770452525042 ”测得“月下八千代”78长度为123cm，“辉夜”78长度为784cm，故星压抑度初始值取这个，这个值没有上限

while remaining_time != 0:
    time.sleep(1)
    print(f"距离与彩叶重逢还有{remaining_time - 1}秒")
    remaining_time -= 1
    runami_yachiyo_sexual_repression += random.randint(0,10)
    
    # print(f"星压抑程度为{runami_yachiyo_sexual_repression}") 

print("辉彩万岁!")
print(f"请小彩叶注意，八千代已经积攒了8000年的星压抑，目前星压抑程度为 {runami_yachiyo_sexual_repression} ，请注意不要被榨干哦")

#以下是那个78测量网站的js代码：
# const clickSound=new Audio('static/1.mp3');
# function initMoreBtnLink(){const e=document.querySelector('.more-btn a');fetch('../domain.php').then(r=>{if(!r.ok)throw new Error(`请求失败：${r.status}`);return r.json()}).then(d=>{d&&d.success&&"string"==typeof d.domain&&d.domain.trim()&&(e.href=d.domain.trim())}).catch(e=>{})}
# window.onload=()=>initMoreBtnLink();
# const [analyzeBtn,usernameInput,resultSection,resultUsername,lengthResult,progressBar,evaluation,moreBtn]=['analyzeBtn','username','resultSection','resultUsername','lengthResult','progressBar','evaluation','more-btn'].map(id=>document.getElementById(id));
#
# function getRandomLength(){
#   const r=Math.random()*100;
#   if(r<20)return Math.floor(Math.random()*6);
#   if(r<35)return Math.floor(Math.random()*5)+6;
#   if(r<45)return Math.floor(Math.random()*3)+11;
#   if(r<55)return Math.floor(Math.random()*3)+14;
#   if(r<75)return Math.floor(Math.random()*4)+17;
#   return Math.random()>0.5?Math.floor(Math.random()*5)+21:Math.floor(Math.random()*901)+100;
# }
#
# analyzeBtn.addEventListener('click',()=>{
#   clickSound.play().catch(e=>{});
#   const username=usernameInput.value.trim();
#   if(!username)return alert('信息不能为空');
#
#   // 分析中禁用输入框，阻止修改用户名
#   usernameInput.disabled=true;
#   analyzeBtn.disabled=true;
#   analyzeBtn.classList.add('btn-loading');
#   analyzeBtn.innerHTML='<div class="spinner"></div><span>分析中...</span>';
#
#   setTimeout(()=>{
#     resultSection.classList.add('show');
#     moreBtn.style.display='block';
#     resultUsername.textContent=username;
#     const len=getRandomLength();
#     progressBar.style.width=`${len>=100?100:len/25*100}%`;
# 
#     const evals={
#       s:['略短：别灰心，还有成长空间','略短：不必焦虑，尺寸并非一切','略短：保持自信，内在更重要'],
#       sh:['较短：还算正常范围','较短：多数人的水平，不必担心','较短：够用就好，无需过度比较'],
#       ml:['中等偏下：仍需努力','中等偏下：中间水平，还有提升空间','中等偏下：日常使用足够，不必苛求'],
#       m:['中规中矩：还行吧,不算丢人','中规中矩：标准水平，无需自卑','中规中矩：大多数人羡慕的程度'],
#       g:['良好：超过平均水平','良好：已经很出色了，值得肯定','良好：超越多数人，继续保持'],
#       e:['优秀：值得骄傲的长度','优秀：相当出色，令人羡慕','优秀：顶级水平，无需低调']
#     };
#  
#     let evalText;
#     if(len<=5)evalText=evals.s[Math.floor(Math.random()*3)];
#     else if(len<=10)evalText=evals.sh[Math.floor(Math.random()*3)];
#     else if(len<=13)evalText=evals.ml[Math.floor(Math.random()*3)];
#     else if(len<=16)evalText=evals.m[Math.floor(Math.random()*3)];
#     else if(len<=20)evalText=evals.g[Math.floor(Math.random()*3)];
#     else evalText=evals.e[Math.floor(Math.random()*3)];
#
#     evaluation.textContent=evalText;
#     animateValue(lengthResult,0,len,1500);
#
#     // 分析完成启用输入框，允许重新修改
#     usernameInput.disabled=false;
#     analyzeBtn.disabled=false;
#     analyzeBtn.classList.remove('btn-loading');
#     analyzeBtn.innerHTML='<span>重新检测</span>';
#   },2000);
# });
#
# usernameInput.addEventListener('keypress',e=>e.key==='Enter'&&analyzeBtn.click());
#
# function animateValue(el,s,e,d){
#   let st=null;
#   const step=t=>{
#     st||(st=t);
#     const p=Math.min((t-st)/d,1);
#     el.textContent=`${Math.floor(p*(e-s)+s)}cm`;
#     p<1&&requestAnimationFrame(step);
#   };
#   requestAnimationFrame(step);
# }
#
# document.addEventListener('touchmove',e=>e.preventDefault(),{passive:false});
# document.addEventListener('wheel',e=>e.preventDefault(),{passive:false});
# // 合并到此处：时间戳hash功能（原有代码末尾添加）
# function addTimestampHash() {
#   const timestamp = Date.now();
#   window.location.hash = timestamp;
# }
#
# if (document.readyState === "loading") {
#   document.addEventListener("DOMContentLoaded", addTimestampHash);
# } else {
#   addTimestampHash();
# }