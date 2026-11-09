// Ранги Рун и Восходящих в таблицах: «золото», «серебро»… -> цветные метки
(function () {
  var MAP = { "дерево": "derevo", "деревянн": "derevo", "бронза": "bronza", "бронзов": "bronza", "серебро": "serebro",
              "серебрян": "serebro", "золото": "zoloto", "золот": "zoloto", "небо": "nebo", "небесн": "nebo",
              "мусор": "musor", "мерзость": "merzost", "обычная": "obychnaya" };
  var RX = /^(дерево|бронза|серебро|золото|небо|мусор|мерзость|обычная|драконье \((?:серебро|золото)\)|драконья)$/i;
  function mark() {
    document.querySelectorAll(".md-typeset table td").forEach(function (td) {
      if (td.dataset.rank || td.children.length) return;
      var t = td.textContent.trim();
      if (!RX.test(t)) return;
      var low = t.toLowerCase(), cls = "serebro";
      Object.keys(MAP).forEach(function (k) { if (low.indexOf(k) >= 0) cls = MAP[k]; });
      td.dataset.rank = cls;
      td.innerHTML = '<span class="rank rank--' + cls + '">' + t + "</span>";
    });
  }
  if (typeof document$ !== "undefined") document$.subscribe(mark); else document.addEventListener("DOMContentLoaded", mark);
})();
