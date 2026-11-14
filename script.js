'use strict';
// ナビゲーションと内容は JavaScript を無効にしても利用できます。
const year = document.getElementById('year');
if (year) year.textContent = new Date().getFullYear();
