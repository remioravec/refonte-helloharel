/* ==========================================================================
   HELLO HAREL — Animations & Interactions
   À injecter via Elementor > Custom Code (avant </body>)
   ========================================================================== */

document.addEventListener('DOMContentLoaded', function () {

  /* --- Scroll Reveal: .hh-fade-in elements --- */
  var fadeObserver = new IntersectionObserver(function (entries) {
    entries.forEach(function (entry) {
      if (entry.isIntersecting) {
        entry.target.classList.add('hh-visible');
        fadeObserver.unobserve(entry.target);
      }
    });
  }, { threshold: 0.15, rootMargin: '0px 0px -50px 0px' });

  document.querySelectorAll('.hh-fade-in').forEach(function (el) {
    fadeObserver.observe(el);
  });

  /* --- FAQ Accordion: .hh-faq-item toggles --- */
  document.querySelectorAll('.hh-faq-item').forEach(function (item) {
    var btn = item.querySelector('button, .elementor-tab-title, .card-header');
    if (btn) {
      btn.addEventListener('click', function () {
        var isActive = item.classList.contains('active');
        /* Close all siblings */
        var parent = item.parentElement;
        if (parent) {
          parent.querySelectorAll('.hh-faq-item').forEach(function (sibling) {
            sibling.classList.remove('active');
          });
        }
        if (!isActive) {
          item.classList.add('active');
        }
      });
    }
  });

  /* --- Mega Menu: Dynamic description on hover (Métiers dropdown) --- */
  var dynamicDesc = document.getElementById('metiers-dynamic-desc');
  if (dynamicDesc) {
    var defaultText = dynamicDesc.textContent;
    document.querySelectorAll('.metier-link').forEach(function (link) {
      link.addEventListener('mouseenter', function () {
        var desc = link.getAttribute('data-desc');
        if (desc) {
          dynamicDesc.textContent = desc;
          dynamicDesc.style.color = '#1d4ed8';
        }
      });
      link.addEventListener('mouseleave', function () {
        dynamicDesc.textContent = defaultText;
        dynamicDesc.style.color = '';
      });
    });
  }

});
