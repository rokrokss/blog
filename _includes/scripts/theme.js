(function () {
  var key = 'rokrokss-theme';
  var system = window.matchMedia('(prefers-color-scheme: dark)');
  var choice;
  var light = document.getElementById('theme-light');
  var dark = document.getElementById('theme-dark');
  try { choice = localStorage.getItem(key); } catch (error) {}
  if (choice !== 'dark' && choice !== 'light') { choice = null; }

  function apply() {
    var isDark = choice ? choice === 'dark' : system.matches;
    document.documentElement.dataset.theme = isDark ? 'dark' : 'light';
    light.media = isDark ? 'not all' : 'all';
    dark.media = isDark ? 'all' : 'not all';
    document.querySelector('meta[name="theme-color"]').content = isDark ? '#17191e' : '#ffffff';
    document.querySelectorAll('.js-theme-toggle').forEach(function (button) {
      button.setAttribute('aria-checked', String(isDark));
      button.title = isDark ? '라이트 모드로 전환' : '다크 모드로 전환';
    });
  }

  // Runs in the head, before the first page paint.
  apply();
  document.addEventListener('DOMContentLoaded', function () {
    apply();
    document.querySelectorAll('.js-theme-toggle').forEach(function (button) {
      button.addEventListener('click', function () {
        choice = document.documentElement.dataset.theme === 'dark' ? 'light' : 'dark';
        try { localStorage.setItem(key, choice); } catch (error) {}
        apply();
      });
    });
  });
  system.addEventListener('change', function () { if (!choice) { apply(); } });
  window.addEventListener('storage', function (event) {
    if (event.key === key || event.key === null) {
      choice = event.newValue === 'dark' || event.newValue === 'light' ? event.newValue : null;
      apply();
    }
  });
})();
