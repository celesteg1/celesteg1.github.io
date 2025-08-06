document$.subscribe(() => {
  // Look for any Swagger containers that haven't been rendered yet
  document.querySelectorAll('[data-render-swagger-url]').forEach(el => {
    // Check if the Swagger UI has already been injected
    if (el.querySelector('.swagger-ui')) return;

    const specUrl = el.getAttribute('data-render-swagger-url');

    // Render Swagger UI inside this element
    window.SwaggerUIBundle({
      url: specUrl,
      domNode: el,
      layout: "BaseLayout",
      presets: [SwaggerUIBundle.presets.apis],
    });
  });
});
