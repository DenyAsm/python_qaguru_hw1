from selene import browser, have, Browser, be

#####
def test_captcha_should_be_shown():
    browser.open('https://google.com')
    browser.element('[name="q"]').type('qa.guru').press_enter()
    browser.element('html').should(have.text('Об этой странице'))

def test_captcha_should_be_shown1():
    browser.open('https://google.com')
    browser.element('[name="q"]').type('qa.guru')
    browser.element('[name="btnK"]').click()
    browser.element('html').should(have.text('Об этой странице'))

def test_other_site_show():
    browser.open('https://duckduckgo.com/')
    browser.element('[data-testid="hero"]').should(have.text('Подробнее'))
    browser.element('[id="searchbox_input"]').type('tutorials selene github')
    browser.element('[type="submit"]').should(be.visible)
    browser.element('[type="submit"]').click()
    # breakpoint()
    # browser.should(have.js_returned(True, 'return document.readyState === "complete"'))
    browser.element('[id="web_content_wrapper"]').should(have.text('GitHub - FunctionLab/selene: a framework for training '))