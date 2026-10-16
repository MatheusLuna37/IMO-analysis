from bs4 import BeautifulSoup

# Substitui pela tua string HTML ou lê a partir de um ficheiro
html_content = """
<tbody>
        
        
        <tr>
          <td>
            <a href="/countries/AFG/" class="data-table__country-cell">
              <img class="data-table__country-flag" src="/assets/images/countries/flags/afg.svg" alt="">
              <span class="data-table__country-full">Afghanistan</span><span class="data-table__country-iso">AFG</span>
            </a>
          </td>
          <td>
            
              Onder Akkusci
            
          </td>
          <td>
            
              <a href="mailto:onderakkuscu@gmail.com" class="js-contact-email" data-email-user="onderakkuscu" data-email-domain="gmail.com" aria-label="Email Onder Akkusci" title="Email">
                <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 1024 1024" aria-hidden="true" focusable="false"><path fill="currentColor" d="M928 160H96c-17.7 0-32 14.3-32 32v640c0 17.7 14.3 32 32 32h832c17.7 0 32-14.3 32-32V192c0-17.7-14.3-32-32-32m-40 110.8V792H136V270.8l-27.6-21.5l39.3-50.5l42.8 33.3h643.1l42.8-33.3l39.3 50.5zM833.6 232L512 482L190.4 232l-42.8-33.3l-39.3 50.5l27.6 21.5l341.6 265.6a55.99 55.99 0 0 0 68.7 0L888 270.8l27.6-21.5l-39.3-50.5z"></path></svg>
              </a>
            
          </td>
          <td>
            
          </td>
          <td class="data-table__hide-mobile data-table__num">
            
          </td>
          <td class="data-table__hide-mobile data-table__num">
            0
          </td>
          <td class="data-table__hide-mobile">
            
          </td>
        </tr>
        
        <tr>
          <td>
            <a href="/countries/AGO/" class="data-table__country-cell">
              <img class="data-table__country-flag" src="/assets/images/countries/flags/ago.svg" alt="">
              <span class="data-table__country-full">Angola</span><span class="data-table__country-iso">AGO</span>
            </a>
          </td>
          <td>
            
              Gabriel Boaventura
            
          </td>
          <td>
            
              <a href="mailto:gabrielboaventura1968@gmail.com" class="js-contact-email" data-email-user="gabrielboaventura1968" data-email-domain="gmail.com" aria-label="Email Gabriel Boaventura" title="Email">
                <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 1024 1024" aria-hidden="true" focusable="false"><path fill="currentColor" d="M928 160H96c-17.7 0-32 14.3-32 32v640c0 17.7 14.3 32 32 32h832c17.7 0 32-14.3 32-32V192c0-17.7-14.3-32-32-32m-40 110.8V792H136V270.8l-27.6-21.5l39.3-50.5l42.8 33.3h643.1l42.8-33.3l39.3 50.5zM833.6 232L512 482L190.4 232l-42.8-33.3l-39.3 50.5l27.6 21.5l341.6 265.6a55.99 55.99 0 0 0 68.7 0L888 270.8l27.6-21.5l-39.3-50.5z"></path></svg>
              </a>
            
          </td>
          <td>
            
          </td>
          <td class="data-table__hide-mobile data-table__num">
            2019
          </td>
          <td class="data-table__hide-mobile data-table__num">
            1
          </td>
          <td class="data-table__hide-mobile">
            
          </td>
        </tr>
        
        <tr>
          <td>
            <a href="/countries/ALB/" class="data-table__country-cell">
              <img class="data-table__country-flag" src="/assets/images/countries/flags/alb.svg" alt="">
              <span class="data-table__country-full">Albania</span><span class="data-table__country-iso">ALB</span>
            </a>
          </td>
          <td>
            
              Adrian Naço
            
          </td>
          <td>
            
              <a href="mailto:nacosotir@gmail.com" class="js-contact-email" data-email-user="nacosotir" data-email-domain="gmail.com" aria-label="Email Adrian Naço" title="Email">
                <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 1024 1024" aria-hidden="true" focusable="false"><path fill="currentColor" d="M928 160H96c-17.7 0-32 14.3-32 32v640c0 17.7 14.3 32 32 32h832c17.7 0 32-14.3 32-32V192c0-17.7-14.3-32-32-32m-40 110.8V792H136V270.8l-27.6-21.5l39.3-50.5l42.8 33.3h643.1l42.8-33.3l39.3 50.5zM833.6 232L512 482L190.4 232l-42.8-33.3l-39.3 50.5l27.6 21.5l341.6 265.6a55.99 55.99 0 0 0 68.7 0L888 270.8l27.6-21.5l-39.3-50.5z"></path></svg>
              </a>
            
          </td>
          <td>
            
              <a href="https://www.ama.org.al" target="_blank" rel="noopener" aria-label="Visit national MO website for Albania (opens in new tab)"><span class="data-table__label-full">Visit ↗</span><span class="data-table__label-short">↗</span></a>
            
          </td>
          <td class="data-table__hide-mobile data-table__num">
            1993
          </td>
          <td class="data-table__hide-mobile data-table__num">
            29
          </td>
          <td class="data-table__hide-mobile">
            
          </td>
        </tr>
        
        <tr>
          <td>
            <a href="/countries/ALG/" class="data-table__country-cell">
              <img class="data-table__country-flag" src="/assets/images/countries/flags/alg.svg" alt="">
              <span class="data-table__country-full">Algeria</span><span class="data-table__country-iso">ALG</span>
            </a>
          </td>
          <td>
            
              Abdallah Rahmani
            
          </td>
          <td>
            
              <a href="mailto:rahmaniabdallah62@gmail.com" class="js-contact-email" data-email-user="rahmaniabdallah62" data-email-domain="gmail.com" aria-label="Email Abdallah Rahmani" title="Email">
                <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 1024 1024" aria-hidden="true" focusable="false"><path fill="currentColor" d="M928 160H96c-17.7 0-32 14.3-32 32v640c0 17.7 14.3 32 32 32h832c17.7 0 32-14.3 32-32V192c0-17.7-14.3-32-32-32m-40 110.8V792H136V270.8l-27.6-21.5l39.3-50.5l42.8 33.3h643.1l42.8-33.3l39.3 50.5zM833.6 232L512 482L190.4 232l-42.8-33.3l-39.3 50.5l27.6 21.5l341.6 265.6a55.99 55.99 0 0 0 68.7 0L888 270.8l27.6-21.5l-39.3-50.5z"></path></svg>
              </a>
            
          </td>
          <td>
            
          </td>
          <td class="data-table__hide-mobile data-table__num">
            1977
          </td>
          <td class="data-table__hide-mobile data-table__num">
            25
          </td>
          <td class="data-table__hide-mobile">
            
          </td>
        </tr>
        
        <tr>
          <td>
            <a href="/countries/ARG/" class="data-table__country-cell">
              <img class="data-table__country-flag" src="/assets/images/countries/flags/arg.svg" alt="">
              <span class="data-table__country-full">Argentina</span><span class="data-table__country-iso">ARG</span>
            </a>
          </td>
          <td>
            
              Patricia Fauring
            
          </td>
          <td>
            
              <a href="mailto:fauringpatricia@gmail.com" class="js-contact-email" data-email-user="fauringpatricia" data-email-domain="gmail.com" aria-label="Email Patricia Fauring" title="Email">
                <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 1024 1024" aria-hidden="true" focusable="false"><path fill="currentColor" d="M928 160H96c-17.7 0-32 14.3-32 32v640c0 17.7 14.3 32 32 32h832c17.7 0 32-14.3 32-32V192c0-17.7-14.3-32-32-32m-40 110.8V792H136V270.8l-27.6-21.5l39.3-50.5l42.8 33.3h643.1l42.8-33.3l39.3 50.5zM833.6 232L512 482L190.4 232l-42.8-33.3l-39.3 50.5l27.6 21.5l341.6 265.6a55.99 55.99 0 0 0 68.7 0L888 270.8l27.6-21.5l-39.3-50.5z"></path></svg>
              </a>
            
          </td>
          <td>
            
              <a href="http://www.oma.org.ar/" target="_blank" rel="noopener" aria-label="Visit national MO website for Argentina (opens in new tab)"><span class="data-table__label-full">Visit ↗</span><span class="data-table__label-short">↗</span></a>
            
          </td>
          <td class="data-table__hide-mobile data-table__num">
            1988
          </td>
          <td class="data-table__hide-mobile data-table__num">
            38
          </td>
          <td class="data-table__hide-mobile">
            
              1997, 2012
            
          </td>
        </tr>
        
        <tr>
          <td>
            <a href="/countries/ARM/" class="data-table__country-cell">
              <img class="data-table__country-flag" src="/assets/images/countries/flags/arm.svg" alt="">
              <span class="data-table__country-full">Armenia</span><span class="data-table__country-iso">ARM</span>
            </a>
          </td>
          <td>
            
              Grigor Keropyan
            
          </td>
          <td>
            
              <a href="mailto:grigorkeropyan@gmail.com" class="js-contact-email" data-email-user="grigorkeropyan" data-email-domain="gmail.com" aria-label="Email Grigor Keropyan" title="Email">
                <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 1024 1024" aria-hidden="true" focusable="false"><path fill="currentColor" d="M928 160H96c-17.7 0-32 14.3-32 32v640c0 17.7 14.3 32 32 32h832c17.7 0 32-14.3 32-32V192c0-17.7-14.3-32-32-32m-40 110.8V792H136V270.8l-27.6-21.5l39.3-50.5l42.8 33.3h643.1l42.8-33.3l39.3 50.5zM833.6 232L512 482L190.4 232l-42.8-33.3l-39.3 50.5l27.6 21.5l341.6 265.6a55.99 55.99 0 0 0 68.7 0L888 270.8l27.6-21.5l-39.3-50.5z"></path></svg>
              </a>
            
          </td>
          <td>
            
              <a href="http://www.olymp.am" target="_blank" rel="noopener" aria-label="Visit national MO website for Armenia (opens in new tab)"><span class="data-table__label-full">Visit ↗</span><span class="data-table__label-short">↗</span></a>
            
          </td>
          <td class="data-table__hide-mobile data-table__num">
            1993
          </td>
          <td class="data-table__hide-mobile data-table__num">
            34
          </td>
          <td class="data-table__hide-mobile">
            
          </td>
        </tr>
        
        <tr>
          <td>
            <a href="/countries/AUS/" class="data-table__country-cell">
              <img class="data-table__country-flag" src="/assets/images/countries/flags/aus.svg" alt="">
              <span class="data-table__country-full">Australia</span><span class="data-table__country-iso">AUS</span>
            </a>
          </td>
          <td>
            
              Mark Barnes
            
          </td>
          <td>
            
              <a href="mailto:olympiads@amt.edu.au" class="js-contact-email" data-email-user="olympiads" data-email-domain="amt.edu.au" aria-label="Email Mark Barnes" title="Email">
                <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 1024 1024" aria-hidden="true" focusable="false"><path fill="currentColor" d="M928 160H96c-17.7 0-32 14.3-32 32v640c0 17.7 14.3 32 32 32h832c17.7 0 32-14.3 32-32V192c0-17.7-14.3-32-32-32m-40 110.8V792H136V270.8l-27.6-21.5l39.3-50.5l42.8 33.3h643.1l42.8-33.3l39.3 50.5zM833.6 232L512 482L190.4 232l-42.8-33.3l-39.3 50.5l27.6 21.5l341.6 265.6a55.99 55.99 0 0 0 68.7 0L888 270.8l27.6-21.5l-39.3-50.5z"></path></svg>
              </a>
            
          </td>
          <td>
            
              <a href="http://www.amt.edu.au/" target="_blank" rel="noopener" aria-label="Visit national MO website for Australia (opens in new tab)"><span class="data-table__label-full">Visit ↗</span><span class="data-table__label-short">↗</span></a>
            
          </td>
          <td class="data-table__hide-mobile data-table__num">
            1981
          </td>
          <td class="data-table__hide-mobile data-table__num">
            46
          </td>
          <td class="data-table__hide-mobile">
            
              1988, 2025
            
          </td>
        </tr>
        
        <tr>
          <td>
            <a href="/countries/AUT/" class="data-table__country-cell">
              <img class="data-table__country-flag" src="/assets/images/countries/flags/aut.svg" alt="">
              <span class="data-table__country-full">Austria</span><span class="data-table__country-iso">AUT</span>
            </a>
          </td>
          <td>
            
              Theresia Eisenkölbl
            
          </td>
          <td>
            
              <a href="mailto:theresia.eisenkoelbl@univie.ac.at" class="js-contact-email" data-email-user="theresia.eisenkoelbl" data-email-domain="univie.ac.at" aria-label="Email Theresia Eisenkölbl" title="Email">
                <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 1024 1024" aria-hidden="true" focusable="false"><path fill="currentColor" d="M928 160H96c-17.7 0-32 14.3-32 32v640c0 17.7 14.3 32 32 32h832c17.7 0 32-14.3 32-32V192c0-17.7-14.3-32-32-32m-40 110.8V792H136V270.8l-27.6-21.5l39.3-50.5l42.8 33.3h643.1l42.8-33.3l39.3 50.5zM833.6 232L512 482L190.4 232l-42.8-33.3l-39.3 50.5l27.6 21.5l341.6 265.6a55.99 55.99 0 0 0 68.7 0L888 270.8l27.6-21.5l-39.3-50.5z"></path></svg>
              </a>
            
          </td>
          <td>
            
              <a href="https://www.oemo.at" target="_blank" rel="noopener" aria-label="Visit national MO website for Austria (opens in new tab)"><span class="data-table__label-full">Visit ↗</span><span class="data-table__label-short">↗</span></a>
            
          </td>
          <td class="data-table__hide-mobile data-table__num">
            1970
          </td>
          <td class="data-table__hide-mobile data-table__num">
            56
          </td>
          <td class="data-table__hide-mobile">
            
              1976
            
          </td>
        </tr>
        
        <tr>
          <td>
            <a href="/countries/AZE/" class="data-table__country-cell">
              <img class="data-table__country-flag" src="/assets/images/countries/flags/aze.svg" alt="">
              <span class="data-table__country-full">Azerbaijan</span><span class="data-table__country-iso">AZE</span>
            </a>
          </td>
          <td>
            
              Fuad Garayev
            
          </td>
          <td>
            
              <a href="mailto:fuad.qarayev@arti.edu.az" class="js-contact-email" data-email-user="fuad.qarayev" data-email-domain="arti.edu.az" aria-label="Email Fuad Garayev" title="Email">
                <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 1024 1024" aria-hidden="true" focusable="false"><path fill="currentColor" d="M928 160H96c-17.7 0-32 14.3-32 32v640c0 17.7 14.3 32 32 32h832c17.7 0 32-14.3 32-32V192c0-17.7-14.3-32-32-32m-40 110.8V792H136V270.8l-27.6-21.5l39.3-50.5l42.8 33.3h643.1l42.8-33.3l39.3 50.5zM833.6 232L512 482L190.4 232l-42.8-33.3l-39.3 50.5l27.6 21.5l341.6 265.6a55.99 55.99 0 0 0 68.7 0L888 270.8l27.6-21.5l-39.3-50.5z"></path></svg>
              </a>
            
          </td>
          <td>
            
          </td>
          <td class="data-table__hide-mobile data-table__num">
            1993
          </td>
          <td class="data-table__hide-mobile data-table__num">
            33
          </td>
          <td class="data-table__hide-mobile">
            
          </td>
        </tr>
        
        <tr>
          <td>
            <a href="/countries/BAH/" class="data-table__country-cell">
              <img class="data-table__country-flag" src="/assets/images/countries/flags/bah.svg" alt="">
              <span class="data-table__country-full">Bahrain</span><span class="data-table__country-iso">BAH</span>
            </a>
          </td>
          <td>
            
          </td>
          <td>
            
          </td>
          <td>
            
          </td>
          <td class="data-table__hide-mobile data-table__num">
            1990
          </td>
          <td class="data-table__hide-mobile data-table__num">
            3
          </td>
          <td class="data-table__hide-mobile">
            
          </td>
        </tr>
        
        <tr>
          <td>
            <a href="/countries/BEL/" class="data-table__country-cell">
              <img class="data-table__country-flag" src="/assets/images/countries/flags/bel.svg" alt="">
              <span class="data-table__country-full">Belgium</span><span class="data-table__country-iso">BEL</span>
            </a>
          </td>
          <td>
            
              Bart Windels
            
          </td>
          <td>
            
              <a href="mailto:bart.windels@telenet.be" class="js-contact-email" data-email-user="bart.windels" data-email-domain="telenet.be" aria-label="Email Bart Windels" title="Email">
                <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 1024 1024" aria-hidden="true" focusable="false"><path fill="currentColor" d="M928 160H96c-17.7 0-32 14.3-32 32v640c0 17.7 14.3 32 32 32h832c17.7 0 32-14.3 32-32V192c0-17.7-14.3-32-32-32m-40 110.8V792H136V270.8l-27.6-21.5l39.3-50.5l42.8 33.3h643.1l42.8-33.3l39.3 50.5zM833.6 232L512 482L190.4 232l-42.8-33.3l-39.3 50.5l27.6 21.5l341.6 265.6a55.99 55.99 0 0 0 68.7 0L888 270.8l27.6-21.5l-39.3-50.5z"></path></svg>
              </a>
            
          </td>
          <td>
            
              <a href="https://www.vwo.be/vwo/belgianmatholympiads" target="_blank" rel="noopener" aria-label="Visit national MO website for Belgium (opens in new tab)"><span class="data-table__label-full">Visit ↗</span><span class="data-table__label-short">↗</span></a>
            
          </td>
          <td class="data-table__hide-mobile data-table__num">
            1969
          </td>
          <td class="data-table__hide-mobile data-table__num">
            48
          </td>
          <td class="data-table__hide-mobile">
            
          </td>
        </tr>
        
        <tr>
          <td>
            <a href="/countries/BEN/" class="data-table__country-cell">
              <img class="data-table__country-flag" src="/assets/images/countries/flags/ben.svg" alt="">
              <span class="data-table__country-full">Benin</span><span class="data-table__country-iso">BEN</span>
            </a>
          </td>
          <td>
            
              Leonard Todjihounde
            
          </td>
          <td>
            
              <a href="mailto:leonardt67@gmail.com" class="js-contact-email" data-email-user="leonardt67" data-email-domain="gmail.com" aria-label="Email Leonard Todjihounde" title="Email">
                <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 1024 1024" aria-hidden="true" focusable="false"><path fill="currentColor" d="M928 160H96c-17.7 0-32 14.3-32 32v640c0 17.7 14.3 32 32 32h832c17.7 0 32-14.3 32-32V192c0-17.7-14.3-32-32-32m-40 110.8V792H136V270.8l-27.6-21.5l39.3-50.5l42.8 33.3h643.1l42.8-33.3l39.3 50.5zM833.6 232L512 482L190.4 232l-42.8-33.3l-39.3 50.5l27.6 21.5l341.6 265.6a55.99 55.99 0 0 0 68.7 0L888 270.8l27.6-21.5l-39.3-50.5z"></path></svg>
              </a>
            
          </td>
          <td>
            
          </td>
          <td class="data-table__hide-mobile data-table__num">
            2009
          </td>
          <td class="data-table__hide-mobile data-table__num">
            2
          </td>
          <td class="data-table__hide-mobile">
            
          </td>
        </tr>
        
        <tr>
          <td>
            <a href="/countries/BFA/" class="data-table__country-cell">
              <img class="data-table__country-flag" src="/assets/images/countries/flags/bfa.svg" alt="">
              <span class="data-table__country-full">Burkina Faso</span><span class="data-table__country-iso">BFA</span>
            </a>
          </td>
          <td>
            
              Antonio Kambiré
            
          </td>
          <td>
            
              <a href="mailto:antoniokambire@gmail.com" class="js-contact-email" data-email-user="antoniokambire" data-email-domain="gmail.com" aria-label="Email Antonio Kambiré" title="Email">
                <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 1024 1024" aria-hidden="true" focusable="false"><path fill="currentColor" d="M928 160H96c-17.7 0-32 14.3-32 32v640c0 17.7 14.3 32 32 32h832c17.7 0 32-14.3 32-32V192c0-17.7-14.3-32-32-32m-40 110.8V792H136V270.8l-27.6-21.5l39.3-50.5l42.8 33.3h643.1l42.8-33.3l39.3 50.5zM833.6 232L512 482L190.4 232l-42.8-33.3l-39.3 50.5l27.6 21.5l341.6 265.6a55.99 55.99 0 0 0 68.7 0L888 270.8l27.6-21.5l-39.3-50.5z"></path></svg>
              </a>
            
          </td>
          <td>
            
              <a href="https://cmathburkina.org" target="_blank" rel="noopener" aria-label="Visit national MO website for Burkina Faso (opens in new tab)"><span class="data-table__label-full">Visit ↗</span><span class="data-table__label-short">↗</span></a>
            
          </td>
          <td class="data-table__hide-mobile data-table__num">
            2014
          </td>
          <td class="data-table__hide-mobile data-table__num">
            2
          </td>
          <td class="data-table__hide-mobile">
            
          </td>
        </tr>
        
        <tr>
          <td>
            <a href="/countries/BGD/" class="data-table__country-cell">
              <img class="data-table__country-flag" src="/assets/images/countries/flags/bgd.svg" alt="">
              <span class="data-table__country-full">Bangladesh</span><span class="data-table__country-iso">BGD</span>
            </a>
          </td>
          <td>
            
              Mahbub Majumdar
            
          </td>
          <td>
            
              <a href="mailto:where.is.mahbub@gmail.com" class="js-contact-email" data-email-user="where.is.mahbub" data-email-domain="gmail.com" aria-label="Email Mahbub Majumdar" title="Email">
                <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 1024 1024" aria-hidden="true" focusable="false"><path fill="currentColor" d="M928 160H96c-17.7 0-32 14.3-32 32v640c0 17.7 14.3 32 32 32h832c17.7 0 32-14.3 32-32V192c0-17.7-14.3-32-32-32m-40 110.8V792H136V270.8l-27.6-21.5l39.3-50.5l42.8 33.3h643.1l42.8-33.3l39.3 50.5zM833.6 232L512 482L190.4 232l-42.8-33.3l-39.3 50.5l27.6 21.5l341.6 265.6a55.99 55.99 0 0 0 68.7 0L888 270.8l27.6-21.5l-39.3-50.5z"></path></svg>
              </a>
            
          </td>
          <td>
            
              <a href="http://www.matholympiad.org.bd/" target="_blank" rel="noopener" aria-label="Visit national MO website for Bangladesh (opens in new tab)"><span class="data-table__label-full">Visit ↗</span><span class="data-table__label-short">↗</span></a>
            
          </td>
          <td class="data-table__hide-mobile data-table__num">
            2005
          </td>
          <td class="data-table__hide-mobile data-table__num">
            22
          </td>
          <td class="data-table__hide-mobile">
            
          </td>
        </tr>
        
        <tr>
          <td>
            <a href="/countries/BGR/" class="data-table__country-cell">
              <img class="data-table__country-flag" src="/assets/images/countries/flags/bgr.svg" alt="">
              <span class="data-table__country-full">Bulgaria</span><span class="data-table__country-iso">BGR</span>
            </a>
          </td>
          <td>
            
              Emil Kolev
            
          </td>
          <td>
            
              <a href="mailto:emilkol@gmail.com" class="js-contact-email" data-email-user="emilkol" data-email-domain="gmail.com" aria-label="Email Emil Kolev" title="Email">
                <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 1024 1024" aria-hidden="true" focusable="false"><path fill="currentColor" d="M928 160H96c-17.7 0-32 14.3-32 32v640c0 17.7 14.3 32 32 32h832c17.7 0 32-14.3 32-32V192c0-17.7-14.3-32-32-32m-40 110.8V792H136V270.8l-27.6-21.5l39.3-50.5l42.8 33.3h643.1l42.8-33.3l39.3 50.5zM833.6 232L512 482L190.4 232l-42.8-33.3l-39.3 50.5l27.6 21.5l341.6 265.6a55.99 55.99 0 0 0 68.7 0L888 270.8l27.6-21.5l-39.3-50.5z"></path></svg>
              </a>
            
          </td>
          <td>
            
              <a href="http://www.math.bas.bg" target="_blank" rel="noopener" aria-label="Visit national MO website for Bulgaria (opens in new tab)"><span class="data-table__label-full">Visit ↗</span><span class="data-table__label-short">↗</span></a>
            
          </td>
          <td class="data-table__hide-mobile data-table__num">
            1959
          </td>
          <td class="data-table__hide-mobile data-table__num">
            67
          </td>
          <td class="data-table__hide-mobile">
            
              1966, 1975
            
          </td>
        </tr>
        
        <tr>
          <td>
            <a href="/countries/BIH/" class="data-table__country-cell">
              <img class="data-table__country-flag" src="/assets/images/countries/flags/bih.svg" alt="">
              <span class="data-table__country-full">Bosnia and Herzegovina</span><span class="data-table__country-iso">BIH</span>
            </a>
          </td>
          <td>
            
              Muharem Avdispahić
            
          </td>
          <td>
            
              <a href="mailto:mavdispa@pmf.unsa.ba" class="js-contact-email" data-email-user="mavdispa" data-email-domain="pmf.unsa.ba" aria-label="Email Muharem Avdispahić" title="Email">
                <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 1024 1024" aria-hidden="true" focusable="false"><path fill="currentColor" d="M928 160H96c-17.7 0-32 14.3-32 32v640c0 17.7 14.3 32 32 32h832c17.7 0 32-14.3 32-32V192c0-17.7-14.3-32-32-32m-40 110.8V792H136V270.8l-27.6-21.5l39.3-50.5l42.8 33.3h643.1l42.8-33.3l39.3 50.5zM833.6 232L512 482L190.4 232l-42.8-33.3l-39.3 50.5l27.6 21.5l341.6 265.6a55.99 55.99 0 0 0 68.7 0L888 270.8l27.6-21.5l-39.3-50.5z"></path></svg>
              </a>
            
          </td>
          <td>
            
          </td>
          <td class="data-table__hide-mobile data-table__num">
            1993
          </td>
          <td class="data-table__hide-mobile data-table__num">
            34
          </td>
          <td class="data-table__hide-mobile">
            
          </td>
        </tr>
        
        <tr>
          <td>
            <a href="/countries/BLR/" class="data-table__country-cell">
              <img class="data-table__country-flag" src="/assets/images/countries/flags/blr.svg" alt="">
              <span class="data-table__country-full">Belarus</span><span class="data-table__country-iso">BLR</span>
            </a>
          </td>
          <td>
            
              David Zmiaikou
            
          </td>
          <td>
            
              <a href="mailto:david.zmiaikou@gmail.com" class="js-contact-email" data-email-user="david.zmiaikou" data-email-domain="gmail.com" aria-label="Email David Zmiaikou" title="Email">
                <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 1024 1024" aria-hidden="true" focusable="false"><path fill="currentColor" d="M928 160H96c-17.7 0-32 14.3-32 32v640c0 17.7 14.3 32 32 32h832c17.7 0 32-14.3 32-32V192c0-17.7-14.3-32-32-32m-40 110.8V792H136V270.8l-27.6-21.5l39.3-50.5l42.8 33.3h643.1l42.8-33.3l39.3 50.5zM833.6 232L512 482L190.4 232l-42.8-33.3l-39.3 50.5l27.6 21.5l341.6 265.6a55.99 55.99 0 0 0 68.7 0L888 270.8l27.6-21.5l-39.3-50.5z"></path></svg>
              </a>
            
          </td>
          <td>
            
          </td>
          <td class="data-table__hide-mobile data-table__num">
            1993
          </td>
          <td class="data-table__hide-mobile data-table__num">
            34
          </td>
          <td class="data-table__hide-mobile">
            
          </td>
        </tr>
        
        <tr>
          <td>
            <a href="/countries/BMU/" class="data-table__country-cell">
              <img class="data-table__country-flag" src="/assets/images/countries/flags/bmu.svg" alt="">
              <span class="data-table__country-full">Bermuda</span><span class="data-table__country-iso">BMU</span>
            </a>
          </td>
          <td>
            
              Kevin Minors
            
          </td>
          <td>
            
              <a href="mailto:hello@maths.bm" class="js-contact-email" data-email-user="hello" data-email-domain="maths.bm" aria-label="Email Kevin Minors" title="Email">
                <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 1024 1024" aria-hidden="true" focusable="false"><path fill="currentColor" d="M928 160H96c-17.7 0-32 14.3-32 32v640c0 17.7 14.3 32 32 32h832c17.7 0 32-14.3 32-32V192c0-17.7-14.3-32-32-32m-40 110.8V792H136V270.8l-27.6-21.5l39.3-50.5l42.8 33.3h643.1l42.8-33.3l39.3 50.5zM833.6 232L512 482L190.4 232l-42.8-33.3l-39.3 50.5l27.6 21.5l341.6 265.6a55.99 55.99 0 0 0 68.7 0L888 270.8l27.6-21.5l-39.3-50.5z"></path></svg>
              </a>
            
          </td>
          <td>
            
              <a href="https://www.maths.bm" target="_blank" rel="noopener" aria-label="Visit national MO website for Bermuda (opens in new tab)"><span class="data-table__label-full">Visit ↗</span><span class="data-table__label-short">↗</span></a>
            
          </td>
          <td class="data-table__hide-mobile data-table__num">
            
          </td>
          <td class="data-table__hide-mobile data-table__num">
            0
          </td>
          <td class="data-table__hide-mobile">
            
          </td>
        </tr>
        
        <tr>
          <td>
            <a href="/countries/BOL/" class="data-table__country-cell">
              <img class="data-table__country-flag" src="/assets/images/countries/flags/bol.svg" alt="">
              <span class="data-table__country-full">Bolivia</span><span class="data-table__country-iso">BOL</span>
            </a>
          </td>
          <td>
            
              Sonia Cordero Cárdenas
            
          </td>
          <td>
            
              <a href="mailto:soniacordero3r@gmail.com" class="js-contact-email" data-email-user="soniacordero3r" data-email-domain="gmail.com" aria-label="Email Sonia Cordero Cárdenas" title="Email">
                <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 1024 1024" aria-hidden="true" focusable="false"><path fill="currentColor" d="M928 160H96c-17.7 0-32 14.3-32 32v640c0 17.7 14.3 32 32 32h832c17.7 0 32-14.3 32-32V192c0-17.7-14.3-32-32-32m-40 110.8V792H136V270.8l-27.6-21.5l39.3-50.5l42.8 33.3h643.1l42.8-33.3l39.3 50.5zM833.6 232L512 482L190.4 232l-42.8-33.3l-39.3 50.5l27.6 21.5l341.6 265.6a55.99 55.99 0 0 0 68.7 0L888 270.8l27.6-21.5l-39.3-50.5z"></path></svg>
              </a>
            
          </td>
          <td>
            
              <a href="https://www.omatbol.org" target="_blank" rel="noopener" aria-label="Visit national MO website for Bolivia (opens in new tab)"><span class="data-table__label-full">Visit ↗</span><span class="data-table__label-short">↗</span></a>
            
          </td>
          <td class="data-table__hide-mobile data-table__num">
            1997
          </td>
          <td class="data-table__hide-mobile data-table__num">
            22
          </td>
          <td class="data-table__hide-mobile">
            
          </td>
        </tr>
        
        <tr>
          <td>
            <a href="/countries/BRA/" class="data-table__country-cell">
              <img class="data-table__country-flag" src="/assets/images/countries/flags/bra.svg" alt="">
              <span class="data-table__country-full">Brazil</span><span class="data-table__country-iso">BRA</span>
            </a>
          </td>
          <td>
            
              Edmilson Luis Rodrigues Motta
            
          </td>
          <td>
            
              <a href="mailto:edmilsonlrm@gmail.com" class="js-contact-email" data-email-user="edmilsonlrm" data-email-domain="gmail.com" aria-label="Email Edmilson Luis Rodrigues Motta" title="Email">
                <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 1024 1024" aria-hidden="true" focusable="false"><path fill="currentColor" d="M928 160H96c-17.7 0-32 14.3-32 32v640c0 17.7 14.3 32 32 32h832c17.7 0 32-14.3 32-32V192c0-17.7-14.3-32-32-32m-40 110.8V792H136V270.8l-27.6-21.5l39.3-50.5l42.8 33.3h643.1l42.8-33.3l39.3 50.5zM833.6 232L512 482L190.4 232l-42.8-33.3l-39.3 50.5l27.6 21.5l341.6 265.6a55.99 55.99 0 0 0 68.7 0L888 270.8l27.6-21.5l-39.3-50.5z"></path></svg>
              </a>
            
          </td>
          <td>
            
              <a href="http://www.obm.org.br/" target="_blank" rel="noopener" aria-label="Visit national MO website for Brazil (opens in new tab)"><span class="data-table__label-full">Visit ↗</span><span class="data-table__label-short">↗</span></a>
            
          </td>
          <td class="data-table__hide-mobile data-table__num">
            1979
          </td>
          <td class="data-table__hide-mobile data-table__num">
            47
          </td>
          <td class="data-table__hide-mobile">
            
              2017
            
          </td>
        </tr>
        
        <tr>
          <td>
            <a href="/countries/BRU/" class="data-table__country-cell">
              <img class="data-table__country-flag" src="/assets/images/countries/flags/bru.svg" alt="">
              <span class="data-table__country-full">Brunei</span><span class="data-table__country-iso">BRU</span>
            </a>
          </td>
          <td>
            
              Syed Rozman bin Haji Syed Abd Rahim
            
          </td>
          <td>
            
              <a href="mailto:rozmansr@hotmail.com" class="js-contact-email" data-email-user="rozmansr" data-email-domain="hotmail.com" aria-label="Email Syed Rozman bin Haji Syed Abd Rahim" title="Email">
                <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 1024 1024" aria-hidden="true" focusable="false"><path fill="currentColor" d="M928 160H96c-17.7 0-32 14.3-32 32v640c0 17.7 14.3 32 32 32h832c17.7 0 32-14.3 32-32V192c0-17.7-14.3-32-32-32m-40 110.8V792H136V270.8l-27.6-21.5l39.3-50.5l42.8 33.3h643.1l42.8-33.3l39.3 50.5zM833.6 232L512 482L190.4 232l-42.8-33.3l-39.3 50.5l27.6 21.5l341.6 265.6a55.99 55.99 0 0 0 68.7 0L888 270.8l27.6-21.5l-39.3-50.5z"></path></svg>
              </a>
            
          </td>
          <td>
            
          </td>
          <td class="data-table__hide-mobile data-table__num">
            2000
          </td>
          <td class="data-table__hide-mobile data-table__num">
            1
          </td>
          <td class="data-table__hide-mobile">
            
          </td>
        </tr>
        
        <tr>
          <td>
            <a href="/countries/BTN/" class="data-table__country-cell">
              <img class="data-table__country-flag" src="/assets/images/countries/flags/btn.svg" alt="">
              <span class="data-table__country-full">Bhutan</span><span class="data-table__country-iso">BTN</span>
            </a>
          </td>
          <td>
            
              Yeshey Lhendup
            
          </td>
          <td>
            
              <a href="mailto:yesheylhendup@moe.gov.bt" class="js-contact-email" data-email-user="yesheylhendup" data-email-domain="moe.gov.bt" aria-label="Email Yeshey Lhendup" title="Email">
                <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 1024 1024" aria-hidden="true" focusable="false"><path fill="currentColor" d="M928 160H96c-17.7 0-32 14.3-32 32v640c0 17.7 14.3 32 32 32h832c17.7 0 32-14.3 32-32V192c0-17.7-14.3-32-32-32m-40 110.8V792H136V270.8l-27.6-21.5l39.3-50.5l42.8 33.3h643.1l42.8-33.3l39.3 50.5zM833.6 232L512 482L190.4 232l-42.8-33.3l-39.3 50.5l27.6 21.5l341.6 265.6a55.99 55.99 0 0 0 68.7 0L888 270.8l27.6-21.5l-39.3-50.5z"></path></svg>
              </a>
            
          </td>
          <td>
            
          </td>
          <td class="data-table__hide-mobile data-table__num">
            2024
          </td>
          <td class="data-table__hide-mobile data-table__num">
            3
          </td>
          <td class="data-table__hide-mobile">
            
          </td>
        </tr>
        
        <tr>
          <td>
            <a href="/countries/BWA/" class="data-table__country-cell">
              <img class="data-table__country-flag" src="/assets/images/countries/flags/bwa.svg" alt="">
              <span class="data-table__country-full">Botswana</span><span class="data-table__country-iso">BWA</span>
            </a>
          </td>
          <td>
            
              Mmoloki Lekhutlile
            
          </td>
          <td>
            
              <a href="mailto:mlekhutlile@gmail.com" class="js-contact-email" data-email-user="mlekhutlile" data-email-domain="gmail.com" aria-label="Email Mmoloki Lekhutlile" title="Email">
                <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 1024 1024" aria-hidden="true" focusable="false"><path fill="currentColor" d="M928 160H96c-17.7 0-32 14.3-32 32v640c0 17.7 14.3 32 32 32h832c17.7 0 32-14.3 32-32V192c0-17.7-14.3-32-32-32m-40 110.8V792H136V270.8l-27.6-21.5l39.3-50.5l42.8 33.3h643.1l42.8-33.3l39.3 50.5zM833.6 232L512 482L190.4 232l-42.8-33.3l-39.3 50.5l27.6 21.5l341.6 265.6a55.99 55.99 0 0 0 68.7 0L888 270.8l27.6-21.5l-39.3-50.5z"></path></svg>
              </a>
            
          </td>
          <td>
            
              <a href="https://mabtrust.co.bw/" target="_blank" rel="noopener" aria-label="Visit national MO website for Botswana (opens in new tab)"><span class="data-table__label-full">Visit ↗</span><span class="data-table__label-short">↗</span></a>
            
          </td>
          <td class="data-table__hide-mobile data-table__num">
            2015
          </td>
          <td class="data-table__hide-mobile data-table__num">
            12
          </td>
          <td class="data-table__hide-mobile">
            
          </td>
        </tr>
        
        <tr>
          <td>
            <a href="/countries/CAN/" class="data-table__country-cell">
              <img class="data-table__country-flag" src="/assets/images/countries/flags/can.svg" alt="">
              <span class="data-table__country-full">Canada</span><span class="data-table__country-iso">CAN</span>
            </a>
          </td>
          <td>
            
              James Rickards
            
          </td>
          <td>
            
              <a href="mailto:imo@cms.math.ca" class="js-contact-email" data-email-user="imo" data-email-domain="cms.math.ca" aria-label="Email James Rickards" title="Email">
                <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 1024 1024" aria-hidden="true" focusable="false"><path fill="currentColor" d="M928 160H96c-17.7 0-32 14.3-32 32v640c0 17.7 14.3 32 32 32h832c17.7 0 32-14.3 32-32V192c0-17.7-14.3-32-32-32m-40 110.8V792H136V270.8l-27.6-21.5l39.3-50.5l42.8 33.3h643.1l42.8-33.3l39.3 50.5zM833.6 232L512 482L190.4 232l-42.8-33.3l-39.3 50.5l27.6 21.5l341.6 265.6a55.99 55.99 0 0 0 68.7 0L888 270.8l27.6-21.5l-39.3-50.5z"></path></svg>
              </a>
            
          </td>
          <td>
            
              <a href="https://cms.math.ca/competitions/cmo/" target="_blank" rel="noopener" aria-label="Visit national MO website for Canada (opens in new tab)"><span class="data-table__label-full">Visit ↗</span><span class="data-table__label-short">↗</span></a>
            
          </td>
          <td class="data-table__hide-mobile data-table__num">
            1981
          </td>
          <td class="data-table__hide-mobile data-table__num">
            46
          </td>
          <td class="data-table__hide-mobile">
            
              1995
            
          </td>
        </tr>
        
        <tr>
          <td>
            <a href="/countries/CHI/" class="data-table__country-cell">
              <img class="data-table__country-flag" src="/assets/images/countries/flags/chi.svg" alt="">
              <span class="data-table__country-full">Chile</span><span class="data-table__country-iso">CHI</span>
            </a>
          </td>
          <td>
            
              Hernan Burgos
            
          </td>
          <td>
            
              <a href="mailto:hernan.burgos@ufrontera.cl" class="js-contact-email" data-email-user="hernan.burgos" data-email-domain="ufrontera.cl" aria-label="Email Hernan Burgos" title="Email">
                <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 1024 1024" aria-hidden="true" focusable="false"><path fill="currentColor" d="M928 160H96c-17.7 0-32 14.3-32 32v640c0 17.7 14.3 32 32 32h832c17.7 0 32-14.3 32-32V192c0-17.7-14.3-32-32-32m-40 110.8V792H136V270.8l-27.6-21.5l39.3-50.5l42.8 33.3h643.1l42.8-33.3l39.3 50.5zM833.6 232L512 482L190.4 232l-42.8-33.3l-39.3 50.5l27.6 21.5l341.6 265.6a55.99 55.99 0 0 0 68.7 0L888 270.8l27.6-21.5l-39.3-50.5z"></path></svg>
              </a>
            
          </td>
          <td>
            
              <a href="http://www.olimpiadadematematica.cl/" target="_blank" rel="noopener" aria-label="Visit national MO website for Chile (opens in new tab)"><span class="data-table__label-full">Visit ↗</span><span class="data-table__label-short">↗</span></a>
            
          </td>
          <td class="data-table__hide-mobile data-table__num">
            1994
          </td>
          <td class="data-table__hide-mobile data-table__num">
            23
          </td>
          <td class="data-table__hide-mobile">
            
          </td>
        </tr>
        
        <tr>
          <td>
            <a href="/countries/CHN/" class="data-table__country-cell">
              <img class="data-table__country-flag" src="/assets/images/countries/flags/chn.svg" alt="">
              <span class="data-table__country-full">People's Republic of China</span><span class="data-table__country-iso">CHN</span>
            </a>
          </td>
          <td>
            
              HUANG Lei
            
          </td>
          <td>
            
              <a href="mailto:leihuang@amss.ac.cn" class="js-contact-email" data-email-user="leihuang" data-email-domain="amss.ac.cn" aria-label="Email HUANG Lei" title="Email">
                <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 1024 1024" aria-hidden="true" focusable="false"><path fill="currentColor" d="M928 160H96c-17.7 0-32 14.3-32 32v640c0 17.7 14.3 32 32 32h832c17.7 0 32-14.3 32-32V192c0-17.7-14.3-32-32-32m-40 110.8V792H136V270.8l-27.6-21.5l39.3-50.5l42.8 33.3h643.1l42.8-33.3l39.3 50.5zM833.6 232L512 482L190.4 232l-42.8-33.3l-39.3 50.5l27.6 21.5l341.6 265.6a55.99 55.99 0 0 0 68.7 0L888 270.8l27.6-21.5l-39.3-50.5z"></path></svg>
              </a>
            
          </td>
          <td>
            
          </td>
          <td class="data-table__hide-mobile data-table__num">
            1985
          </td>
          <td class="data-table__hide-mobile data-table__num">
            41
          </td>
          <td class="data-table__hide-mobile">
            
              1990, 2026
            
          </td>
        </tr>
        
        <tr class="data-table__row--inactive">
          <td>
            <a href="/countries/CIS/" class="data-table__country-cell">
              <img class="data-table__country-flag" src="/assets/images/countries/flags/cis.svg" alt="">
              <span class="data-table__country-full">Commonwealth of Independent States</span><span class="data-table__country-iso">CIS</span>
            </a>
          </td>
          <td>
            
          </td>
          <td>
            
          </td>
          <td>
            
          </td>
          <td class="data-table__hide-mobile data-table__num">
            1992
          </td>
          <td class="data-table__hide-mobile data-table__num">
            1
          </td>
          <td class="data-table__hide-mobile">
            
          </td>
        </tr>
        
        <tr>
          <td>
            <a href="/countries/CIV/" class="data-table__country-cell">
              <img class="data-table__country-flag" src="/assets/images/countries/flags/civ.svg" alt="">
              <span class="data-table__country-full">Ivory Coast</span><span class="data-table__country-iso">CIV</span>
            </a>
          </td>
          <td>
            
              Adama Coulibaly
            
          </td>
          <td>
            
              <a href="mailto:couliba@yahoo.fr" class="js-contact-email" data-email-user="couliba" data-email-domain="yahoo.fr" aria-label="Email Adama Coulibaly" title="Email">
                <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 1024 1024" aria-hidden="true" focusable="false"><path fill="currentColor" d="M928 160H96c-17.7 0-32 14.3-32 32v640c0 17.7 14.3 32 32 32h832c17.7 0 32-14.3 32-32V192c0-17.7-14.3-32-32-32m-40 110.8V792H136V270.8l-27.6-21.5l39.3-50.5l42.8 33.3h643.1l42.8-33.3l39.3 50.5zM833.6 232L512 482L190.4 232l-42.8-33.3l-39.3 50.5l27.6 21.5l341.6 265.6a55.99 55.99 0 0 0 68.7 0L888 270.8l27.6-21.5l-39.3-50.5z"></path></svg>
              </a>
            
          </td>
          <td>
            
          </td>
          <td class="data-table__hide-mobile data-table__num">
            2010
          </td>
          <td class="data-table__hide-mobile data-table__num">
            9
          </td>
          <td class="data-table__hide-mobile">
            
          </td>
        </tr>
        
        <tr>
          <td>
            <a href="/countries/CMR/" class="data-table__country-cell">
              <img class="data-table__country-flag" src="/assets/images/countries/flags/cmr.svg" alt="">
              <span class="data-table__country-full">Cameroon</span><span class="data-table__country-iso">CMR</span>
            </a>
          </td>
          <td>
            
              Joseph Domguia
            
          </td>
          <td>
            
              <a href="mailto:imocmr@gmail.com" class="js-contact-email" data-email-user="imocmr" data-email-domain="gmail.com" aria-label="Email Joseph Domguia" title="Email">
                <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 1024 1024" aria-hidden="true" focusable="false"><path fill="currentColor" d="M928 160H96c-17.7 0-32 14.3-32 32v640c0 17.7 14.3 32 32 32h832c17.7 0 32-14.3 32-32V192c0-17.7-14.3-32-32-32m-40 110.8V792H136V270.8l-27.6-21.5l39.3-50.5l42.8 33.3h643.1l42.8-33.3l39.3 50.5zM833.6 232L512 482L190.4 232l-42.8-33.3l-39.3 50.5l27.6 21.5l341.6 265.6a55.99 55.99 0 0 0 68.7 0L888 270.8l27.6-21.5l-39.3-50.5z"></path></svg>
              </a>
            
          </td>
          <td>
            
              <a href="https://olympiad.cm/" target="_blank" rel="noopener" aria-label="Visit national MO website for Cameroon (opens in new tab)"><span class="data-table__label-full">Visit ↗</span><span class="data-table__label-short">↗</span></a>
            
          </td>
          <td class="data-table__hide-mobile data-table__num">
            2023
          </td>
          <td class="data-table__hide-mobile data-table__num">
            3
          </td>
          <td class="data-table__hide-mobile">
            
          </td>
        </tr>
        
        <tr>
          <td>
            <a href="/countries/COL/" class="data-table__country-cell">
              <img class="data-table__country-flag" src="/assets/images/countries/flags/col.svg" alt="">
              <span class="data-table__country-full">Colombia</span><span class="data-table__country-iso">COL</span>
            </a>
          </td>
          <td>
            
              María Falk Losada
            
          </td>
          <td>
            
              <a href="mailto:mariadelosada@gmail.com" class="js-contact-email" data-email-user="mariadelosada" data-email-domain="gmail.com" aria-label="Email María Falk Losada" title="Email">
                <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 1024 1024" aria-hidden="true" focusable="false"><path fill="currentColor" d="M928 160H96c-17.7 0-32 14.3-32 32v640c0 17.7 14.3 32 32 32h832c17.7 0 32-14.3 32-32V192c0-17.7-14.3-32-32-32m-40 110.8V792H136V270.8l-27.6-21.5l39.3-50.5l42.8 33.3h643.1l42.8-33.3l39.3 50.5zM833.6 232L512 482L190.4 232l-42.8-33.3l-39.3 50.5l27.6 21.5l341.6 265.6a55.99 55.99 0 0 0 68.7 0L888 270.8l27.6-21.5l-39.3-50.5z"></path></svg>
              </a>
            
          </td>
          <td>
            
              <a href="http://oc.uan.edu.co" target="_blank" rel="noopener" aria-label="Visit national MO website for Colombia (opens in new tab)"><span class="data-table__label-full">Visit ↗</span><span class="data-table__label-short">↗</span></a>
            
          </td>
          <td class="data-table__hide-mobile data-table__num">
            1981
          </td>
          <td class="data-table__hide-mobile data-table__num">
            46
          </td>
          <td class="data-table__hide-mobile">
            
              2013
            
          </td>
        </tr>
        
        <tr>
          <td>
            <a href="/countries/CRI/" class="data-table__country-cell">
              <img class="data-table__country-flag" src="/assets/images/countries/flags/cri.svg" alt="">
              <span class="data-table__country-full">Costa Rica</span><span class="data-table__country-iso">CRI</span>
            </a>
          </td>
          <td>
            
              Comisión de las Olimpiadas Costarricenses de Matemáticas
            
          </td>
          <td>
            
              <a href="mailto:olcoma@ucr.ac.cr" class="js-contact-email" data-email-user="olcoma" data-email-domain="ucr.ac.cr" aria-label="Email Comisión de las Olimpiadas Costarricenses de Matemáticas" title="Email">
                <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 1024 1024" aria-hidden="true" focusable="false"><path fill="currentColor" d="M928 160H96c-17.7 0-32 14.3-32 32v640c0 17.7 14.3 32 32 32h832c17.7 0 32-14.3 32-32V192c0-17.7-14.3-32-32-32m-40 110.8V792H136V270.8l-27.6-21.5l39.3-50.5l42.8 33.3h643.1l42.8-33.3l39.3 50.5zM833.6 232L512 482L190.4 232l-42.8-33.3l-39.3 50.5l27.6 21.5l341.6 265.6a55.99 55.99 0 0 0 68.7 0L888 270.8l27.6-21.5l-39.3-50.5z"></path></svg>
              </a>
            
          </td>
          <td>
            
              <a href="http://olcoma.ac.cr/" target="_blank" rel="noopener" aria-label="Visit national MO website for Costa Rica (opens in new tab)"><span class="data-table__label-full">Visit ↗</span><span class="data-table__label-short">↗</span></a>
            
          </td>
          <td class="data-table__hide-mobile data-table__num">
            2005
          </td>
          <td class="data-table__hide-mobile data-table__num">
            22
          </td>
          <td class="data-table__hide-mobile">
            
          </td>
        </tr>
        
        <tr>
          <td>
            <a href="/countries/CUB/" class="data-table__country-cell">
              <img class="data-table__country-flag" src="/assets/images/countries/flags/cub.svg" alt="">
              <span class="data-table__country-full">Cuba</span><span class="data-table__country-iso">CUB</span>
            </a>
          </td>
          <td>
            
              Nelson Tomás Hernandez Reyes
            
          </td>
          <td>
            
              <a href="mailto:nelsonh231059@gmail.com" class="js-contact-email" data-email-user="nelsonh231059" data-email-domain="gmail.com" aria-label="Email Nelson Tomás Hernandez Reyes" title="Email">
                <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 1024 1024" aria-hidden="true" focusable="false"><path fill="currentColor" d="M928 160H96c-17.7 0-32 14.3-32 32v640c0 17.7 14.3 32 32 32h832c17.7 0 32-14.3 32-32V192c0-17.7-14.3-32-32-32m-40 110.8V792H136V270.8l-27.6-21.5l39.3-50.5l42.8 33.3h643.1l42.8-33.3l39.3 50.5zM833.6 232L512 482L190.4 232l-42.8-33.3l-39.3 50.5l27.6 21.5l341.6 265.6a55.99 55.99 0 0 0 68.7 0L888 270.8l27.6-21.5l-39.3-50.5z"></path></svg>
              </a>
            
          </td>
          <td>
            
          </td>
          <td class="data-table__hide-mobile data-table__num">
            1971
          </td>
          <td class="data-table__hide-mobile data-table__num">
            48
          </td>
          <td class="data-table__hide-mobile">
            
              1987
            
          </td>
        </tr>
        
        <tr>
          <td>
            <a href="/countries/CYP/" class="data-table__country-cell">
              <img class="data-table__country-flag" src="/assets/images/countries/flags/cyp.svg" alt="">
              <span class="data-table__country-full">Cyprus</span><span class="data-table__country-iso">CYP</span>
            </a>
          </td>
          <td>
            
              Gregory Makrides
            
          </td>
          <td>
            
              <a href="mailto:makrides.g@eaecnet.com" class="js-contact-email" data-email-user="makrides.g" data-email-domain="eaecnet.com" aria-label="Email Gregory Makrides" title="Email">
                <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 1024 1024" aria-hidden="true" focusable="false"><path fill="currentColor" d="M928 160H96c-17.7 0-32 14.3-32 32v640c0 17.7 14.3 32 32 32h832c17.7 0 32-14.3 32-32V192c0-17.7-14.3-32-32-32m-40 110.8V792H136V270.8l-27.6-21.5l39.3-50.5l42.8 33.3h643.1l42.8-33.3l39.3 50.5zM833.6 232L512 482L190.4 232l-42.8-33.3l-39.3 50.5l27.6 21.5l341.6 265.6a55.99 55.99 0 0 0 68.7 0L888 270.8l27.6-21.5l-39.3-50.5z"></path></svg>
              </a>
            
          </td>
          <td>
            
              <a href="http://www.cms.org.cy" target="_blank" rel="noopener" aria-label="Visit national MO website for Cyprus (opens in new tab)"><span class="data-table__label-full">Visit ↗</span><span class="data-table__label-short">↗</span></a>
            
          </td>
          <td class="data-table__hide-mobile data-table__num">
            1984
          </td>
          <td class="data-table__hide-mobile data-table__num">
            42
          </td>
          <td class="data-table__hide-mobile">
            
          </td>
        </tr>
        
        <tr>
          <td>
            <a href="/countries/CZE/" class="data-table__country-cell">
              <img class="data-table__country-flag" src="/assets/images/countries/flags/cze.svg" alt="">
              <span class="data-table__country-full">Czech Republic</span><span class="data-table__country-iso">CZE</span>
            </a>
          </td>
          <td>
            
              Pavel Calábek
            
          </td>
          <td>
            
              <a href="mailto:pavel.calabek@upol.cz" class="js-contact-email" data-email-user="pavel.calabek" data-email-domain="upol.cz" aria-label="Email Pavel Calábek" title="Email">
                <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 1024 1024" aria-hidden="true" focusable="false"><path fill="currentColor" d="M928 160H96c-17.7 0-32 14.3-32 32v640c0 17.7 14.3 32 32 32h832c17.7 0 32-14.3 32-32V192c0-17.7-14.3-32-32-32m-40 110.8V792H136V270.8l-27.6-21.5l39.3-50.5l42.8 33.3h643.1l42.8-33.3l39.3 50.5zM833.6 232L512 482L190.4 232l-42.8-33.3l-39.3 50.5l27.6 21.5l341.6 265.6a55.99 55.99 0 0 0 68.7 0L888 270.8l27.6-21.5l-39.3-50.5z"></path></svg>
              </a>
            
          </td>
          <td>
            
              <a href="http://www.matematickaolympiada.cz/" target="_blank" rel="noopener" aria-label="Visit national MO website for Czech Republic (opens in new tab)"><span class="data-table__label-full">Visit ↗</span><span class="data-table__label-short">↗</span></a>
            
          </td>
          <td class="data-table__hide-mobile data-table__num">
            1993
          </td>
          <td class="data-table__hide-mobile data-table__num">
            34
          </td>
          <td class="data-table__hide-mobile">
            
          </td>
        </tr>
        
        <tr class="data-table__row--inactive">
          <td>
            <a href="/countries/CZS/" class="data-table__country-cell">
              <img class="data-table__country-flag" src="/assets/images/countries/flags/czs.svg" alt="">
              <span class="data-table__country-full">Czechoslovakia</span><span class="data-table__country-iso">CZS</span>
            </a>
          </td>
          <td>
            
          </td>
          <td>
            
          </td>
          <td>
            
          </td>
          <td class="data-table__hide-mobile data-table__num">
            1959
          </td>
          <td class="data-table__hide-mobile data-table__num">
            33
          </td>
          <td class="data-table__hide-mobile">
            
              1962, 1971, 1984
            
          </td>
        </tr>
        
        <tr>
          <td>
            <a href="/countries/DEN/" class="data-table__country-cell">
              <img class="data-table__country-flag" src="/assets/images/countries/flags/den.svg" alt="">
              <span class="data-table__country-full">Denmark</span><span class="data-table__country-iso">DEN</span>
            </a>
          </td>
          <td>
            
              Kirsten Rosenkilde
            
          </td>
          <td>
            
              <a href="mailto:kr@georgmohr.dk" class="js-contact-email" data-email-user="kr" data-email-domain="georgmohr.dk" aria-label="Email Kirsten Rosenkilde" title="Email">
                <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 1024 1024" aria-hidden="true" focusable="false"><path fill="currentColor" d="M928 160H96c-17.7 0-32 14.3-32 32v640c0 17.7 14.3 32 32 32h832c17.7 0 32-14.3 32-32V192c0-17.7-14.3-32-32-32m-40 110.8V792H136V270.8l-27.6-21.5l39.3-50.5l42.8 33.3h643.1l42.8-33.3l39.3 50.5zM833.6 232L512 482L190.4 232l-42.8-33.3l-39.3 50.5l27.6 21.5l341.6 265.6a55.99 55.99 0 0 0 68.7 0L888 270.8l27.6-21.5l-39.3-50.5z"></path></svg>
              </a>
            
          </td>
          <td>
            
              <a href="http://www.georgmohr.dk/" target="_blank" rel="noopener" aria-label="Visit national MO website for Denmark (opens in new tab)"><span class="data-table__label-full">Visit ↗</span><span class="data-table__label-short">↗</span></a>
            
          </td>
          <td class="data-table__hide-mobile data-table__num">
            1991
          </td>
          <td class="data-table__hide-mobile data-table__num">
            36
          </td>
          <td class="data-table__hide-mobile">
            
          </td>
        </tr>
        
        <tr>
          <td>
            <a href="/countries/DOM/" class="data-table__country-cell">
              <img class="data-table__country-flag" src="/assets/images/countries/flags/dom.svg" alt="">
              <span class="data-table__country-full">Dominican Republic</span><span class="data-table__country-iso">DOM</span>
            </a>
          </td>
          <td>
            
              Zulaicka M. Guzmán G.
            
          </td>
          <td>
            
              <a href="mailto:zulaicka.guzman@minerd.gob.do" class="js-contact-email" data-email-user="zulaicka.guzman" data-email-domain="minerd.gob.do" aria-label="Email Zulaicka M. Guzmán G." title="Email">
                <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 1024 1024" aria-hidden="true" focusable="false"><path fill="currentColor" d="M928 160H96c-17.7 0-32 14.3-32 32v640c0 17.7 14.3 32 32 32h832c17.7 0 32-14.3 32-32V192c0-17.7-14.3-32-32-32m-40 110.8V792H136V270.8l-27.6-21.5l39.3-50.5l42.8 33.3h643.1l42.8-33.3l39.3 50.5zM833.6 232L512 482L190.4 232l-42.8-33.3l-39.3 50.5l27.6 21.5l341.6 265.6a55.99 55.99 0 0 0 68.7 0L888 270.8l27.6-21.5l-39.3-50.5z"></path></svg>
              </a>
            
          </td>
          <td>
            
          </td>
          <td class="data-table__hide-mobile data-table__num">
            2019
          </td>
          <td class="data-table__hide-mobile data-table__num">
            6
          </td>
          <td class="data-table__hide-mobile">
            
          </td>
        </tr>
        
        <tr>
          <td>
            <a href="/countries/ECU/" class="data-table__country-cell">
              <img class="data-table__country-flag" src="/assets/images/countries/flags/ecu.svg" alt="">
              <span class="data-table__country-full">Ecuador</span><span class="data-table__country-iso">ECU</span>
            </a>
          </td>
          <td>
            
              Pablo Serrano Santos
            
          </td>
          <td>
            
              <a href="mailto:info@omec-mat.org" class="js-contact-email" data-email-user="info" data-email-domain="omec-mat.org" aria-label="Email Pablo Serrano Santos" title="Email">
                <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 1024 1024" aria-hidden="true" focusable="false"><path fill="currentColor" d="M928 160H96c-17.7 0-32 14.3-32 32v640c0 17.7 14.3 32 32 32h832c17.7 0 32-14.3 32-32V192c0-17.7-14.3-32-32-32m-40 110.8V792H136V270.8l-27.6-21.5l39.3-50.5l42.8 33.3h643.1l42.8-33.3l39.3 50.5zM833.6 232L512 482L190.4 232l-42.8-33.3l-39.3 50.5l27.6 21.5l341.6 265.6a55.99 55.99 0 0 0 68.7 0L888 270.8l27.6-21.5l-39.3-50.5z"></path></svg>
              </a>
            
          </td>
          <td>
            
              <a href="https://omec-mat.org/" target="_blank" rel="noopener" aria-label="Visit national MO website for Ecuador (opens in new tab)"><span class="data-table__label-full">Visit ↗</span><span class="data-table__label-short">↗</span></a>
            
          </td>
          <td class="data-table__hide-mobile data-table__num">
            1988
          </td>
          <td class="data-table__hide-mobile data-table__num">
            28
          </td>
          <td class="data-table__hide-mobile">
            
          </td>
        </tr>
        
        <tr>
          <td>
            <a href="/countries/EGY/" class="data-table__country-cell">
              <img class="data-table__country-flag" src="/assets/images/countries/flags/egy.svg" alt="">
              <span class="data-table__country-full">Egypt</span><span class="data-table__country-iso">EGY</span>
            </a>
          </td>
          <td>
            
              Saeed Youssef
            
          </td>
          <td>
            
              <a href="mailto:saeed.youssef.2005@gmail.com" class="js-contact-email" data-email-user="saeed.youssef.2005" data-email-domain="gmail.com" aria-label="Email Saeed Youssef" title="Email">
                <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 1024 1024" aria-hidden="true" focusable="false"><path fill="currentColor" d="M928 160H96c-17.7 0-32 14.3-32 32v640c0 17.7 14.3 32 32 32h832c17.7 0 32-14.3 32-32V192c0-17.7-14.3-32-32-32m-40 110.8V792H136V270.8l-27.6-21.5l39.3-50.5l42.8 33.3h643.1l42.8-33.3l39.3 50.5zM833.6 232L512 482L190.4 232l-42.8-33.3l-39.3 50.5l27.6 21.5l341.6 265.6a55.99 55.99 0 0 0 68.7 0L888 270.8l27.6-21.5l-39.3-50.5z"></path></svg>
              </a>
            
          </td>
          <td>
            
          </td>
          <td class="data-table__hide-mobile data-table__num">
            2016
          </td>
          <td class="data-table__hide-mobile data-table__num">
            5
          </td>
          <td class="data-table__hide-mobile">
            
          </td>
        </tr>
        
        <tr>
          <td>
            <a href="/countries/ESP/" class="data-table__country-cell">
              <img class="data-table__country-flag" src="/assets/images/countries/flags/esp.svg" alt="">
              <span class="data-table__country-full">Spain</span><span class="data-table__country-iso">ESP</span>
            </a>
          </td>
          <td>
            
              María Gaspar
            
          </td>
          <td>
            
              <a href="mailto:mgaspar@ucm.es" class="js-contact-email" data-email-user="mgaspar" data-email-domain="ucm.es" aria-label="Email María Gaspar" title="Email">
                <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 1024 1024" aria-hidden="true" focusable="false"><path fill="currentColor" d="M928 160H96c-17.7 0-32 14.3-32 32v640c0 17.7 14.3 32 32 32h832c17.7 0 32-14.3 32-32V192c0-17.7-14.3-32-32-32m-40 110.8V792H136V270.8l-27.6-21.5l39.3-50.5l42.8 33.3h643.1l42.8-33.3l39.3 50.5zM833.6 232L512 482L190.4 232l-42.8-33.3l-39.3 50.5l27.6 21.5l341.6 265.6a55.99 55.99 0 0 0 68.7 0L888 270.8l27.6-21.5l-39.3-50.5z"></path></svg>
              </a>
            
          </td>
          <td>
            
              <a href="https://www.rsme.es/olimpiada-matematica-espanola" target="_blank" rel="noopener" aria-label="Visit national MO website for Spain (opens in new tab)"><span class="data-table__label-full">Visit ↗</span><span class="data-table__label-short">↗</span></a>
            
          </td>
          <td class="data-table__hide-mobile data-table__num">
            1983
          </td>
          <td class="data-table__hide-mobile data-table__num">
            44
          </td>
          <td class="data-table__hide-mobile">
            
              2008
            
          </td>
        </tr>
        
        <tr>
          <td>
            <a href="/countries/EST/" class="data-table__country-cell">
              <img class="data-table__country-flag" src="/assets/images/countries/flags/est.svg" alt="">
              <span class="data-table__country-full">Estonia</span><span class="data-table__country-iso">EST</span>
            </a>
          </td>
          <td>
            
              Oleg Košik
            
          </td>
          <td>
            
              <a href="mailto:oleg.koshik@ut.ee" class="js-contact-email" data-email-user="oleg.koshik" data-email-domain="ut.ee" aria-label="Email Oleg Košik" title="Email">
                <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 1024 1024" aria-hidden="true" focusable="false"><path fill="currentColor" d="M928 160H96c-17.7 0-32 14.3-32 32v640c0 17.7 14.3 32 32 32h832c17.7 0 32-14.3 32-32V192c0-17.7-14.3-32-32-32m-40 110.8V792H136V270.8l-27.6-21.5l39.3-50.5l42.8 33.3h643.1l42.8-33.3l39.3 50.5zM833.6 232L512 482L190.4 232l-42.8-33.3l-39.3 50.5l27.6 21.5l341.6 265.6a55.99 55.99 0 0 0 68.7 0L888 270.8l27.6-21.5l-39.3-50.5z"></path></svg>
              </a>
            
          </td>
          <td>
            
              <a href="http://www.math.olympiaadid.ut.ee/" target="_blank" rel="noopener" aria-label="Visit national MO website for Estonia (opens in new tab)"><span class="data-table__label-full">Visit ↗</span><span class="data-table__label-short">↗</span></a>
            
          </td>
          <td class="data-table__hide-mobile data-table__num">
            1993
          </td>
          <td class="data-table__hide-mobile data-table__num">
            34
          </td>
          <td class="data-table__hide-mobile">
            
          </td>
        </tr>
        
        <tr>
          <td>
            <a href="/countries/ETH/" class="data-table__country-cell">
              <img class="data-table__country-flag" src="/assets/images/countries/flags/eth.svg" alt="">
              <span class="data-table__country-full">Ethiopia</span><span class="data-table__country-iso">ETH</span>
            </a>
          </td>
          <td>
            
              Abdu Mohammed Seid
            
          </td>
          <td>
            
              <a href="mailto:abdum442@yahoo.com" class="js-contact-email" data-email-user="abdum442" data-email-domain="yahoo.com" aria-label="Email Abdu Mohammed Seid" title="Email">
                <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 1024 1024" aria-hidden="true" focusable="false"><path fill="currentColor" d="M928 160H96c-17.7 0-32 14.3-32 32v640c0 17.7 14.3 32 32 32h832c17.7 0 32-14.3 32-32V192c0-17.7-14.3-32-32-32m-40 110.8V792H136V270.8l-27.6-21.5l39.3-50.5l42.8 33.3h643.1l42.8-33.3l39.3 50.5zM833.6 232L512 482L190.4 232l-42.8-33.3l-39.3 50.5l27.6 21.5l341.6 265.6a55.99 55.99 0 0 0 68.7 0L888 270.8l27.6-21.5l-39.3-50.5z"></path></svg>
              </a>
            
          </td>
          <td>
            
          </td>
          <td class="data-table__hide-mobile data-table__num">
            
          </td>
          <td class="data-table__hide-mobile data-table__num">
            0
          </td>
          <td class="data-table__hide-mobile">
            
          </td>
        </tr>
        
        <tr>
          <td>
            <a href="/countries/FIN/" class="data-table__country-cell">
              <img class="data-table__country-flag" src="/assets/images/countries/flags/fin.svg" alt="">
              <span class="data-table__country-full">Finland</span><span class="data-table__country-iso">FIN</span>
            </a>
          </td>
          <td>
            
              Anne-Maria Ernvall-Hytönen
            
          </td>
          <td>
            
              <a href="mailto:anne-maria.ernvall-hytonen@helsinki.fi" class="js-contact-email" data-email-user="anne-maria.ernvall-hytonen" data-email-domain="helsinki.fi" aria-label="Email Anne-Maria Ernvall-Hytönen" title="Email">
                <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 1024 1024" aria-hidden="true" focusable="false"><path fill="currentColor" d="M928 160H96c-17.7 0-32 14.3-32 32v640c0 17.7 14.3 32 32 32h832c17.7 0 32-14.3 32-32V192c0-17.7-14.3-32-32-32m-40 110.8V792H136V270.8l-27.6-21.5l39.3-50.5l42.8 33.3h643.1l42.8-33.3l39.3 50.5zM833.6 232L512 482L190.4 232l-42.8-33.3l-39.3 50.5l27.6 21.5l341.6 265.6a55.99 55.99 0 0 0 68.7 0L888 270.8l27.6-21.5l-39.3-50.5z"></path></svg>
              </a>
            
          </td>
          <td>
            
              <a href="http://matematiikkakilpailut.fi/" target="_blank" rel="noopener" aria-label="Visit national MO website for Finland (opens in new tab)"><span class="data-table__label-full">Visit ↗</span><span class="data-table__label-short">↗</span></a>
            
          </td>
          <td class="data-table__hide-mobile data-table__num">
            1965
          </td>
          <td class="data-table__hide-mobile data-table__num">
            53
          </td>
          <td class="data-table__hide-mobile">
            
              1985
            
          </td>
        </tr>
        
        <tr>
          <td>
            <a href="/countries/FRA/" class="data-table__country-cell">
              <img class="data-table__country-flag" src="/assets/images/countries/flags/fra.svg" alt="">
              <span class="data-table__country-full">France</span><span class="data-table__country-iso">FRA</span>
            </a>
          </td>
          <td>
            
              Vincent Jugé et Johan Yebbou
            
          </td>
          <td>
            
              <a href="mailto:vincent.juge@animath.fr" class="js-contact-email" data-email-user="vincent.juge" data-email-domain="animath.fr" aria-label="Email Vincent Jugé et Johan Yebbou" title="Email">
                <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 1024 1024" aria-hidden="true" focusable="false"><path fill="currentColor" d="M928 160H96c-17.7 0-32 14.3-32 32v640c0 17.7 14.3 32 32 32h832c17.7 0 32-14.3 32-32V192c0-17.7-14.3-32-32-32m-40 110.8V792H136V270.8l-27.6-21.5l39.3-50.5l42.8 33.3h643.1l42.8-33.3l39.3 50.5zM833.6 232L512 482L190.4 232l-42.8-33.3l-39.3 50.5l27.6 21.5l341.6 265.6a55.99 55.99 0 0 0 68.7 0L888 270.8l27.6-21.5l-39.3-50.5z"></path></svg>
              </a>
            
          </td>
          <td>
            
              <a href="http://www.animath.fr/" target="_blank" rel="noopener" aria-label="Visit national MO website for France (opens in new tab)"><span class="data-table__label-full">Visit ↗</span><span class="data-table__label-short">↗</span></a>
            
          </td>
          <td class="data-table__hide-mobile data-table__num">
            1967
          </td>
          <td class="data-table__hide-mobile data-table__num">
            57
          </td>
          <td class="data-table__hide-mobile">
            
              1983
            
          </td>
        </tr>
        
        <tr class="data-table__row--inactive">
          <td>
            <a href="/countries/GDR/" class="data-table__country-cell">
              <img class="data-table__country-flag" src="/assets/images/countries/flags/gdr.svg" alt="">
              <span class="data-table__country-full">German Democratic Republic</span><span class="data-table__country-iso">GDR</span>
            </a>
          </td>
          <td>
            
          </td>
          <td>
            
          </td>
          <td>
            
          </td>
          <td class="data-table__hide-mobile data-table__num">
            1959
          </td>
          <td class="data-table__hide-mobile data-table__num">
            29
          </td>
          <td class="data-table__hide-mobile">
            
              1965, 1974
            
          </td>
        </tr>
        
        <tr>
          <td>
            <a href="/countries/GEO/" class="data-table__country-cell">
              <img class="data-table__country-flag" src="/assets/images/countries/flags/geo.svg" alt="">
              <span class="data-table__country-full">Georgia</span><span class="data-table__country-iso">GEO</span>
            </a>
          </td>
          <td>
            
              George Chelidze
            
          </td>
          <td>
            
              <a href="mailto:giorgi.chelidze@kiu.edu.ge" class="js-contact-email" data-email-user="giorgi.chelidze" data-email-domain="kiu.edu.ge" aria-label="Email George Chelidze" title="Email">
                <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 1024 1024" aria-hidden="true" focusable="false"><path fill="currentColor" d="M928 160H96c-17.7 0-32 14.3-32 32v640c0 17.7 14.3 32 32 32h832c17.7 0 32-14.3 32-32V192c0-17.7-14.3-32-32-32m-40 110.8V792H136V270.8l-27.6-21.5l39.3-50.5l42.8 33.3h643.1l42.8-33.3l39.3 50.5zM833.6 232L512 482L190.4 232l-42.8-33.3l-39.3 50.5l27.6 21.5l341.6 265.6a55.99 55.99 0 0 0 68.7 0L888 270.8l27.6-21.5l-39.3-50.5z"></path></svg>
              </a>
            
          </td>
          <td>
            
          </td>
          <td class="data-table__hide-mobile data-table__num">
            1993
          </td>
          <td class="data-table__hide-mobile data-table__num">
            34
          </td>
          <td class="data-table__hide-mobile">
            
          </td>
        </tr>
        
        <tr>
          <td>
            <a href="/countries/GER/" class="data-table__country-cell">
              <img class="data-table__country-flag" src="/assets/images/countries/flags/ger.svg" alt="">
              <span class="data-table__country-full">Germany</span><span class="data-table__country-iso">GER</span>
            </a>
          </td>
          <td>
            
              Uwe Leck
            
          </td>
          <td>
            
              <a href="mailto:uwe.leck@uni-flensburg.de" class="js-contact-email" data-email-user="uwe.leck" data-email-domain="uni-flensburg.de" aria-label="Email Uwe Leck" title="Email">
                <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 1024 1024" aria-hidden="true" focusable="false"><path fill="currentColor" d="M928 160H96c-17.7 0-32 14.3-32 32v640c0 17.7 14.3 32 32 32h832c17.7 0 32-14.3 32-32V192c0-17.7-14.3-32-32-32m-40 110.8V792H136V270.8l-27.6-21.5l39.3-50.5l42.8 33.3h643.1l42.8-33.3l39.3 50.5zM833.6 232L512 482L190.4 232l-42.8-33.3l-39.3 50.5l27.6 21.5l341.6 265.6a55.99 55.99 0 0 0 68.7 0L888 270.8l27.6-21.5l-39.3-50.5z"></path></svg>
              </a>
            
          </td>
          <td>
            
              <a href="https://www.mathe-wettbewerbe.de/" target="_blank" rel="noopener" aria-label="Visit national MO website for Germany (opens in new tab)"><span class="data-table__label-full">Visit ↗</span><span class="data-table__label-short">↗</span></a>
            
          </td>
          <td class="data-table__hide-mobile data-table__num">
            1977
          </td>
          <td class="data-table__hide-mobile data-table__num">
            49
          </td>
          <td class="data-table__hide-mobile">
            
              1989, 2009
            
          </td>
        </tr>
        
        <tr>
          <td>
            <a href="/countries/GHA/" class="data-table__country-cell">
              <img class="data-table__country-flag" src="/assets/images/countries/flags/gha.svg" alt="">
              <span class="data-table__country-full">Ghana</span><span class="data-table__country-iso">GHA</span>
            </a>
          </td>
          <td>
            
              Joel M. Dogoe
            
          </td>
          <td>
            
              <a href="mailto:admin@misemaths.org" class="js-contact-email" data-email-user="admin" data-email-domain="misemaths.org" aria-label="Email Joel M. Dogoe" title="Email">
                <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 1024 1024" aria-hidden="true" focusable="false"><path fill="currentColor" d="M928 160H96c-17.7 0-32 14.3-32 32v640c0 17.7 14.3 32 32 32h832c17.7 0 32-14.3 32-32V192c0-17.7-14.3-32-32-32m-40 110.8V792H136V270.8l-27.6-21.5l39.3-50.5l42.8 33.3h643.1l42.8-33.3l39.3 50.5zM833.6 232L512 482L190.4 232l-42.8-33.3l-39.3 50.5l27.6 21.5l341.6 265.6a55.99 55.99 0 0 0 68.7 0L888 270.8l27.6-21.5l-39.3-50.5z"></path></svg>
              </a>
            
          </td>
          <td>
            
          </td>
          <td class="data-table__hide-mobile data-table__num">
            2014
          </td>
          <td class="data-table__hide-mobile data-table__num">
            13
          </td>
          <td class="data-table__hide-mobile">
            
          </td>
        </tr>
        
        <tr>
          <td>
            <a href="/countries/GMB/" class="data-table__country-cell">
              <img class="data-table__country-flag" src="/assets/images/countries/flags/gmb.svg" alt="">
              <span class="data-table__country-full">Gambia</span><span class="data-table__country-iso">GMB</span>
            </a>
          </td>
          <td>
            
              Kolapo I. Abdul
            
          </td>
          <td>
            
              <a href="mailto:youthcarefd@yahoo.com" class="js-contact-email" data-email-user="youthcarefd" data-email-domain="yahoo.com" aria-label="Email Kolapo I. Abdul" title="Email">
                <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 1024 1024" aria-hidden="true" focusable="false"><path fill="currentColor" d="M928 160H96c-17.7 0-32 14.3-32 32v640c0 17.7 14.3 32 32 32h832c17.7 0 32-14.3 32-32V192c0-17.7-14.3-32-32-32m-40 110.8V792H136V270.8l-27.6-21.5l39.3-50.5l42.8 33.3h643.1l42.8-33.3l39.3 50.5zM833.6 232L512 482L190.4 232l-42.8-33.3l-39.3 50.5l27.6 21.5l341.6 265.6a55.99 55.99 0 0 0 68.7 0L888 270.8l27.6-21.5l-39.3-50.5z"></path></svg>
              </a>
            
          </td>
          <td>
            
          </td>
          <td class="data-table__hide-mobile data-table__num">
            2014
          </td>
          <td class="data-table__hide-mobile data-table__num">
            1
          </td>
          <td class="data-table__hide-mobile">
            
          </td>
        </tr>
        
        <tr>
          <td>
            <a href="/countries/GTM/" class="data-table__country-cell">
              <img class="data-table__country-flag" src="/assets/images/countries/flags/gtm.svg" alt="">
              <span class="data-table__country-full">Guatemala</span><span class="data-table__country-iso">GTM</span>
            </a>
          </td>
          <td>
            
              José Carlos Bonilla
            
          </td>
          <td>
            
              <a href="mailto:jcbonilla14@gmail.com" class="js-contact-email" data-email-user="jcbonilla14" data-email-domain="gmail.com" aria-label="Email José Carlos Bonilla" title="Email">
                <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 1024 1024" aria-hidden="true" focusable="false"><path fill="currentColor" d="M928 160H96c-17.7 0-32 14.3-32 32v640c0 17.7 14.3 32 32 32h832c17.7 0 32-14.3 32-32V192c0-17.7-14.3-32-32-32m-40 110.8V792H136V270.8l-27.6-21.5l39.3-50.5l42.8 33.3h643.1l42.8-33.3l39.3 50.5zM833.6 232L512 482L190.4 232l-42.8-33.3l-39.3 50.5l27.6 21.5l341.6 265.6a55.99 55.99 0 0 0 68.7 0L888 270.8l27.6-21.5l-39.3-50.5z"></path></svg>
              </a>
            
          </td>
          <td>
            
          </td>
          <td class="data-table__hide-mobile data-table__num">
            1997
          </td>
          <td class="data-table__hide-mobile data-table__num">
            15
          </td>
          <td class="data-table__hide-mobile">
            
          </td>
        </tr>
        
        <tr>
          <td>
            <a href="/countries/HEL/" class="data-table__country-cell">
              <img class="data-table__country-flag" src="/assets/images/countries/flags/hel.svg" alt="">
              <span class="data-table__country-full">Greece</span><span class="data-table__country-iso">HEL</span>
            </a>
          </td>
          <td>
            
              Anargyros Fellouris
            
          </td>
          <td>
            
              <a href="mailto:info@hms.gr" class="js-contact-email" data-email-user="info" data-email-domain="hms.gr" aria-label="Email Anargyros Fellouris" title="Email">
                <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 1024 1024" aria-hidden="true" focusable="false"><path fill="currentColor" d="M928 160H96c-17.7 0-32 14.3-32 32v640c0 17.7 14.3 32 32 32h832c17.7 0 32-14.3 32-32V192c0-17.7-14.3-32-32-32m-40 110.8V792H136V270.8l-27.6-21.5l39.3-50.5l42.8 33.3h643.1l42.8-33.3l39.3 50.5zM833.6 232L512 482L190.4 232l-42.8-33.3l-39.3 50.5l27.6 21.5l341.6 265.6a55.99 55.99 0 0 0 68.7 0L888 270.8l27.6-21.5l-39.3-50.5z"></path></svg>
              </a>
            
          </td>
          <td>
            
              <a href="http://www.hms.gr" target="_blank" rel="noopener" aria-label="Visit national MO website for Greece (opens in new tab)"><span class="data-table__label-full">Visit ↗</span><span class="data-table__label-short">↗</span></a>
            
          </td>
          <td class="data-table__hide-mobile data-table__num">
            1975
          </td>
          <td class="data-table__hide-mobile data-table__num">
            48
          </td>
          <td class="data-table__hide-mobile">
            
              2004
            
          </td>
        </tr>
        
        <tr>
          <td>
            <a href="/countries/HKG/" class="data-table__country-cell">
              <img class="data-table__country-flag" src="/assets/images/countries/flags/hkg.svg" alt="">
              <span class="data-table__country-full">Hong Kong</span><span class="data-table__country-iso">HKG</span>
            </a>
          </td>
          <td>
            
              Lander Lam
            
          </td>
          <td>
            
              <a href="mailto:ccdoge@edb.gov.hk" class="js-contact-email" data-email-user="ccdoge" data-email-domain="edb.gov.hk" aria-label="Email Lander Lam" title="Email">
                <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 1024 1024" aria-hidden="true" focusable="false"><path fill="currentColor" d="M928 160H96c-17.7 0-32 14.3-32 32v640c0 17.7 14.3 32 32 32h832c17.7 0 32-14.3 32-32V192c0-17.7-14.3-32-32-32m-40 110.8V792H136V270.8l-27.6-21.5l39.3-50.5l42.8 33.3h643.1l42.8-33.3l39.3 50.5zM833.6 232L512 482L190.4 232l-42.8-33.3l-39.3 50.5l27.6 21.5l341.6 265.6a55.99 55.99 0 0 0 68.7 0L888 270.8l27.6-21.5l-39.3-50.5z"></path></svg>
              </a>
            
          </td>
          <td>
            
          </td>
          <td class="data-table__hide-mobile data-table__num">
            1988
          </td>
          <td class="data-table__hide-mobile data-table__num">
            39
          </td>
          <td class="data-table__hide-mobile">
            
              1994, 2016
            
          </td>
        </tr>
        
        <tr>
          <td>
            <a href="/countries/HND/" class="data-table__country-cell">
              <img class="data-table__country-flag" src="/assets/images/countries/flags/hnd.svg" alt="">
              <span class="data-table__country-full">Honduras</span><span class="data-table__country-iso">HND</span>
            </a>
          </td>
          <td>
            
              Comité Hondureño de Olimpiadas Matemáticas
            
          </td>
          <td>
            
              <a href="mailto:olimpiadamatematica.honduras@gmail.com" class="js-contact-email" data-email-user="olimpiadamatematica.honduras" data-email-domain="gmail.com" aria-label="Email Comité Hondureño de Olimpiadas Matemáticas" title="Email">
                <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 1024 1024" aria-hidden="true" focusable="false"><path fill="currentColor" d="M928 160H96c-17.7 0-32 14.3-32 32v640c0 17.7 14.3 32 32 32h832c17.7 0 32-14.3 32-32V192c0-17.7-14.3-32-32-32m-40 110.8V792H136V270.8l-27.6-21.5l39.3-50.5l42.8 33.3h643.1l42.8-33.3l39.3 50.5zM833.6 232L512 482L190.4 232l-42.8-33.3l-39.3 50.5l27.6 21.5l341.6 265.6a55.99 55.99 0 0 0 68.7 0L888 270.8l27.6-21.5l-39.3-50.5z"></path></svg>
              </a>
            
          </td>
          <td>
            
          </td>
          <td class="data-table__hide-mobile data-table__num">
            2008
          </td>
          <td class="data-table__hide-mobile data-table__num">
            16
          </td>
          <td class="data-table__hide-mobile">
            
          </td>
        </tr>
        
        <tr>
          <td>
            <a href="/countries/HRV/" class="data-table__country-cell">
              <img class="data-table__country-flag" src="/assets/images/countries/flags/hrv.svg" alt="">
              <span class="data-table__country-full">Croatia</span><span class="data-table__country-iso">HRV</span>
            </a>
          </td>
          <td>
            
              Matija Bašić
            
          </td>
          <td>
            
              <a href="mailto:mbasic@math.hr" class="js-contact-email" data-email-user="mbasic" data-email-domain="math.hr" aria-label="Email Matija Bašić" title="Email">
                <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 1024 1024" aria-hidden="true" focusable="false"><path fill="currentColor" d="M928 160H96c-17.7 0-32 14.3-32 32v640c0 17.7 14.3 32 32 32h832c17.7 0 32-14.3 32-32V192c0-17.7-14.3-32-32-32m-40 110.8V792H136V270.8l-27.6-21.5l39.3-50.5l42.8 33.3h643.1l42.8-33.3l39.3 50.5zM833.6 232L512 482L190.4 232l-42.8-33.3l-39.3 50.5l27.6 21.5l341.6 265.6a55.99 55.99 0 0 0 68.7 0L888 270.8l27.6-21.5l-39.3-50.5z"></path></svg>
              </a>
            
          </td>
          <td>
            
              <a href="http://www.matematika.hr/index.php/natjecanja/" target="_blank" rel="noopener" aria-label="Visit national MO website for Croatia (opens in new tab)"><span class="data-table__label-full">Visit ↗</span><span class="data-table__label-short">↗</span></a>
            
          </td>
          <td class="data-table__hide-mobile data-table__num">
            1993
          </td>
          <td class="data-table__hide-mobile data-table__num">
            34
          </td>
          <td class="data-table__hide-mobile">
            
          </td>
        </tr>
        
        <tr>
          <td>
            <a href="/countries/HUN/" class="data-table__country-cell">
              <img class="data-table__country-flag" src="/assets/images/countries/flags/hun.svg" alt="">
              <span class="data-table__country-full">Hungary</span><span class="data-table__country-iso">HUN</span>
            </a>
          </td>
          <td>
            
              Géza Kós
            
          </td>
          <td>
            
              <a href="mailto:kosgeza@gmail.com" class="js-contact-email" data-email-user="kosgeza" data-email-domain="gmail.com" aria-label="Email Géza Kós" title="Email">
                <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 1024 1024" aria-hidden="true" focusable="false"><path fill="currentColor" d="M928 160H96c-17.7 0-32 14.3-32 32v640c0 17.7 14.3 32 32 32h832c17.7 0 32-14.3 32-32V192c0-17.7-14.3-32-32-32m-40 110.8V792H136V270.8l-27.6-21.5l39.3-50.5l42.8 33.3h643.1l42.8-33.3l39.3 50.5zM833.6 232L512 482L190.4 232l-42.8-33.3l-39.3 50.5l27.6 21.5l341.6 265.6a55.99 55.99 0 0 0 68.7 0L888 270.8l27.6-21.5l-39.3-50.5z"></path></svg>
              </a>
            
          </td>
          <td>
            
          </td>
          <td class="data-table__hide-mobile data-table__num">
            1959
          </td>
          <td class="data-table__hide-mobile data-table__num">
            66
          </td>
          <td class="data-table__hide-mobile">
            
              1961, 1970, 1982, 2027
            
          </td>
        </tr>
        
        <tr>
          <td>
            <a href="/countries/IDN/" class="data-table__country-cell">
              <img class="data-table__country-flag" src="/assets/images/countries/flags/idn.svg" alt="">
              <span class="data-table__country-full">Indonesia</span><span class="data-table__country-iso">IDN</span>
            </a>
          </td>
          <td>
            
              Aleams Barra
            
          </td>
          <td>
            
              <a href="mailto:aleamsbarra@gmail.com" class="js-contact-email" data-email-user="aleamsbarra" data-email-domain="gmail.com" aria-label="Email Aleams Barra" title="Email">
                <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 1024 1024" aria-hidden="true" focusable="false"><path fill="currentColor" d="M928 160H96c-17.7 0-32 14.3-32 32v640c0 17.7 14.3 32 32 32h832c17.7 0 32-14.3 32-32V192c0-17.7-14.3-32-32-32m-40 110.8V792H136V270.8l-27.6-21.5l39.3-50.5l42.8 33.3h643.1l42.8-33.3l39.3 50.5zM833.6 232L512 482L190.4 232l-42.8-33.3l-39.3 50.5l27.6 21.5l341.6 265.6a55.99 55.99 0 0 0 68.7 0L888 270.8l27.6-21.5l-39.3-50.5z"></path></svg>
              </a>
            
          </td>
          <td>
            
              <a href="http://www.tomi.or.id" target="_blank" rel="noopener" aria-label="Visit national MO website for Indonesia (opens in new tab)"><span class="data-table__label-full">Visit ↗</span><span class="data-table__label-short">↗</span></a>
            
          </td>
          <td class="data-table__hide-mobile data-table__num">
            1988
          </td>
          <td class="data-table__hide-mobile data-table__num">
            38
          </td>
          <td class="data-table__hide-mobile">
            
          </td>
        </tr>
        
        <tr>
          <td>
            <a href="/countries/IND/" class="data-table__country-cell">
              <img class="data-table__country-flag" src="/assets/images/countries/flags/ind.svg" alt="">
              <span class="data-table__country-full">India</span><span class="data-table__country-iso">IND</span>
            </a>
          </td>
          <td>
            
              Prithwijit De
            
          </td>
          <td>
            
              <a href="mailto:prithiwjit@hbcse.tifr.res.in" class="js-contact-email" data-email-user="prithiwjit" data-email-domain="hbcse.tifr.res.in" aria-label="Email Prithwijit De" title="Email">
                <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 1024 1024" aria-hidden="true" focusable="false"><path fill="currentColor" d="M928 160H96c-17.7 0-32 14.3-32 32v640c0 17.7 14.3 32 32 32h832c17.7 0 32-14.3 32-32V192c0-17.7-14.3-32-32-32m-40 110.8V792H136V270.8l-27.6-21.5l39.3-50.5l42.8 33.3h643.1l42.8-33.3l39.3 50.5zM833.6 232L512 482L190.4 232l-42.8-33.3l-39.3 50.5l27.6 21.5l341.6 265.6a55.99 55.99 0 0 0 68.7 0L888 270.8l27.6-21.5l-39.3-50.5z"></path></svg>
              </a>
            
          </td>
          <td>
            
              <a href="http://olympiads.hbcse.tifr.res.in/subjects/mathematics" target="_blank" rel="noopener" aria-label="Visit national MO website for India (opens in new tab)"><span class="data-table__label-full">Visit ↗</span><span class="data-table__label-short">↗</span></a>
            
          </td>
          <td class="data-table__hide-mobile data-table__num">
            1989
          </td>
          <td class="data-table__hide-mobile data-table__num">
            37
          </td>
          <td class="data-table__hide-mobile">
            
              1996
            
          </td>
        </tr>
        
        <tr>
          <td>
            <a href="/countries/IRL/" class="data-table__country-cell">
              <img class="data-table__country-flag" src="/assets/images/countries/flags/irl.svg" alt="">
              <span class="data-table__country-full">Ireland</span><span class="data-table__country-iso">IRL</span>
            </a>
          </td>
          <td>
            
              Mark Flanagan
            
          </td>
          <td>
            
              <a href="mailto:mark.flanagan@ucd.ie" class="js-contact-email" data-email-user="mark.flanagan" data-email-domain="ucd.ie" aria-label="Email Mark Flanagan" title="Email">
                <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 1024 1024" aria-hidden="true" focusable="false"><path fill="currentColor" d="M928 160H96c-17.7 0-32 14.3-32 32v640c0 17.7 14.3 32 32 32h832c17.7 0 32-14.3 32-32V192c0-17.7-14.3-32-32-32m-40 110.8V792H136V270.8l-27.6-21.5l39.3-50.5l42.8 33.3h643.1l42.8-33.3l39.3 50.5zM833.6 232L512 482L190.4 232l-42.8-33.3l-39.3 50.5l27.6 21.5l341.6 265.6a55.99 55.99 0 0 0 68.7 0L888 270.8l27.6-21.5l-39.3-50.5z"></path></svg>
              </a>
            
          </td>
          <td>
            
              <a href="https://www.irmo.ie" target="_blank" rel="noopener" aria-label="Visit national MO website for Ireland (opens in new tab)"><span class="data-table__label-full">Visit ↗</span><span class="data-table__label-short">↗</span></a>
            
          </td>
          <td class="data-table__hide-mobile data-table__num">
            1988
          </td>
          <td class="data-table__hide-mobile data-table__num">
            39
          </td>
          <td class="data-table__hide-mobile">
            
          </td>
        </tr>
        
        <tr>
          <td>
            <a href="/countries/IRN/" class="data-table__country-cell">
              <img class="data-table__country-flag" src="/assets/images/countries/flags/irn.svg" alt="">
              <span class="data-table__country-full">Islamic Republic of Iran</span><span class="data-table__country-iso">IRN</span>
            </a>
          </td>
          <td>
            
              Seyed Hessam Firouzi
            
          </td>
          <td>
            
              <a href="mailto:hessam.firouzi@gmail.com" class="js-contact-email" data-email-user="hessam.firouzi" data-email-domain="gmail.com" aria-label="Email Seyed Hessam Firouzi" title="Email">
                <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 1024 1024" aria-hidden="true" focusable="false"><path fill="currentColor" d="M928 160H96c-17.7 0-32 14.3-32 32v640c0 17.7 14.3 32 32 32h832c17.7 0 32-14.3 32-32V192c0-17.7-14.3-32-32-32m-40 110.8V792H136V270.8l-27.6-21.5l39.3-50.5l42.8 33.3h643.1l42.8-33.3l39.3 50.5zM833.6 232L512 482L190.4 232l-42.8-33.3l-39.3 50.5l27.6 21.5l341.6 265.6a55.99 55.99 0 0 0 68.7 0L888 270.8l27.6-21.5l-39.3-50.5z"></path></svg>
              </a>
            
          </td>
          <td>
            
              <a href="http://www.mathysc.ir" target="_blank" rel="noopener" aria-label="Visit national MO website for Islamic Republic of Iran (opens in new tab)"><span class="data-table__label-full">Visit ↗</span><span class="data-table__label-short">↗</span></a>
            
          </td>
          <td class="data-table__hide-mobile data-table__num">
            1985
          </td>
          <td class="data-table__hide-mobile data-table__num">
            41
          </td>
          <td class="data-table__hide-mobile">
            
          </td>
        </tr>
        
        <tr>
          <td>
            <a href="/countries/IRQ/" class="data-table__country-cell">
              <img class="data-table__country-flag" src="/assets/images/countries/flags/irq.svg" alt="">
              <span class="data-table__country-full">Iraq</span><span class="data-table__country-iso">IRQ</span>
            </a>
          </td>
          <td>
            
              Miri Tas
            
          </td>
          <td>
            
              <a href="mailto:miritas2011@gmail.com" class="js-contact-email" data-email-user="miritas2011" data-email-domain="gmail.com" aria-label="Email Miri Tas" title="Email">
                <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 1024 1024" aria-hidden="true" focusable="false"><path fill="currentColor" d="M928 160H96c-17.7 0-32 14.3-32 32v640c0 17.7 14.3 32 32 32h832c17.7 0 32-14.3 32-32V192c0-17.7-14.3-32-32-32m-40 110.8V792H136V270.8l-27.6-21.5l39.3-50.5l42.8 33.3h643.1l42.8-33.3l39.3 50.5zM833.6 232L512 482L190.4 232l-42.8-33.3l-39.3 50.5l27.6 21.5l341.6 265.6a55.99 55.99 0 0 0 68.7 0L888 270.8l27.6-21.5l-39.3-50.5z"></path></svg>
              </a>
            
          </td>
          <td>
            
          </td>
          <td class="data-table__hide-mobile data-table__num">
            2016
          </td>
          <td class="data-table__hide-mobile data-table__num">
            10
          </td>
          <td class="data-table__hide-mobile">
            
          </td>
        </tr>
        
        <tr>
          <td>
            <a href="/countries/ISL/" class="data-table__country-cell">
              <img class="data-table__country-flag" src="/assets/images/countries/flags/isl.svg" alt="">
              <span class="data-table__country-full">Iceland</span><span class="data-table__country-iso">ISL</span>
            </a>
          </td>
          <td>
            
              Marteinn Thor Harðarson
            
          </td>
          <td>
            
              <a href="mailto:mart1thor@gmail.com" class="js-contact-email" data-email-user="mart1thor" data-email-domain="gmail.com" aria-label="Email Marteinn Thor Harðarson" title="Email">
                <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 1024 1024" aria-hidden="true" focusable="false"><path fill="currentColor" d="M928 160H96c-17.7 0-32 14.3-32 32v640c0 17.7 14.3 32 32 32h832c17.7 0 32-14.3 32-32V192c0-17.7-14.3-32-32-32m-40 110.8V792H136V270.8l-27.6-21.5l39.3-50.5l42.8 33.3h643.1l42.8-33.3l39.3 50.5zM833.6 232L512 482L190.4 232l-42.8-33.3l-39.3 50.5l27.6 21.5l341.6 265.6a55.99 55.99 0 0 0 68.7 0L888 270.8l27.6-21.5l-39.3-50.5z"></path></svg>
              </a>
            
          </td>
          <td>
            
              <a href="http://stae.is/stak/keppnin" target="_blank" rel="noopener" aria-label="Visit national MO website for Iceland (opens in new tab)"><span class="data-table__label-full">Visit ↗</span><span class="data-table__label-short">↗</span></a>
            
          </td>
          <td class="data-table__hide-mobile data-table__num">
            1985
          </td>
          <td class="data-table__hide-mobile data-table__num">
            42
          </td>
          <td class="data-table__hide-mobile">
            
          </td>
        </tr>
        
        <tr>
          <td>
            <a href="/countries/ISR/" class="data-table__country-cell">
              <img class="data-table__country-flag" src="/assets/images/countries/flags/isr.svg" alt="">
              <span class="data-table__country-full">Israel</span><span class="data-table__country-iso">ISR</span>
            </a>
          </td>
          <td>
            
              Lev Radzivilovsky
            
          </td>
          <td>
            
              <a href="mailto:levr78@hotmail.com" class="js-contact-email" data-email-user="levr78" data-email-domain="hotmail.com" aria-label="Email Lev Radzivilovsky" title="Email">
                <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 1024 1024" aria-hidden="true" focusable="false"><path fill="currentColor" d="M928 160H96c-17.7 0-32 14.3-32 32v640c0 17.7 14.3 32 32 32h832c17.7 0 32-14.3 32-32V192c0-17.7-14.3-32-32-32m-40 110.8V792H136V270.8l-27.6-21.5l39.3-50.5l42.8 33.3h643.1l42.8-33.3l39.3 50.5zM833.6 232L512 482L190.4 232l-42.8-33.3l-39.3 50.5l27.6 21.5l341.6 265.6a55.99 55.99 0 0 0 68.7 0L888 270.8l27.6-21.5l-39.3-50.5z"></path></svg>
              </a>
            
          </td>
          <td>
            
              <a href="http://www.weizmann.ac.il/zemed/gillis" target="_blank" rel="noopener" aria-label="Visit national MO website for Israel (opens in new tab)"><span class="data-table__label-full">Visit ↗</span><span class="data-table__label-short">↗</span></a>
            
          </td>
          <td class="data-table__hide-mobile data-table__num">
            1979
          </td>
          <td class="data-table__hide-mobile data-table__num">
            45
          </td>
          <td class="data-table__hide-mobile">
            
          </td>
        </tr>
        
        <tr>
          <td>
            <a href="/countries/ITA/" class="data-table__country-cell">
              <img class="data-table__country-flag" src="/assets/images/countries/flags/ita.svg" alt="">
              <span class="data-table__country-full">Italy</span><span class="data-table__country-iso">ITA</span>
            </a>
          </td>
          <td>
            
              Massimo Gobbino
            
          </td>
          <td>
            
              <a href="mailto:massimo.gobbino@unipi.it" class="js-contact-email" data-email-user="massimo.gobbino" data-email-domain="unipi.it" aria-label="Email Massimo Gobbino" title="Email">
                <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 1024 1024" aria-hidden="true" focusable="false"><path fill="currentColor" d="M928 160H96c-17.7 0-32 14.3-32 32v640c0 17.7 14.3 32 32 32h832c17.7 0 32-14.3 32-32V192c0-17.7-14.3-32-32-32m-40 110.8V792H136V270.8l-27.6-21.5l39.3-50.5l42.8 33.3h643.1l42.8-33.3l39.3 50.5zM833.6 232L512 482L190.4 232l-42.8-33.3l-39.3 50.5l27.6 21.5l341.6 265.6a55.99 55.99 0 0 0 68.7 0L888 270.8l27.6-21.5l-39.3-50.5z"></path></svg>
              </a>
            
          </td>
          <td>
            
              <a href="http://olimpiadi.dm.unibo.it/" target="_blank" rel="noopener" aria-label="Visit national MO website for Italy (opens in new tab)"><span class="data-table__label-full">Visit ↗</span><span class="data-table__label-short">↗</span></a>
            
          </td>
          <td class="data-table__hide-mobile data-table__num">
            1967
          </td>
          <td class="data-table__hide-mobile data-table__num">
            47
          </td>
          <td class="data-table__hide-mobile">
            
          </td>
        </tr>
        
        <tr>
          <td>
            <a href="/countries/JAM/" class="data-table__country-cell">
              <img class="data-table__country-flag" src="/assets/images/countries/flags/jam.svg" alt="">
              <span class="data-table__country-full">Jamaica</span><span class="data-table__country-iso">JAM</span>
            </a>
          </td>
          <td>
            
              Raymond McEachin
            
          </td>
          <td>
            
              <a href="mailto:rmceachin@hotmail.com" class="js-contact-email" data-email-user="rmceachin" data-email-domain="hotmail.com" aria-label="Email Raymond McEachin" title="Email">
                <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 1024 1024" aria-hidden="true" focusable="false"><path fill="currentColor" d="M928 160H96c-17.7 0-32 14.3-32 32v640c0 17.7 14.3 32 32 32h832c17.7 0 32-14.3 32-32V192c0-17.7-14.3-32-32-32m-40 110.8V792H136V270.8l-27.6-21.5l39.3-50.5l42.8 33.3h643.1l42.8-33.3l39.3 50.5zM833.6 232L512 482L190.4 232l-42.8-33.3l-39.3 50.5l27.6 21.5l341.6 265.6a55.99 55.99 0 0 0 68.7 0L888 270.8l27.6-21.5l-39.3-50.5z"></path></svg>
              </a>
            
          </td>
          <td>
            
          </td>
          <td class="data-table__hide-mobile data-table__num">
            2016
          </td>
          <td class="data-table__hide-mobile data-table__num">
            1
          </td>
          <td class="data-table__hide-mobile">
            
          </td>
        </tr>
        
        <tr>
          <td>
            <a href="/countries/JPN/" class="data-table__country-cell">
              <img class="data-table__country-flag" src="/assets/images/countries/flags/jpn.svg" alt="">
              <span class="data-table__country-full">Japan</span><span class="data-table__country-iso">JPN</span>
            </a>
          </td>
          <td>
            
              前田 吉昭
            
          </td>
          <td>
            
              <a href="mailto:info@imojp.org" class="js-contact-email" data-email-user="info" data-email-domain="imojp.org" aria-label="Email 前田 吉昭" title="Email">
                <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 1024 1024" aria-hidden="true" focusable="false"><path fill="currentColor" d="M928 160H96c-17.7 0-32 14.3-32 32v640c0 17.7 14.3 32 32 32h832c17.7 0 32-14.3 32-32V192c0-17.7-14.3-32-32-32m-40 110.8V792H136V270.8l-27.6-21.5l39.3-50.5l42.8 33.3h643.1l42.8-33.3l39.3 50.5zM833.6 232L512 482L190.4 232l-42.8-33.3l-39.3 50.5l27.6 21.5l341.6 265.6a55.99 55.99 0 0 0 68.7 0L888 270.8l27.6-21.5l-39.3-50.5z"></path></svg>
              </a>
            
          </td>
          <td>
            
              <a href="http://www.imojp.org" target="_blank" rel="noopener" aria-label="Visit national MO website for Japan (opens in new tab)"><span class="data-table__label-full">Visit ↗</span><span class="data-table__label-short">↗</span></a>
            
          </td>
          <td class="data-table__hide-mobile data-table__num">
            1990
          </td>
          <td class="data-table__hide-mobile data-table__num">
            37
          </td>
          <td class="data-table__hide-mobile">
            
              2003, 2023
            
          </td>
        </tr>
        
        <tr>
          <td>
            <a href="/countries/KAZ/" class="data-table__country-cell">
              <img class="data-table__country-flag" src="/assets/images/countries/flags/kaz.svg" alt="">
              <span class="data-table__country-full">Kazakhstan</span><span class="data-table__country-iso">KAZ</span>
            </a>
          </td>
          <td>
            
              Gazhdembek Tursunov
            
          </td>
          <td>
            
              <a href="mailto:daryn.intel@gmail.com" class="js-contact-email" data-email-user="daryn.intel" data-email-domain="gmail.com" aria-label="Email Gazhdembek Tursunov" title="Email">
                <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 1024 1024" aria-hidden="true" focusable="false"><path fill="currentColor" d="M928 160H96c-17.7 0-32 14.3-32 32v640c0 17.7 14.3 32 32 32h832c17.7 0 32-14.3 32-32V192c0-17.7-14.3-32-32-32m-40 110.8V792H136V270.8l-27.6-21.5l39.3-50.5l42.8 33.3h643.1l42.8-33.3l39.3 50.5zM833.6 232L512 482L190.4 232l-42.8-33.3l-39.3 50.5l27.6 21.5l341.6 265.6a55.99 55.99 0 0 0 68.7 0L888 270.8l27.6-21.5l-39.3-50.5z"></path></svg>
              </a>
            
          </td>
          <td>
            
          </td>
          <td class="data-table__hide-mobile data-table__num">
            1993
          </td>
          <td class="data-table__hide-mobile data-table__num">
            33
          </td>
          <td class="data-table__hide-mobile">
            
              2010
            
          </td>
        </tr>
        
        <tr>
          <td>
            <a href="/countries/KEN/" class="data-table__country-cell">
              <img class="data-table__country-flag" src="/assets/images/countries/flags/ken.svg" alt="">
              <span class="data-table__country-full">Kenya</span><span class="data-table__country-iso">KEN</span>
            </a>
          </td>
          <td>
            
              James Kiwanuka Katende
            
          </td>
          <td>
            
              <a href="mailto:jkatende@uonbi.ac.ke" class="js-contact-email" data-email-user="jkatende" data-email-domain="uonbi.ac.ke" aria-label="Email James Kiwanuka Katende" title="Email">
                <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 1024 1024" aria-hidden="true" focusable="false"><path fill="currentColor" d="M928 160H96c-17.7 0-32 14.3-32 32v640c0 17.7 14.3 32 32 32h832c17.7 0 32-14.3 32-32V192c0-17.7-14.3-32-32-32m-40 110.8V792H136V270.8l-27.6-21.5l39.3-50.5l42.8 33.3h643.1l42.8-33.3l39.3 50.5zM833.6 232L512 482L190.4 232l-42.8-33.3l-39.3 50.5l27.6 21.5l341.6 265.6a55.99 55.99 0 0 0 68.7 0L888 270.8l27.6-21.5l-39.3-50.5z"></path></svg>
              </a>
            
          </td>
          <td>
            
              <a href="http://kkmo-official.com" target="_blank" rel="noopener" aria-label="Visit national MO website for Kenya (opens in new tab)"><span class="data-table__label-full">Visit ↗</span><span class="data-table__label-short">↗</span></a>
            
          </td>
          <td class="data-table__hide-mobile data-table__num">
            2016
          </td>
          <td class="data-table__hide-mobile data-table__num">
            9
          </td>
          <td class="data-table__hide-mobile">
            
          </td>
        </tr>
        
        <tr>
          <td>
            <a href="/countries/KGZ/" class="data-table__country-cell">
              <img class="data-table__country-flag" src="/assets/images/countries/flags/kgz.svg" alt="">
              <span class="data-table__country-full">Kyrgyzstan</span><span class="data-table__country-iso">KGZ</span>
            </a>
          </td>
          <td>
            
              Ishmatov Makhamadkhan
            
          </td>
          <td>
            
              <a href="mailto:matematikLL@gmail.com" class="js-contact-email" data-email-user="matematikLL" data-email-domain="gmail.com" aria-label="Email Ishmatov Makhamadkhan" title="Email">
                <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 1024 1024" aria-hidden="true" focusable="false"><path fill="currentColor" d="M928 160H96c-17.7 0-32 14.3-32 32v640c0 17.7 14.3 32 32 32h832c17.7 0 32-14.3 32-32V192c0-17.7-14.3-32-32-32m-40 110.8V792H136V270.8l-27.6-21.5l39.3-50.5l42.8 33.3h643.1l42.8-33.3l39.3 50.5zM833.6 232L512 482L190.4 232l-42.8-33.3l-39.3 50.5l27.6 21.5l341.6 265.6a55.99 55.99 0 0 0 68.7 0L888 270.8l27.6-21.5l-39.3-50.5z"></path></svg>
              </a>
            
          </td>
          <td>
            
          </td>
          <td class="data-table__hide-mobile data-table__num">
            1993
          </td>
          <td class="data-table__hide-mobile data-table__num">
            34
          </td>
          <td class="data-table__hide-mobile">
            
          </td>
        </tr>
        
        <tr>
          <td>
            <a href="/countries/KHM/" class="data-table__country-cell">
              <img class="data-table__country-flag" src="/assets/images/countries/flags/khm.svg" alt="">
              <span class="data-table__country-full">Cambodia</span><span class="data-table__country-iso">KHM</span>
            </a>
          </td>
          <td>
            
              Seam Ngonn
            
          </td>
          <td>
            
              <a href="mailto:seamngonn@yahoo.fr" class="js-contact-email" data-email-user="seamngonn" data-email-domain="yahoo.fr" aria-label="Email Seam Ngonn" title="Email">
                <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 1024 1024" aria-hidden="true" focusable="false"><path fill="currentColor" d="M928 160H96c-17.7 0-32 14.3-32 32v640c0 17.7 14.3 32 32 32h832c17.7 0 32-14.3 32-32V192c0-17.7-14.3-32-32-32m-40 110.8V792H136V270.8l-27.6-21.5l39.3-50.5l42.8 33.3h643.1l42.8-33.3l39.3 50.5zM833.6 232L512 482L190.4 232l-42.8-33.3l-39.3 50.5l27.6 21.5l341.6 265.6a55.99 55.99 0 0 0 68.7 0L888 270.8l27.6-21.5l-39.3-50.5z"></path></svg>
              </a>
            
          </td>
          <td>
            
          </td>
          <td class="data-table__hide-mobile data-table__num">
            2007
          </td>
          <td class="data-table__hide-mobile data-table__num">
            11
          </td>
          <td class="data-table__hide-mobile">
            
          </td>
        </tr>
        
        <tr>
          <td>
            <a href="/countries/KOR/" class="data-table__country-cell">
              <img class="data-table__country-flag" src="/assets/images/countries/flags/kor.svg" alt="">
              <span class="data-table__country-full">Republic of Korea</span><span class="data-table__country-iso">KOR</span>
            </a>
          </td>
          <td>
            
              Prof. Hoseog Yu
            
          </td>
          <td>
            
              <a href="mailto:kmo@kms.or.kr" class="js-contact-email" data-email-user="kmo" data-email-domain="kms.or.kr" aria-label="Email Prof. Hoseog Yu" title="Email">
                <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 1024 1024" aria-hidden="true" focusable="false"><path fill="currentColor" d="M928 160H96c-17.7 0-32 14.3-32 32v640c0 17.7 14.3 32 32 32h832c17.7 0 32-14.3 32-32V192c0-17.7-14.3-32-32-32m-40 110.8V792H136V270.8l-27.6-21.5l39.3-50.5l42.8 33.3h643.1l42.8-33.3l39.3 50.5zM833.6 232L512 482L190.4 232l-42.8-33.3l-39.3 50.5l27.6 21.5l341.6 265.6a55.99 55.99 0 0 0 68.7 0L888 270.8l27.6-21.5l-39.3-50.5z"></path></svg>
              </a>
            
          </td>
          <td>
            
              <a href="https://www.kmo.or.kr" target="_blank" rel="noopener" aria-label="Visit national MO website for Republic of Korea (opens in new tab)"><span class="data-table__label-full">Visit ↗</span><span class="data-table__label-short">↗</span></a>
            
          </td>
          <td class="data-table__hide-mobile data-table__num">
            1988
          </td>
          <td class="data-table__hide-mobile data-table__num">
            39
          </td>
          <td class="data-table__hide-mobile">
            
              2000
            
          </td>
        </tr>
        
        <tr>
          <td>
            <a href="/countries/KSV/" class="data-table__country-cell">
              <img class="data-table__country-flag" src="/assets/images/countries/flags/ksv.svg" alt="">
              <span class="data-table__country-full">Kosovo</span><span class="data-table__country-iso">KSV</span>
            </a>
          </td>
          <td>
            
              Armend Shabani
            
          </td>
          <td>
            
              <a href="mailto:shoqata.matematikaneve@gmail.com" class="js-contact-email" data-email-user="shoqata.matematikaneve" data-email-domain="gmail.com" aria-label="Email Armend Shabani" title="Email">
                <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 1024 1024" aria-hidden="true" focusable="false"><path fill="currentColor" d="M928 160H96c-17.7 0-32 14.3-32 32v640c0 17.7 14.3 32 32 32h832c17.7 0 32-14.3 32-32V192c0-17.7-14.3-32-32-32m-40 110.8V792H136V270.8l-27.6-21.5l39.3-50.5l42.8 33.3h643.1l42.8-33.3l39.3 50.5zM833.6 232L512 482L190.4 232l-42.8-33.3l-39.3 50.5l27.6 21.5l341.6 265.6a55.99 55.99 0 0 0 68.7 0L888 270.8l27.6-21.5l-39.3-50.5z"></path></svg>
              </a>
            
          </td>
          <td>
            
              <a href="http://www.kms-ks.org" target="_blank" rel="noopener" aria-label="Visit national MO website for Kosovo (opens in new tab)"><span class="data-table__label-full">Visit ↗</span><span class="data-table__label-short">↗</span></a>
            
          </td>
          <td class="data-table__hide-mobile data-table__num">
            2011
          </td>
          <td class="data-table__hide-mobile data-table__num">
            15
          </td>
          <td class="data-table__hide-mobile">
            
          </td>
        </tr>
        
        <tr>
          <td>
            <a href="/countries/KWT/" class="data-table__country-cell">
              <img class="data-table__country-flag" src="/assets/images/countries/flags/kwt.svg" alt="">
              <span class="data-table__country-full">Kuwait</span><span class="data-table__country-iso">KWT</span>
            </a>
          </td>
          <td>
            
              Mohammad Al-Baqshi
            
          </td>
          <td>
            
              <a href="mailto:m.albaqshi@sacgc.org" class="js-contact-email" data-email-user="m.albaqshi" data-email-domain="sacgc.org" aria-label="Email Mohammad Al-Baqshi" title="Email">
                <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 1024 1024" aria-hidden="true" focusable="false"><path fill="currentColor" d="M928 160H96c-17.7 0-32 14.3-32 32v640c0 17.7 14.3 32 32 32h832c17.7 0 32-14.3 32-32V192c0-17.7-14.3-32-32-32m-40 110.8V792H136V270.8l-27.6-21.5l39.3-50.5l42.8 33.3h643.1l42.8-33.3l39.3 50.5zM833.6 232L512 482L190.4 232l-42.8-33.3l-39.3 50.5l27.6 21.5l341.6 265.6a55.99 55.99 0 0 0 68.7 0L888 270.8l27.6-21.5l-39.3-50.5z"></path></svg>
              </a>
            
          </td>
          <td>
            
          </td>
          <td class="data-table__hide-mobile data-table__num">
            1982
          </td>
          <td class="data-table__hide-mobile data-table__num">
            28
          </td>
          <td class="data-table__hide-mobile">
            
          </td>
        </tr>
        
        <tr>
          <td>
            <a href="/countries/LAO/" class="data-table__country-cell">
              <img class="data-table__country-flag" src="/assets/images/countries/flags/lao.svg" alt="">
              <span class="data-table__country-full">Laos</span><span class="data-table__country-iso">LAO</span>
            </a>
          </td>
          <td>
            
              Sackmone Sirisack
            
          </td>
          <td>
            
              <a href="mailto:ssirisack2000@yahoo.com" class="js-contact-email" data-email-user="ssirisack2000" data-email-domain="yahoo.com" aria-label="Email Sackmone Sirisack" title="Email">
                <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 1024 1024" aria-hidden="true" focusable="false"><path fill="currentColor" d="M928 160H96c-17.7 0-32 14.3-32 32v640c0 17.7 14.3 32 32 32h832c17.7 0 32-14.3 32-32V192c0-17.7-14.3-32-32-32m-40 110.8V792H136V270.8l-27.6-21.5l39.3-50.5l42.8 33.3h643.1l42.8-33.3l39.3 50.5zM833.6 232L512 482L190.4 232l-42.8-33.3l-39.3 50.5l27.6 21.5l341.6 265.6a55.99 55.99 0 0 0 68.7 0L888 270.8l27.6-21.5l-39.3-50.5z"></path></svg>
              </a>
            
          </td>
          <td>
            
          </td>
          <td class="data-table__hide-mobile data-table__num">
            2016
          </td>
          <td class="data-table__hide-mobile data-table__num">
            1
          </td>
          <td class="data-table__hide-mobile">
            
          </td>
        </tr>
        
        <tr>
          <td>
            <a href="/countries/LBN/" class="data-table__country-cell">
              <img class="data-table__country-flag" src="/assets/images/countries/flags/lbn.svg" alt="">
              <span class="data-table__country-full">Lebanon</span><span class="data-table__country-iso">LBN</span>
            </a>
          </td>
          <td>
            
              Marc Fares
            
          </td>
          <td>
            
              <a href="mailto:imo@mjfares.com" class="js-contact-email" data-email-user="imo" data-email-domain="mjfares.com" aria-label="Email Marc Fares" title="Email">
                <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 1024 1024" aria-hidden="true" focusable="false"><path fill="currentColor" d="M928 160H96c-17.7 0-32 14.3-32 32v640c0 17.7 14.3 32 32 32h832c17.7 0 32-14.3 32-32V192c0-17.7-14.3-32-32-32m-40 110.8V792H136V270.8l-27.6-21.5l39.3-50.5l42.8 33.3h643.1l42.8-33.3l39.3 50.5zM833.6 232L512 482L190.4 232l-42.8-33.3l-39.3 50.5l27.6 21.5l341.6 265.6a55.99 55.99 0 0 0 68.7 0L888 270.8l27.6-21.5l-39.3-50.5z"></path></svg>
              </a>
            
          </td>
          <td>
            
          </td>
          <td class="data-table__hide-mobile data-table__num">
            
          </td>
          <td class="data-table__hide-mobile data-table__num">
            0
          </td>
          <td class="data-table__hide-mobile">
            
          </td>
        </tr>
        
        <tr>
          <td>
            <a href="/countries/LBY/" class="data-table__country-cell">
              <img class="data-table__country-flag" src="/assets/images/countries/flags/lby.svg" alt="">
              <span class="data-table__country-full">Libya</span><span class="data-table__country-iso">LBY</span>
            </a>
          </td>
          <td>
            
              Moied Baleg
            
          </td>
          <td>
            
              <a href="mailto:whitearrow1434@gmail.com" class="js-contact-email" data-email-user="whitearrow1434" data-email-domain="gmail.com" aria-label="Email Moied Baleg" title="Email">
                <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 1024 1024" aria-hidden="true" focusable="false"><path fill="currentColor" d="M928 160H96c-17.7 0-32 14.3-32 32v640c0 17.7 14.3 32 32 32h832c17.7 0 32-14.3 32-32V192c0-17.7-14.3-32-32-32m-40 110.8V792H136V270.8l-27.6-21.5l39.3-50.5l42.8 33.3h643.1l42.8-33.3l39.3 50.5zM833.6 232L512 482L190.4 232l-42.8-33.3l-39.3 50.5l27.6 21.5l341.6 265.6a55.99 55.99 0 0 0 68.7 0L888 270.8l27.6-21.5l-39.3-50.5z"></path></svg>
              </a>
            
          </td>
          <td>
            
          </td>
          <td class="data-table__hide-mobile data-table__num">
            2026
          </td>
          <td class="data-table__hide-mobile data-table__num">
            1
          </td>
          <td class="data-table__hide-mobile">
            
          </td>
        </tr>
        
        <tr>
          <td>
            <a href="/countries/LIE/" class="data-table__country-cell">
              <img class="data-table__country-flag" src="/assets/images/countries/flags/lie.svg" alt="">
              <span class="data-table__country-full">Liechtenstein</span><span class="data-table__country-iso">LIE</span>
            </a>
          </td>
          <td>
            
              Arnaud Maret
            
          </td>
          <td>
            
              <a href="mailto:a.maret@mathematical.olympiad.ch" class="js-contact-email" data-email-user="a.maret" data-email-domain="mathematical.olympiad.ch" aria-label="Email Arnaud Maret" title="Email">
                <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 1024 1024" aria-hidden="true" focusable="false"><path fill="currentColor" d="M928 160H96c-17.7 0-32 14.3-32 32v640c0 17.7 14.3 32 32 32h832c17.7 0 32-14.3 32-32V192c0-17.7-14.3-32-32-32m-40 110.8V792H136V270.8l-27.6-21.5l39.3-50.5l42.8 33.3h643.1l42.8-33.3l39.3 50.5zM833.6 232L512 482L190.4 232l-42.8-33.3l-39.3 50.5l27.6 21.5l341.6 265.6a55.99 55.99 0 0 0 68.7 0L888 270.8l27.6-21.5l-39.3-50.5z"></path></svg>
              </a>
            
          </td>
          <td>
            
              <a href="https://mathematical.olympiad.ch/en/" target="_blank" rel="noopener" aria-label="Visit national MO website for Liechtenstein (opens in new tab)"><span class="data-table__label-full">Visit ↗</span><span class="data-table__label-short">↗</span></a>
            
          </td>
          <td class="data-table__hide-mobile data-table__num">
            2005
          </td>
          <td class="data-table__hide-mobile data-table__num">
            16
          </td>
          <td class="data-table__hide-mobile">
            
          </td>
        </tr>
        
        <tr>
          <td>
            <a href="/countries/LKA/" class="data-table__country-cell">
              <img class="data-table__country-flag" src="/assets/images/countries/flags/lka.svg" alt="">
              <span class="data-table__country-full">Sri Lanka</span><span class="data-table__country-iso">LKA</span>
            </a>
          </td>
          <td>
            
              Chanakya J. Wijeratne
            
          </td>
          <td>
            
              <a href="mailto:chanakya_wijeratne@yahoo.com" class="js-contact-email" data-email-user="chanakya_wijeratne" data-email-domain="yahoo.com" aria-label="Email Chanakya J. Wijeratne" title="Email">
                <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 1024 1024" aria-hidden="true" focusable="false"><path fill="currentColor" d="M928 160H96c-17.7 0-32 14.3-32 32v640c0 17.7 14.3 32 32 32h832c17.7 0 32-14.3 32-32V192c0-17.7-14.3-32-32-32m-40 110.8V792H136V270.8l-27.6-21.5l39.3-50.5l42.8 33.3h643.1l42.8-33.3l39.3 50.5zM833.6 232L512 482L190.4 232l-42.8-33.3l-39.3 50.5l27.6 21.5l341.6 265.6a55.99 55.99 0 0 0 68.7 0L888 270.8l27.6-21.5l-39.3-50.5z"></path></svg>
              </a>
            
          </td>
          <td>
            
              <a href="http://www.slmathsolympiad.org/" target="_blank" rel="noopener" aria-label="Visit national MO website for Sri Lanka (opens in new tab)"><span class="data-table__label-full">Visit ↗</span><span class="data-table__label-short">↗</span></a>
            
          </td>
          <td class="data-table__hide-mobile data-table__num">
            1995
          </td>
          <td class="data-table__hide-mobile data-table__num">
            31
          </td>
          <td class="data-table__hide-mobile">
            
          </td>
        </tr>
        
        <tr>
          <td>
            <a href="/countries/LTU/" class="data-table__country-cell">
              <img class="data-table__country-flag" src="/assets/images/countries/flags/ltu.svg" alt="">
              <span class="data-table__country-full">Lithuania</span><span class="data-table__country-iso">LTU</span>
            </a>
          </td>
          <td>
            
              Aivaras Novikas
            
          </td>
          <td>
            
              <a href="mailto:aivaras.novikas@mif.vu.lt" class="js-contact-email" data-email-user="aivaras.novikas" data-email-domain="mif.vu.lt" aria-label="Email Aivaras Novikas" title="Email">
                <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 1024 1024" aria-hidden="true" focusable="false"><path fill="currentColor" d="M928 160H96c-17.7 0-32 14.3-32 32v640c0 17.7 14.3 32 32 32h832c17.7 0 32-14.3 32-32V192c0-17.7-14.3-32-32-32m-40 110.8V792H136V270.8l-27.6-21.5l39.3-50.5l42.8 33.3h643.1l42.8-33.3l39.3 50.5zM833.6 232L512 482L190.4 232l-42.8-33.3l-39.3 50.5l27.6 21.5l341.6 265.6a55.99 55.99 0 0 0 68.7 0L888 270.8l27.6-21.5l-39.3-50.5z"></path></svg>
              </a>
            
          </td>
          <td>
            
              <a href="https://mif.vu.lt/matematikos-olimpiados/" target="_blank" rel="noopener" aria-label="Visit national MO website for Lithuania (opens in new tab)"><span class="data-table__label-full">Visit ↗</span><span class="data-table__label-short">↗</span></a>
            
          </td>
          <td class="data-table__hide-mobile data-table__num">
            1993
          </td>
          <td class="data-table__hide-mobile data-table__num">
            34
          </td>
          <td class="data-table__hide-mobile">
            
          </td>
        </tr>
        
        <tr>
          <td>
            <a href="/countries/LUX/" class="data-table__country-cell">
              <img class="data-table__country-flag" src="/assets/images/countries/flags/lux.svg" alt="">
              <span class="data-table__country-full">Luxembourg</span><span class="data-table__country-iso">LUX</span>
            </a>
          </td>
          <td>
            
              Mike Dostert
            
          </td>
          <td>
            
              <a href="mailto:mike.dostert@education.lu" class="js-contact-email" data-email-user="mike.dostert" data-email-domain="education.lu" aria-label="Email Mike Dostert" title="Email">
                <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 1024 1024" aria-hidden="true" focusable="false"><path fill="currentColor" d="M928 160H96c-17.7 0-32 14.3-32 32v640c0 17.7 14.3 32 32 32h832c17.7 0 32-14.3 32-32V192c0-17.7-14.3-32-32-32m-40 110.8V792H136V270.8l-27.6-21.5l39.3-50.5l42.8 33.3h643.1l42.8-33.3l39.3 50.5zM833.6 232L512 482L190.4 232l-42.8-33.3l-39.3 50.5l27.6 21.5l341.6 265.6a55.99 55.99 0 0 0 68.7 0L888 270.8l27.6-21.5l-39.3-50.5z"></path></svg>
              </a>
            
          </td>
          <td>
            
          </td>
          <td class="data-table__hide-mobile data-table__num">
            1979
          </td>
          <td class="data-table__hide-mobile data-table__num">
            41
          </td>
          <td class="data-table__hide-mobile">
            
          </td>
        </tr>
        
        <tr>
          <td>
            <a href="/countries/LVA/" class="data-table__country-cell">
              <img class="data-table__country-flag" src="/assets/images/countries/flags/lva.svg" alt="">
              <span class="data-table__country-full">Latvia</span><span class="data-table__country-iso">LVA</span>
            </a>
          </td>
          <td>
            
              Kristīne Akopjana
            
          </td>
          <td>
            
              <a href="mailto:nms@lu.lv" class="js-contact-email" data-email-user="nms" data-email-domain="lu.lv" aria-label="Email Kristīne Akopjana" title="Email">
                <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 1024 1024" aria-hidden="true" focusable="false"><path fill="currentColor" d="M928 160H96c-17.7 0-32 14.3-32 32v640c0 17.7 14.3 32 32 32h832c17.7 0 32-14.3 32-32V192c0-17.7-14.3-32-32-32m-40 110.8V792H136V270.8l-27.6-21.5l39.3-50.5l42.8 33.3h643.1l42.8-33.3l39.3 50.5zM833.6 232L512 482L190.4 232l-42.8-33.3l-39.3 50.5l27.6 21.5l341.6 265.6a55.99 55.99 0 0 0 68.7 0L888 270.8l27.6-21.5l-39.3-50.5z"></path></svg>
              </a>
            
          </td>
          <td>
            
              <a href="http://nms.lu.lv" target="_blank" rel="noopener" aria-label="Visit national MO website for Latvia (opens in new tab)"><span class="data-table__label-full">Visit ↗</span><span class="data-table__label-short">↗</span></a>
            
          </td>
          <td class="data-table__hide-mobile data-table__num">
            1993
          </td>
          <td class="data-table__hide-mobile data-table__num">
            34
          </td>
          <td class="data-table__hide-mobile">
            
          </td>
        </tr>
        
        <tr>
          <td>
            <a href="/countries/MAC/" class="data-table__country-cell">
              <img class="data-table__country-flag" src="/assets/images/countries/flags/mac.svg" alt="">
              <span class="data-table__country-full">Macau</span><span class="data-table__country-iso">MAC</span>
            </a>
          </td>
          <td>
            
              Ieng Tak Long
            
          </td>
          <td>
            
              <a href="mailto:itleong@um.edu.mo" class="js-contact-email" data-email-user="itleong" data-email-domain="um.edu.mo" aria-label="Email Ieng Tak Long" title="Email">
                <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 1024 1024" aria-hidden="true" focusable="false"><path fill="currentColor" d="M928 160H96c-17.7 0-32 14.3-32 32v640c0 17.7 14.3 32 32 32h832c17.7 0 32-14.3 32-32V192c0-17.7-14.3-32-32-32m-40 110.8V792H136V270.8l-27.6-21.5l39.3-50.5l42.8 33.3h643.1l42.8-33.3l39.3 50.5zM833.6 232L512 482L190.4 232l-42.8-33.3l-39.3 50.5l27.6 21.5l341.6 265.6a55.99 55.99 0 0 0 68.7 0L888 270.8l27.6-21.5l-39.3-50.5z"></path></svg>
              </a>
            
          </td>
          <td>
            
          </td>
          <td class="data-table__hide-mobile data-table__num">
            1990
          </td>
          <td class="data-table__hide-mobile data-table__num">
            35
          </td>
          <td class="data-table__hide-mobile">
            
          </td>
        </tr>
        
        <tr>
          <td>
            <a href="/countries/MAR/" class="data-table__country-cell">
              <img class="data-table__country-flag" src="/assets/images/countries/flags/mar.svg" alt="">
              <span class="data-table__country-full">Morocco</span><span class="data-table__country-iso">MAR</span>
            </a>
          </td>
          <td>
            
              ASENSOUYIS Hassan
            
          </td>
          <td>
            
              <a href="mailto:hassan_asensouyis@yahoo.fr" class="js-contact-email" data-email-user="hassan_asensouyis" data-email-domain="yahoo.fr" aria-label="Email ASENSOUYIS Hassan" title="Email">
                <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 1024 1024" aria-hidden="true" focusable="false"><path fill="currentColor" d="M928 160H96c-17.7 0-32 14.3-32 32v640c0 17.7 14.3 32 32 32h832c17.7 0 32-14.3 32-32V192c0-17.7-14.3-32-32-32m-40 110.8V792H136V270.8l-27.6-21.5l39.3-50.5l42.8 33.3h643.1l42.8-33.3l39.3 50.5zM833.6 232L512 482L190.4 232l-42.8-33.3l-39.3 50.5l27.6 21.5l341.6 265.6a55.99 55.99 0 0 0 68.7 0L888 270.8l27.6-21.5l-39.3-50.5z"></path></svg>
              </a>
            
          </td>
          <td>
            
          </td>
          <td class="data-table__hide-mobile data-table__num">
            1983
          </td>
          <td class="data-table__hide-mobile data-table__num">
            43
          </td>
          <td class="data-table__hide-mobile">
            
          </td>
        </tr>
        
        <tr>
          <td>
            <a href="/countries/MAS/" class="data-table__country-cell">
              <img class="data-table__country-flag" src="/assets/images/countries/flags/mas.svg" alt="">
              <span class="data-table__country-full">Malaysia</span><span class="data-table__country-iso">MAS</span>
            </a>
          </td>
          <td>
            
              M. Suhaimi Ramly
            
          </td>
          <td>
            
              <a href="mailto:contact@imo-malaysia.org" class="js-contact-email" data-email-user="contact" data-email-domain="imo-malaysia.org" aria-label="Email M. Suhaimi Ramly" title="Email">
                <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 1024 1024" aria-hidden="true" focusable="false"><path fill="currentColor" d="M928 160H96c-17.7 0-32 14.3-32 32v640c0 17.7 14.3 32 32 32h832c17.7 0 32-14.3 32-32V192c0-17.7-14.3-32-32-32m-40 110.8V792H136V270.8l-27.6-21.5l39.3-50.5l42.8 33.3h643.1l42.8-33.3l39.3 50.5zM833.6 232L512 482L190.4 232l-42.8-33.3l-39.3 50.5l27.6 21.5l341.6 265.6a55.99 55.99 0 0 0 68.7 0L888 270.8l27.6-21.5l-39.3-50.5z"></path></svg>
              </a>
            
          </td>
          <td>
            
              <a href="https://imo-malaysia.org/" target="_blank" rel="noopener" aria-label="Visit national MO website for Malaysia (opens in new tab)"><span class="data-table__label-full">Visit ↗</span><span class="data-table__label-short">↗</span></a>
            
          </td>
          <td class="data-table__hide-mobile data-table__num">
            1995
          </td>
          <td class="data-table__hide-mobile data-table__num">
            32
          </td>
          <td class="data-table__hide-mobile">
            
          </td>
        </tr>
        
        <tr>
          <td>
            <a href="/countries/MDA/" class="data-table__country-cell">
              <img class="data-table__country-flag" src="/assets/images/countries/flags/mda.svg" alt="">
              <span class="data-table__country-full">Republic of Moldova</span><span class="data-table__country-iso">MDA</span>
            </a>
          </td>
          <td>
            
              Anatolie Topala
            
          </td>
          <td>
            
              <a href="mailto:anatoltop@yahoo.com" class="js-contact-email" data-email-user="anatoltop" data-email-domain="yahoo.com" aria-label="Email Anatolie Topala" title="Email">
                <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 1024 1024" aria-hidden="true" focusable="false"><path fill="currentColor" d="M928 160H96c-17.7 0-32 14.3-32 32v640c0 17.7 14.3 32 32 32h832c17.7 0 32-14.3 32-32V192c0-17.7-14.3-32-32-32m-40 110.8V792H136V270.8l-27.6-21.5l39.3-50.5l42.8 33.3h643.1l42.8-33.3l39.3 50.5zM833.6 232L512 482L190.4 232l-42.8-33.3l-39.3 50.5l27.6 21.5l341.6 265.6a55.99 55.99 0 0 0 68.7 0L888 270.8l27.6-21.5l-39.3-50.5z"></path></svg>
              </a>
            
          </td>
          <td>
            
          </td>
          <td class="data-table__hide-mobile data-table__num">
            1993
          </td>
          <td class="data-table__hide-mobile data-table__num">
            34
          </td>
          <td class="data-table__hide-mobile">
            
          </td>
        </tr>
        
        <tr>
          <td>
            <a href="/countries/MDG/" class="data-table__country-cell">
              <img class="data-table__country-flag" src="/assets/images/countries/flags/mdg.svg" alt="">
              <span class="data-table__country-full">Madagascar</span><span class="data-table__country-iso">MDG</span>
            </a>
          </td>
          <td>
            
              Fanja Rakotondrajao
            
          </td>
          <td>
            
              <a href="mailto:frakoton@yahoo.fr" class="js-contact-email" data-email-user="frakoton" data-email-domain="yahoo.fr" aria-label="Email Fanja Rakotondrajao" title="Email">
                <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 1024 1024" aria-hidden="true" focusable="false"><path fill="currentColor" d="M928 160H96c-17.7 0-32 14.3-32 32v640c0 17.7 14.3 32 32 32h832c17.7 0 32-14.3 32-32V192c0-17.7-14.3-32-32-32m-40 110.8V792H136V270.8l-27.6-21.5l39.3-50.5l42.8 33.3h643.1l42.8-33.3l39.3 50.5zM833.6 232L512 482L190.4 232l-42.8-33.3l-39.3 50.5l27.6 21.5l341.6 265.6a55.99 55.99 0 0 0 68.7 0L888 270.8l27.6-21.5l-39.3-50.5z"></path></svg>
              </a>
            
          </td>
          <td>
            
          </td>
          <td class="data-table__hide-mobile data-table__num">
            2016
          </td>
          <td class="data-table__hide-mobile data-table__num">
            1
          </td>
          <td class="data-table__hide-mobile">
            
          </td>
        </tr>
        
        <tr>
          <td>
            <a href="/countries/MEX/" class="data-table__country-cell">
              <img class="data-table__country-flag" src="/assets/images/countries/flags/mex.svg" alt="">
              <span class="data-table__country-full">Mexico</span><span class="data-table__country-iso">MEX</span>
            </a>
          </td>
          <td>
            
              Maria Guadalupe Russell Noriega
            
          </td>
          <td>
            
              <a href="mailto:mgrussell@uas.edu.mx" class="js-contact-email" data-email-user="mgrussell" data-email-domain="uas.edu.mx" aria-label="Email Maria Guadalupe Russell Noriega" title="Email">
                <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 1024 1024" aria-hidden="true" focusable="false"><path fill="currentColor" d="M928 160H96c-17.7 0-32 14.3-32 32v640c0 17.7 14.3 32 32 32h832c17.7 0 32-14.3 32-32V192c0-17.7-14.3-32-32-32m-40 110.8V792H136V270.8l-27.6-21.5l39.3-50.5l42.8 33.3h643.1l42.8-33.3l39.3 50.5zM833.6 232L512 482L190.4 232l-42.8-33.3l-39.3 50.5l27.6 21.5l341.6 265.6a55.99 55.99 0 0 0 68.7 0L888 270.8l27.6-21.5l-39.3-50.5z"></path></svg>
              </a>
            
          </td>
          <td>
            
              <a href="http://www.ommenlinea.org" target="_blank" rel="noopener" aria-label="Visit national MO website for Mexico (opens in new tab)"><span class="data-table__label-full">Visit ↗</span><span class="data-table__label-short">↗</span></a>
            
          </td>
          <td class="data-table__hide-mobile data-table__num">
            1981
          </td>
          <td class="data-table__hide-mobile data-table__num">
            41
          </td>
          <td class="data-table__hide-mobile">
            
              2005
            
          </td>
        </tr>
        
        <tr>
          <td>
            <a href="/countries/MKD/" class="data-table__country-cell">
              <img class="data-table__country-flag" src="/assets/images/countries/flags/mkd.svg" alt="">
              <span class="data-table__country-full">North Macedonia</span><span class="data-table__country-iso">MKD</span>
            </a>
          </td>
          <td>
            
              Gjorgji Markoski
            
          </td>
          <td>
            
              <a href="mailto:gorgi.markoski@gmail.com" class="js-contact-email" data-email-user="gorgi.markoski" data-email-domain="gmail.com" aria-label="Email Gjorgji Markoski" title="Email">
                <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 1024 1024" aria-hidden="true" focusable="false"><path fill="currentColor" d="M928 160H96c-17.7 0-32 14.3-32 32v640c0 17.7 14.3 32 32 32h832c17.7 0 32-14.3 32-32V192c0-17.7-14.3-32-32-32m-40 110.8V792H136V270.8l-27.6-21.5l39.3-50.5l42.8 33.3h643.1l42.8-33.3l39.3 50.5zM833.6 232L512 482L190.4 232l-42.8-33.3l-39.3 50.5l27.6 21.5l341.6 265.6a55.99 55.99 0 0 0 68.7 0L888 270.8l27.6-21.5l-39.3-50.5z"></path></svg>
              </a>
            
          </td>
          <td>
            
              <a href="https://smm.org.mk/" target="_blank" rel="noopener" aria-label="Visit national MO website for North Macedonia (opens in new tab)"><span class="data-table__label-full">Visit ↗</span><span class="data-table__label-short">↗</span></a>
            
          </td>
          <td class="data-table__hide-mobile data-table__num">
            1993
          </td>
          <td class="data-table__hide-mobile data-table__num">
            34
          </td>
          <td class="data-table__hide-mobile">
            
          </td>
        </tr>
        
        <tr>
          <td>
            <a href="/countries/MMR/" class="data-table__country-cell">
              <img class="data-table__country-flag" src="/assets/images/countries/flags/mmr.svg" alt="">
              <span class="data-table__country-full">Myanmar</span><span class="data-table__country-iso">MMR</span>
            </a>
          </td>
          <td>
            
              HTIN AUNG
            
          </td>
          <td>
            
              <a href="mailto:grandpahtinaung@gmail.com" class="js-contact-email" data-email-user="grandpahtinaung" data-email-domain="gmail.com" aria-label="Email HTIN AUNG" title="Email">
                <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 1024 1024" aria-hidden="true" focusable="false"><path fill="currentColor" d="M928 160H96c-17.7 0-32 14.3-32 32v640c0 17.7 14.3 32 32 32h832c17.7 0 32-14.3 32-32V192c0-17.7-14.3-32-32-32m-40 110.8V792H136V270.8l-27.6-21.5l39.3-50.5l42.8 33.3h643.1l42.8-33.3l39.3 50.5zM833.6 232L512 482L190.4 232l-42.8-33.3l-39.3 50.5l27.6 21.5l341.6 265.6a55.99 55.99 0 0 0 68.7 0L888 270.8l27.6-21.5l-39.3-50.5z"></path></svg>
              </a>
            
          </td>
          <td>
            
          </td>
          <td class="data-table__hide-mobile data-table__num">
            2016
          </td>
          <td class="data-table__hide-mobile data-table__num">
            9
          </td>
          <td class="data-table__hide-mobile">
            
          </td>
        </tr>
        
        <tr>
          <td>
            <a href="/countries/MNE/" class="data-table__country-cell">
              <img class="data-table__country-flag" src="/assets/images/countries/flags/mne.svg" alt="">
              <span class="data-table__country-full">Montenegro</span><span class="data-table__country-iso">MNE</span>
            </a>
          </td>
          <td>
            
              Tatjana Vujosevic
            
          </td>
          <td>
            
              <a href="mailto:tatjana.vujosevic@iccg.edu.me" class="js-contact-email" data-email-user="tatjana.vujosevic" data-email-domain="iccg.edu.me" aria-label="Email Tatjana Vujosevic" title="Email">
                <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 1024 1024" aria-hidden="true" focusable="false"><path fill="currentColor" d="M928 160H96c-17.7 0-32 14.3-32 32v640c0 17.7 14.3 32 32 32h832c17.7 0 32-14.3 32-32V192c0-17.7-14.3-32-32-32m-40 110.8V792H136V270.8l-27.6-21.5l39.3-50.5l42.8 33.3h643.1l42.8-33.3l39.3 50.5zM833.6 232L512 482L190.4 232l-42.8-33.3l-39.3 50.5l27.6 21.5l341.6 265.6a55.99 55.99 0 0 0 68.7 0L888 270.8l27.6-21.5l-39.3-50.5z"></path></svg>
              </a>
            
          </td>
          <td>
            
          </td>
          <td class="data-table__hide-mobile data-table__num">
            2007
          </td>
          <td class="data-table__hide-mobile data-table__num">
            19
          </td>
          <td class="data-table__hide-mobile">
            
          </td>
        </tr>
        
        <tr>
          <td>
            <a href="/countries/MNG/" class="data-table__country-cell">
              <img class="data-table__country-flag" src="/assets/images/countries/flags/mng.svg" alt="">
              <span class="data-table__country-full">Mongolia</span><span class="data-table__country-iso">MNG</span>
            </a>
          </td>
          <td>
            
              Otgonbayar Uuye
            
          </td>
          <td>
            
              <a href="mailto:otogo@mmoc.mn" class="js-contact-email" data-email-user="otogo" data-email-domain="mmoc.mn" aria-label="Email Otgonbayar Uuye" title="Email">
                <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 1024 1024" aria-hidden="true" focusable="false"><path fill="currentColor" d="M928 160H96c-17.7 0-32 14.3-32 32v640c0 17.7 14.3 32 32 32h832c17.7 0 32-14.3 32-32V192c0-17.7-14.3-32-32-32m-40 110.8V792H136V270.8l-27.6-21.5l39.3-50.5l42.8 33.3h643.1l42.8-33.3l39.3 50.5zM833.6 232L512 482L190.4 232l-42.8-33.3l-39.3 50.5l27.6 21.5l341.6 265.6a55.99 55.99 0 0 0 68.7 0L888 270.8l27.6-21.5l-39.3-50.5z"></path></svg>
              </a>
            
          </td>
          <td>
            
              <a href="http://www.mmo.mn" target="_blank" rel="noopener" aria-label="Visit national MO website for Mongolia (opens in new tab)"><span class="data-table__label-full">Visit ↗</span><span class="data-table__label-short">↗</span></a>
            
          </td>
          <td class="data-table__hide-mobile data-table__num">
            1964
          </td>
          <td class="data-table__hide-mobile data-table__num">
            55
          </td>
          <td class="data-table__hide-mobile">
            
              2029
            
          </td>
        </tr>
        
        <tr>
          <td>
            <a href="/countries/MOZ/" class="data-table__country-cell">
              <img class="data-table__country-flag" src="/assets/images/countries/flags/moz.svg" alt="">
              <span class="data-table__country-full">Mozambique</span><span class="data-table__country-iso">MOZ</span>
            </a>
          </td>
          <td>
            
              Luis de Nascimento Paulo
            
          </td>
          <td>
            
              <a href="mailto:nascimento@mined.gov.mz" class="js-contact-email" data-email-user="nascimento" data-email-domain="mined.gov.mz" aria-label="Email Luis de Nascimento Paulo" title="Email">
                <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 1024 1024" aria-hidden="true" focusable="false"><path fill="currentColor" d="M928 160H96c-17.7 0-32 14.3-32 32v640c0 17.7 14.3 32 32 32h832c17.7 0 32-14.3 32-32V192c0-17.7-14.3-32-32-32m-40 110.8V792H136V270.8l-27.6-21.5l39.3-50.5l42.8 33.3h643.1l42.8-33.3l39.3 50.5zM833.6 232L512 482L190.4 232l-42.8-33.3l-39.3 50.5l27.6 21.5l341.6 265.6a55.99 55.99 0 0 0 68.7 0L888 270.8l27.6-21.5l-39.3-50.5z"></path></svg>
              </a>
            
          </td>
          <td>
            
          </td>
          <td class="data-table__hide-mobile data-table__num">
            2004
          </td>
          <td class="data-table__hide-mobile data-table__num">
            3
          </td>
          <td class="data-table__hide-mobile">
            
          </td>
        </tr>
        
        <tr>
          <td>
            <a href="/countries/MRT/" class="data-table__country-cell">
              <img class="data-table__country-flag" src="/assets/images/countries/flags/mrt.svg" alt="">
              <span class="data-table__country-full">Mauritania</span><span class="data-table__country-iso">MRT</span>
            </a>
          </td>
          <td>
            
              Horma Ould HAMOUD
            
          </td>
          <td>
            
              <a href="mailto:horma04@yahoo.fr" class="js-contact-email" data-email-user="horma04" data-email-domain="yahoo.fr" aria-label="Email Horma Ould HAMOUD" title="Email">
                <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 1024 1024" aria-hidden="true" focusable="false"><path fill="currentColor" d="M928 160H96c-17.7 0-32 14.3-32 32v640c0 17.7 14.3 32 32 32h832c17.7 0 32-14.3 32-32V192c0-17.7-14.3-32-32-32m-40 110.8V792H136V270.8l-27.6-21.5l39.3-50.5l42.8 33.3h643.1l42.8-33.3l39.3 50.5zM833.6 232L512 482L190.4 232l-42.8-33.3l-39.3 50.5l27.6 21.5l341.6 265.6a55.99 55.99 0 0 0 68.7 0L888 270.8l27.6-21.5l-39.3-50.5z"></path></svg>
              </a>
            
          </td>
          <td>
            
              <a href="https://maurimath.net/Olympiades.php" target="_blank" rel="noopener" aria-label="Visit national MO website for Mauritania (opens in new tab)"><span class="data-table__label-full">Visit ↗</span><span class="data-table__label-short">↗</span></a>
            
          </td>
          <td class="data-table__hide-mobile data-table__num">
            2009
          </td>
          <td class="data-table__hide-mobile data-table__num">
            4
          </td>
          <td class="data-table__hide-mobile">
            
          </td>
        </tr>
        
        <tr>
          <td>
            <a href="/countries/MUS/" class="data-table__country-cell">
              <img class="data-table__country-flag" src="/assets/images/countries/flags/mus.svg" alt="">
              <span class="data-table__country-full">Mauritius</span><span class="data-table__country-iso">MUS</span>
            </a>
          </td>
          <td>
            
          </td>
          <td>
            
          </td>
          <td>
            
          </td>
          <td class="data-table__hide-mobile data-table__num">
            
          </td>
          <td class="data-table__hide-mobile data-table__num">
            0
          </td>
          <td class="data-table__hide-mobile">
            
          </td>
        </tr>
        
        <tr>
          <td>
            <a href="/countries/NAM/" class="data-table__country-cell">
              <img class="data-table__country-flag" src="/assets/images/countries/flags/nam.svg" alt="">
              <span class="data-table__country-full">Namibia</span><span class="data-table__country-iso">NAM</span>
            </a>
          </td>
          <td>
            
              Martin Mugochi
            
          </td>
          <td>
            
              <a href="mailto:mmugochi@unam.na" class="js-contact-email" data-email-user="mmugochi" data-email-domain="unam.na" aria-label="Email Martin Mugochi" title="Email">
                <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 1024 1024" aria-hidden="true" focusable="false"><path fill="currentColor" d="M928 160H96c-17.7 0-32 14.3-32 32v640c0 17.7 14.3 32 32 32h832c17.7 0 32-14.3 32-32V192c0-17.7-14.3-32-32-32m-40 110.8V792H136V270.8l-27.6-21.5l39.3-50.5l42.8 33.3h643.1l42.8-33.3l39.3 50.5zM833.6 232L512 482L190.4 232l-42.8-33.3l-39.3 50.5l27.6 21.5l341.6 265.6a55.99 55.99 0 0 0 68.7 0L888 270.8l27.6-21.5l-39.3-50.5z"></path></svg>
              </a>
            
          </td>
          <td>
            
              <a href="https://nmo.ncrst.na/" target="_blank" rel="noopener" aria-label="Visit national MO website for Namibia (opens in new tab)"><span class="data-table__label-full">Visit ↗</span><span class="data-table__label-short">↗</span></a>
            
          </td>
          <td class="data-table__hide-mobile data-table__num">
            2025
          </td>
          <td class="data-table__hide-mobile data-table__num">
            2
          </td>
          <td class="data-table__hide-mobile">
            
          </td>
        </tr>
        
        <tr class="data-table__row--inactive">
          <td>
            <a href="/countries/NCY/" class="data-table__country-cell">
              <img class="data-table__country-flag" src="/assets/images/countries/flags/ncy.svg" alt="">
              <span class="data-table__country-full">Turkish Republic of Northern Cyprus</span><span class="data-table__country-iso">NCY</span>
            </a>
          </td>
          <td>
            
          </td>
          <td>
            
          </td>
          <td>
            
          </td>
          <td class="data-table__hide-mobile data-table__num">
            1993
          </td>
          <td class="data-table__hide-mobile data-table__num">
            1
          </td>
          <td class="data-table__hide-mobile">
            
          </td>
        </tr>
        
        <tr>
          <td>
            <a href="/countries/NGA/" class="data-table__country-cell">
              <img class="data-table__country-flag" src="/assets/images/countries/flags/nga.svg" alt="">
              <span class="data-table__country-full">Nigeria</span><span class="data-table__country-iso">NGA</span>
            </a>
          </td>
          <td>
            
              Benjamin Oyediran Oyelami
            
          </td>
          <td>
            
              <a href="mailto:boyelami2000@yahoo.com" class="js-contact-email" data-email-user="boyelami2000" data-email-domain="yahoo.com" aria-label="Email Benjamin Oyediran Oyelami" title="Email">
                <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 1024 1024" aria-hidden="true" focusable="false"><path fill="currentColor" d="M928 160H96c-17.7 0-32 14.3-32 32v640c0 17.7 14.3 32 32 32h832c17.7 0 32-14.3 32-32V192c0-17.7-14.3-32-32-32m-40 110.8V792H136V270.8l-27.6-21.5l39.3-50.5l42.8 33.3h643.1l42.8-33.3l39.3 50.5zM833.6 232L512 482L190.4 232l-42.8-33.3l-39.3 50.5l27.6 21.5l341.6 265.6a55.99 55.99 0 0 0 68.7 0L888 270.8l27.6-21.5l-39.3-50.5z"></path></svg>
              </a>
            
          </td>
          <td>
            
          </td>
          <td class="data-table__hide-mobile data-table__num">
            2006
          </td>
          <td class="data-table__hide-mobile data-table__num">
            14
          </td>
          <td class="data-table__hide-mobile">
            
          </td>
        </tr>
        
        <tr>
          <td>
            <a href="/countries/NIC/" class="data-table__country-cell">
              <img class="data-table__country-flag" src="/assets/images/countries/flags/nic.svg" alt="">
              <span class="data-table__country-full">Nicaragua</span><span class="data-table__country-iso">NIC</span>
            </a>
          </td>
          <td>
            
              Hank de Jesús Espinoza Serrano
            
          </td>
          <td>
            
              <a href="mailto:hankchuus@yahoo.com" class="js-contact-email" data-email-user="hankchuus" data-email-domain="yahoo.com" aria-label="Email Hank de Jesús Espinoza Serrano" title="Email">
                <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 1024 1024" aria-hidden="true" focusable="false"><path fill="currentColor" d="M928 160H96c-17.7 0-32 14.3-32 32v640c0 17.7 14.3 32 32 32h832c17.7 0 32-14.3 32-32V192c0-17.7-14.3-32-32-32m-40 110.8V792H136V270.8l-27.6-21.5l39.3-50.5l42.8 33.3h643.1l42.8-33.3l39.3 50.5zM833.6 232L512 482L190.4 232l-42.8-33.3l-39.3 50.5l27.6 21.5l341.6 265.6a55.99 55.99 0 0 0 68.7 0L888 270.8l27.6-21.5l-39.3-50.5z"></path></svg>
              </a>
            
          </td>
          <td>
            
              <a href="http://www.asjtnic.org/" target="_blank" rel="noopener" aria-label="Visit national MO website for Nicaragua (opens in new tab)"><span class="data-table__label-full">Visit ↗</span><span class="data-table__label-short">↗</span></a>
            
          </td>
          <td class="data-table__hide-mobile data-table__num">
            1987
          </td>
          <td class="data-table__hide-mobile data-table__num">
            10
          </td>
          <td class="data-table__hide-mobile">
            
          </td>
        </tr>
        
        <tr>
          <td>
            <a href="/countries/NLD/" class="data-table__country-cell">
              <img class="data-table__country-flag" src="/assets/images/countries/flags/nld.svg" alt="">
              <span class="data-table__country-full">Netherlands</span><span class="data-table__country-iso">NLD</span>
            </a>
          </td>
          <td>
            
              Quintijn Puite
            
          </td>
          <td>
            
              <a href="mailto:olympiade@wiskundeolympiade.nl" class="js-contact-email" data-email-user="olympiade" data-email-domain="wiskundeolympiade.nl" aria-label="Email Quintijn Puite" title="Email">
                <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 1024 1024" aria-hidden="true" focusable="false"><path fill="currentColor" d="M928 160H96c-17.7 0-32 14.3-32 32v640c0 17.7 14.3 32 32 32h832c17.7 0 32-14.3 32-32V192c0-17.7-14.3-32-32-32m-40 110.8V792H136V270.8l-27.6-21.5l39.3-50.5l42.8 33.3h643.1l42.8-33.3l39.3 50.5zM833.6 232L512 482L190.4 232l-42.8-33.3l-39.3 50.5l27.6 21.5l341.6 265.6a55.99 55.99 0 0 0 68.7 0L888 270.8l27.6-21.5l-39.3-50.5z"></path></svg>
              </a>
            
          </td>
          <td>
            
              <a href="http://wiskundeolympiade.nl/" target="_blank" rel="noopener" aria-label="Visit national MO website for Netherlands (opens in new tab)"><span class="data-table__label-full">Visit ↗</span><span class="data-table__label-short">↗</span></a>
            
          </td>
          <td class="data-table__hide-mobile data-table__num">
            1969
          </td>
          <td class="data-table__hide-mobile data-table__num">
            56
          </td>
          <td class="data-table__hide-mobile">
            
              2011
            
          </td>
        </tr>
        
        <tr>
          <td>
            <a href="/countries/NOR/" class="data-table__country-cell">
              <img class="data-table__country-flag" src="/assets/images/countries/flags/nor.svg" alt="">
              <span class="data-table__country-full">Norway</span><span class="data-table__country-iso">NOR</span>
            </a>
          </td>
          <td>
            
              Dag Wessel-Berg
            
          </td>
          <td>
            
              <a href="mailto:dag.wessel-berg@ntnu.no" class="js-contact-email" data-email-user="dag.wessel-berg" data-email-domain="ntnu.no" aria-label="Email Dag Wessel-Berg" title="Email">
                <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 1024 1024" aria-hidden="true" focusable="false"><path fill="currentColor" d="M928 160H96c-17.7 0-32 14.3-32 32v640c0 17.7 14.3 32 32 32h832c17.7 0 32-14.3 32-32V192c0-17.7-14.3-32-32-32m-40 110.8V792H136V270.8l-27.6-21.5l39.3-50.5l42.8 33.3h643.1l42.8-33.3l39.3 50.5zM833.6 232L512 482L190.4 232l-42.8-33.3l-39.3 50.5l27.6 21.5l341.6 265.6a55.99 55.99 0 0 0 68.7 0L888 270.8l27.6-21.5l-39.3-50.5z"></path></svg>
              </a>
            
          </td>
          <td>
            
              <a href="https://www.abelkonkurransen.no" target="_blank" rel="noopener" aria-label="Visit national MO website for Norway (opens in new tab)"><span class="data-table__label-full">Visit ↗</span><span class="data-table__label-short">↗</span></a>
            
          </td>
          <td class="data-table__hide-mobile data-table__num">
            1984
          </td>
          <td class="data-table__hide-mobile data-table__num">
            43
          </td>
          <td class="data-table__hide-mobile">
            
              2022
            
          </td>
        </tr>
        
        <tr>
          <td>
            <a href="/countries/NPL/" class="data-table__country-cell">
              <img class="data-table__country-flag" src="/assets/images/countries/flags/npl.svg" alt="">
              <span class="data-table__country-full">Nepal</span><span class="data-table__country-iso">NPL</span>
            </a>
          </td>
          <td>
            
              Binod Prasad Pant
            
          </td>
          <td>
            
              <a href="mailto:binod@kusoed.edu.np" class="js-contact-email" data-email-user="binod" data-email-domain="kusoed.edu.np" aria-label="Email Binod Prasad Pant" title="Email">
                <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 1024 1024" aria-hidden="true" focusable="false"><path fill="currentColor" d="M928 160H96c-17.7 0-32 14.3-32 32v640c0 17.7 14.3 32 32 32h832c17.7 0 32-14.3 32-32V192c0-17.7-14.3-32-32-32m-40 110.8V792H136V270.8l-27.6-21.5l39.3-50.5l42.8 33.3h643.1l42.8-33.3l39.3 50.5zM833.6 232L512 482L190.4 232l-42.8-33.3l-39.3 50.5l27.6 21.5l341.6 265.6a55.99 55.99 0 0 0 68.7 0L888 270.8l27.6-21.5l-39.3-50.5z"></path></svg>
              </a>
            
          </td>
          <td>
            
              <a href="https://www.mathassociationnepal.org.np/" target="_blank" rel="noopener" aria-label="Visit national MO website for Nepal (opens in new tab)"><span class="data-table__label-full">Visit ↗</span><span class="data-table__label-short">↗</span></a>
            
          </td>
          <td class="data-table__hide-mobile data-table__num">
            2017
          </td>
          <td class="data-table__hide-mobile data-table__num">
            10
          </td>
          <td class="data-table__hide-mobile">
            
          </td>
        </tr>
        
        <tr>
          <td>
            <a href="/countries/NZL/" class="data-table__country-cell">
              <img class="data-table__country-flag" src="/assets/images/countries/flags/nzl.svg" alt="">
              <span class="data-table__country-full">New Zealand</span><span class="data-table__country-iso">NZL</span>
            </a>
          </td>
          <td>
            
              Kevin Shen
            
          </td>
          <td>
            
              <a href="mailto:info@mathsolympiad.org.nz" class="js-contact-email" data-email-user="info" data-email-domain="mathsolympiad.org.nz" aria-label="Email Kevin Shen" title="Email">
                <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 1024 1024" aria-hidden="true" focusable="false"><path fill="currentColor" d="M928 160H96c-17.7 0-32 14.3-32 32v640c0 17.7 14.3 32 32 32h832c17.7 0 32-14.3 32-32V192c0-17.7-14.3-32-32-32m-40 110.8V792H136V270.8l-27.6-21.5l39.3-50.5l42.8 33.3h643.1l42.8-33.3l39.3 50.5zM833.6 232L512 482L190.4 232l-42.8-33.3l-39.3 50.5l27.6 21.5l341.6 265.6a55.99 55.99 0 0 0 68.7 0L888 270.8l27.6-21.5l-39.3-50.5z"></path></svg>
              </a>
            
          </td>
          <td>
            
              <a href="https://www.mathsolympiad.org.nz" target="_blank" rel="noopener" aria-label="Visit national MO website for New Zealand (opens in new tab)"><span class="data-table__label-full">Visit ↗</span><span class="data-table__label-short">↗</span></a>
            
          </td>
          <td class="data-table__hide-mobile data-table__num">
            1988
          </td>
          <td class="data-table__hide-mobile data-table__num">
            39
          </td>
          <td class="data-table__hide-mobile">
            
          </td>
        </tr>
        
        <tr>
          <td>
            <a href="/countries/OMN/" class="data-table__country-cell">
              <img class="data-table__country-flag" src="/assets/images/countries/flags/omn.svg" alt="">
              <span class="data-table__country-full">Oman</span><span class="data-table__country-iso">OMN</span>
            </a>
          </td>
          <td>
            
              Zakiya Alajm
            
          </td>
          <td>
            
              <a href="mailto:Sohar7777@moe.om" class="js-contact-email" data-email-user="Sohar7777" data-email-domain="moe.om" aria-label="Email Zakiya Alajm" title="Email">
                <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 1024 1024" aria-hidden="true" focusable="false"><path fill="currentColor" d="M928 160H96c-17.7 0-32 14.3-32 32v640c0 17.7 14.3 32 32 32h832c17.7 0 32-14.3 32-32V192c0-17.7-14.3-32-32-32m-40 110.8V792H136V270.8l-27.6-21.5l39.3-50.5l42.8 33.3h643.1l42.8-33.3l39.3 50.5zM833.6 232L512 482L190.4 232l-42.8-33.3l-39.3 50.5l27.6 21.5l341.6 265.6a55.99 55.99 0 0 0 68.7 0L888 270.8l27.6-21.5l-39.3-50.5z"></path></svg>
              </a>
            
          </td>
          <td>
            
          </td>
          <td class="data-table__hide-mobile data-table__num">
            2020
          </td>
          <td class="data-table__hide-mobile data-table__num">
            6
          </td>
          <td class="data-table__hide-mobile">
            
          </td>
        </tr>
        
        <tr>
          <td>
            <a href="/countries/PAK/" class="data-table__country-cell">
              <img class="data-table__country-flag" src="/assets/images/countries/flags/pak.svg" alt="">
              <span class="data-table__country-full">Pakistan</span><span class="data-table__country-iso">PAK</span>
            </a>
          </td>
          <td>
            
              Sarfraz Ahmad
            
          </td>
          <td>
            
              <a href="mailto:sarfrazahmad@cuilahore.edu.pk" class="js-contact-email" data-email-user="sarfrazahmad" data-email-domain="cuilahore.edu.pk" aria-label="Email Sarfraz Ahmad" title="Email">
                <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 1024 1024" aria-hidden="true" focusable="false"><path fill="currentColor" d="M928 160H96c-17.7 0-32 14.3-32 32v640c0 17.7 14.3 32 32 32h832c17.7 0 32-14.3 32-32V192c0-17.7-14.3-32-32-32m-40 110.8V792H136V270.8l-27.6-21.5l39.3-50.5l42.8 33.3h643.1l42.8-33.3l39.3 50.5zM833.6 232L512 482L190.4 232l-42.8-33.3l-39.3 50.5l27.6 21.5l341.6 265.6a55.99 55.99 0 0 0 68.7 0L888 270.8l27.6-21.5l-39.3-50.5z"></path></svg>
              </a>
            
          </td>
          <td>
            
          </td>
          <td class="data-table__hide-mobile data-table__num">
            2005
          </td>
          <td class="data-table__hide-mobile data-table__num">
            21
          </td>
          <td class="data-table__hide-mobile">
            
          </td>
        </tr>
        
        <tr>
          <td>
            <a href="/countries/PAN/" class="data-table__country-cell">
              <img class="data-table__country-flag" src="/assets/images/countries/flags/pan.svg" alt="">
              <span class="data-table__country-full">Panama</span><span class="data-table__country-iso">PAN</span>
            </a>
          </td>
          <td>
            
              Pedro A. Marrone G.
            
          </td>
          <td>
            
              <a href="mailto:pmarrone@opm.org.pa" class="js-contact-email" data-email-user="pmarrone" data-email-domain="opm.org.pa" aria-label="Email Pedro A. Marrone G." title="Email">
                <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 1024 1024" aria-hidden="true" focusable="false"><path fill="currentColor" d="M928 160H96c-17.7 0-32 14.3-32 32v640c0 17.7 14.3 32 32 32h832c17.7 0 32-14.3 32-32V192c0-17.7-14.3-32-32-32m-40 110.8V792H136V270.8l-27.6-21.5l39.3-50.5l42.8 33.3h643.1l42.8-33.3l39.3 50.5zM833.6 232L512 482L190.4 232l-42.8-33.3l-39.3 50.5l27.6 21.5l341.6 265.6a55.99 55.99 0 0 0 68.7 0L888 270.8l27.6-21.5l-39.3-50.5z"></path></svg>
              </a>
            
          </td>
          <td>
            
              <a href="http://www.opm.org.pa/" target="_blank" rel="noopener" aria-label="Visit national MO website for Panama (opens in new tab)"><span class="data-table__label-full">Visit ↗</span><span class="data-table__label-short">↗</span></a>
            
          </td>
          <td class="data-table__hide-mobile data-table__num">
            1987
          </td>
          <td class="data-table__hide-mobile data-table__num">
            18
          </td>
          <td class="data-table__hide-mobile">
            
          </td>
        </tr>
        
        <tr>
          <td>
            <a href="/countries/PAR/" class="data-table__country-cell">
              <img class="data-table__country-flag" src="/assets/images/countries/flags/par.svg" alt="">
              <span class="data-table__country-full">Paraguay</span><span class="data-table__country-iso">PAR</span>
            </a>
          </td>
          <td>
            
              Joel Prieto
            
          </td>
          <td>
            
              <a href="mailto:joel.omapa@gmail.com" class="js-contact-email" data-email-user="joel.omapa" data-email-domain="gmail.com" aria-label="Email Joel Prieto" title="Email">
                <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 1024 1024" aria-hidden="true" focusable="false"><path fill="currentColor" d="M928 160H96c-17.7 0-32 14.3-32 32v640c0 17.7 14.3 32 32 32h832c17.7 0 32-14.3 32-32V192c0-17.7-14.3-32-32-32m-40 110.8V792H136V270.8l-27.6-21.5l39.3-50.5l42.8 33.3h643.1l42.8-33.3l39.3 50.5zM833.6 232L512 482L190.4 232l-42.8-33.3l-39.3 50.5l27.6 21.5l341.6 265.6a55.99 55.99 0 0 0 68.7 0L888 270.8l27.6-21.5l-39.3-50.5z"></path></svg>
              </a>
            
          </td>
          <td>
            
              <a href="http://www.omapa.org.py" target="_blank" rel="noopener" aria-label="Visit national MO website for Paraguay (opens in new tab)"><span class="data-table__label-full">Visit ↗</span><span class="data-table__label-short">↗</span></a>
            
          </td>
          <td class="data-table__hide-mobile data-table__num">
            1997
          </td>
          <td class="data-table__hide-mobile data-table__num">
            28
          </td>
          <td class="data-table__hide-mobile">
            
          </td>
        </tr>
        
        <tr>
          <td>
            <a href="/countries/PER/" class="data-table__country-cell">
              <img class="data-table__country-flag" src="/assets/images/countries/flags/per.svg" alt="">
              <span class="data-table__country-full">Peru</span><span class="data-table__country-iso">PER</span>
            </a>
          </td>
          <td>
            
              Comisión de Olimpiadas de la Sociedad Matemática Peruana
            
          </td>
          <td>
            
              <a href="mailto:olimpiadas.matematicas@pucp.edu.pe" class="js-contact-email" data-email-user="olimpiadas.matematicas" data-email-domain="pucp.edu.pe" aria-label="Email Comisión de Olimpiadas de la Sociedad Matemática Peruana" title="Email">
                <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 1024 1024" aria-hidden="true" focusable="false"><path fill="currentColor" d="M928 160H96c-17.7 0-32 14.3-32 32v640c0 17.7 14.3 32 32 32h832c17.7 0 32-14.3 32-32V192c0-17.7-14.3-32-32-32m-40 110.8V792H136V270.8l-27.6-21.5l39.3-50.5l42.8 33.3h643.1l42.8-33.3l39.3 50.5zM833.6 232L512 482L190.4 232l-42.8-33.3l-39.3 50.5l27.6 21.5l341.6 265.6a55.99 55.99 0 0 0 68.7 0L888 270.8l27.6-21.5l-39.3-50.5z"></path></svg>
              </a>
            
          </td>
          <td>
            
              <a href="https://selectivos-peru.blogspot.com/" target="_blank" rel="noopener" aria-label="Visit national MO website for Peru (opens in new tab)"><span class="data-table__label-full">Visit ↗</span><span class="data-table__label-short">↗</span></a>
            
          </td>
          <td class="data-table__hide-mobile data-table__num">
            1987
          </td>
          <td class="data-table__hide-mobile data-table__num">
            33
          </td>
          <td class="data-table__hide-mobile">
            
          </td>
        </tr>
        
        <tr>
          <td>
            <a href="/countries/PHI/" class="data-table__country-cell">
              <img class="data-table__country-flag" src="/assets/images/countries/flags/phi.svg" alt="">
              <span class="data-table__country-full">Philippines</span><span class="data-table__country-iso">PHI</span>
            </a>
          </td>
          <td>
            
              Richard Eden
            
          </td>
          <td>
            
              <a href="mailto:imo.team.philippines@gmail.com" class="js-contact-email" data-email-user="imo.team.philippines" data-email-domain="gmail.com" aria-label="Email Richard Eden" title="Email">
                <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 1024 1024" aria-hidden="true" focusable="false"><path fill="currentColor" d="M928 160H96c-17.7 0-32 14.3-32 32v640c0 17.7 14.3 32 32 32h832c17.7 0 32-14.3 32-32V192c0-17.7-14.3-32-32-32m-40 110.8V792H136V270.8l-27.6-21.5l39.3-50.5l42.8 33.3h643.1l42.8-33.3l39.3 50.5zM833.6 232L512 482L190.4 232l-42.8-33.3l-39.3 50.5l27.6 21.5l341.6 265.6a55.99 55.99 0 0 0 68.7 0L888 270.8l27.6-21.5l-39.3-50.5z"></path></svg>
              </a>
            
          </td>
          <td>
            
              <a href="https://pmo.ph" target="_blank" rel="noopener" aria-label="Visit national MO website for Philippines (opens in new tab)"><span class="data-table__label-full">Visit ↗</span><span class="data-table__label-short">↗</span></a>
            
          </td>
          <td class="data-table__hide-mobile data-table__num">
            1988
          </td>
          <td class="data-table__hide-mobile data-table__num">
            38
          </td>
          <td class="data-table__hide-mobile">
            
          </td>
        </tr>
        
        <tr>
          <td>
            <a href="/countries/POL/" class="data-table__country-cell">
              <img class="data-table__country-flag" src="/assets/images/countries/flags/pol.svg" alt="">
              <span class="data-table__country-full">Poland</span><span class="data-table__country-iso">POL</span>
            </a>
          </td>
          <td>
            
              Tomasz Cieśla
            
          </td>
          <td>
            
              <a href="mailto:t.ciesla@mimuw.edu.pl" class="js-contact-email" data-email-user="t.ciesla" data-email-domain="mimuw.edu.pl" aria-label="Email Tomasz Cieśla" title="Email">
                <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 1024 1024" aria-hidden="true" focusable="false"><path fill="currentColor" d="M928 160H96c-17.7 0-32 14.3-32 32v640c0 17.7 14.3 32 32 32h832c17.7 0 32-14.3 32-32V192c0-17.7-14.3-32-32-32m-40 110.8V792H136V270.8l-27.6-21.5l39.3-50.5l42.8 33.3h643.1l42.8-33.3l39.3 50.5zM833.6 232L512 482L190.4 232l-42.8-33.3l-39.3 50.5l27.6 21.5l341.6 265.6a55.99 55.99 0 0 0 68.7 0L888 270.8l27.6-21.5l-39.3-50.5z"></path></svg>
              </a>
            
          </td>
          <td>
            
              <a href="http://om.sem.edu.pl/" target="_blank" rel="noopener" aria-label="Visit national MO website for Poland (opens in new tab)"><span class="data-table__label-full">Visit ↗</span><span class="data-table__label-short">↗</span></a>
            
          </td>
          <td class="data-table__hide-mobile data-table__num">
            1959
          </td>
          <td class="data-table__hide-mobile data-table__num">
            66
          </td>
          <td class="data-table__hide-mobile">
            
              1963, 1972, 1986
            
          </td>
        </tr>
        
        <tr>
          <td>
            <a href="/countries/POR/" class="data-table__country-cell">
              <img class="data-table__country-flag" src="/assets/images/countries/flags/por.svg" alt="">
              <span class="data-table__country-full">Portugal</span><span class="data-table__country-iso">POR</span>
            </a>
          </td>
          <td>
            
              Joana Teles
            
          </td>
          <td>
            
              <a href="mailto:jteles@mat.uc.pt" class="js-contact-email" data-email-user="jteles" data-email-domain="mat.uc.pt" aria-label="Email Joana Teles" title="Email">
                <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 1024 1024" aria-hidden="true" focusable="false"><path fill="currentColor" d="M928 160H96c-17.7 0-32 14.3-32 32v640c0 17.7 14.3 32 32 32h832c17.7 0 32-14.3 32-32V192c0-17.7-14.3-32-32-32m-40 110.8V792H136V270.8l-27.6-21.5l39.3-50.5l42.8 33.3h643.1l42.8-33.3l39.3 50.5zM833.6 232L512 482L190.4 232l-42.8-33.3l-39.3 50.5l27.6 21.5l341.6 265.6a55.99 55.99 0 0 0 68.7 0L888 270.8l27.6-21.5l-39.3-50.5z"></path></svg>
              </a>
            
          </td>
          <td>
            
              <a href="http://www.spm.pt/olimpiadas" target="_blank" rel="noopener" aria-label="Visit national MO website for Portugal (opens in new tab)"><span class="data-table__label-full">Visit ↗</span><span class="data-table__label-short">↗</span></a>
            
          </td>
          <td class="data-table__hide-mobile data-table__num">
            1989
          </td>
          <td class="data-table__hide-mobile data-table__num">
            38
          </td>
          <td class="data-table__hide-mobile">
            
          </td>
        </tr>
        
        <tr>
          <td>
            <a href="/countries/PRI/" class="data-table__country-cell">
              <img class="data-table__country-flag" src="/assets/images/countries/flags/pri.svg" alt="">
              <span class="data-table__country-full">Puerto Rico</span><span class="data-table__country-iso">PRI</span>
            </a>
          </td>
          <td>
            
              Luis F. Cáceres
            
          </td>
          <td>
            
              <a href="mailto:luis.caceres1@upr.edu" class="js-contact-email" data-email-user="luis.caceres1" data-email-domain="upr.edu" aria-label="Email Luis F. Cáceres" title="Email">
                <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 1024 1024" aria-hidden="true" focusable="false"><path fill="currentColor" d="M928 160H96c-17.7 0-32 14.3-32 32v640c0 17.7 14.3 32 32 32h832c17.7 0 32-14.3 32-32V192c0-17.7-14.3-32-32-32m-40 110.8V792H136V270.8l-27.6-21.5l39.3-50.5l42.8 33.3h643.1l42.8-33.3l39.3 50.5zM833.6 232L512 482L190.4 232l-42.8-33.3l-39.3 50.5l27.6 21.5l341.6 265.6a55.99 55.99 0 0 0 68.7 0L888 270.8l27.6-21.5l-39.3-50.5z"></path></svg>
              </a>
            
          </td>
          <td>
            
              <a href="http://om.pr" target="_blank" rel="noopener" aria-label="Visit national MO website for Puerto Rico (opens in new tab)"><span class="data-table__label-full">Visit ↗</span><span class="data-table__label-short">↗</span></a>
            
          </td>
          <td class="data-table__hide-mobile data-table__num">
            1997
          </td>
          <td class="data-table__hide-mobile data-table__num">
            27
          </td>
          <td class="data-table__hide-mobile">
            
          </td>
        </tr>
        
        <tr>
          <td>
            <a href="/countries/PRK/" class="data-table__country-cell">
              <img class="data-table__country-flag" src="/assets/images/countries/flags/prk.svg" alt="">
              <span class="data-table__country-full">Democratic People's Republic of Korea</span><span class="data-table__country-iso">PRK</span>
            </a>
          </td>
          <td>
            
              Ri Kyong Ho
            
          </td>
          <td>
            
              <a href="mailto:drkedu@163.com" class="js-contact-email" data-email-user="drkedu" data-email-domain="163.com" aria-label="Email Ri Kyong Ho" title="Email">
                <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 1024 1024" aria-hidden="true" focusable="false"><path fill="currentColor" d="M928 160H96c-17.7 0-32 14.3-32 32v640c0 17.7 14.3 32 32 32h832c17.7 0 32-14.3 32-32V192c0-17.7-14.3-32-32-32m-40 110.8V792H136V270.8l-27.6-21.5l39.3-50.5l42.8 33.3h643.1l42.8-33.3l39.3 50.5zM833.6 232L512 482L190.4 232l-42.8-33.3l-39.3 50.5l27.6 21.5l341.6 265.6a55.99 55.99 0 0 0 68.7 0L888 270.8l27.6-21.5l-39.3-50.5z"></path></svg>
              </a>
            
          </td>
          <td>
            
          </td>
          <td class="data-table__hide-mobile data-table__num">
            1990
          </td>
          <td class="data-table__hide-mobile data-table__num">
            13
          </td>
          <td class="data-table__hide-mobile">
            
          </td>
        </tr>
        
        <tr>
          <td>
            <a href="/countries/PSE/" class="data-table__country-cell">
              <img class="data-table__country-flag" src="/assets/images/countries/flags/pse.svg" alt="">
              <span class="data-table__country-full">Palestine</span><span class="data-table__country-iso">PSE</span>
            </a>
          </td>
          <td>
            
              Dr. Mohamed Khalil
            
          </td>
          <td>
            
              <a href="mailto:imo.palestine@moe.edu.ps" class="js-contact-email" data-email-user="imo.palestine" data-email-domain="moe.edu.ps" aria-label="Email Dr. Mohamed Khalil" title="Email">
                <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 1024 1024" aria-hidden="true" focusable="false"><path fill="currentColor" d="M928 160H96c-17.7 0-32 14.3-32 32v640c0 17.7 14.3 32 32 32h832c17.7 0 32-14.3 32-32V192c0-17.7-14.3-32-32-32m-40 110.8V792H136V270.8l-27.6-21.5l39.3-50.5l42.8 33.3h643.1l42.8-33.3l39.3 50.5zM833.6 232L512 482L190.4 232l-42.8-33.3l-39.3 50.5l27.6 21.5l341.6 265.6a55.99 55.99 0 0 0 68.7 0L888 270.8l27.6-21.5l-39.3-50.5z"></path></svg>
              </a>
            
          </td>
          <td>
            
              <a href="https://moe.edu.ps/" target="_blank" rel="noopener" aria-label="Visit national MO website for Palestine (opens in new tab)"><span class="data-table__label-full">Visit ↗</span><span class="data-table__label-short">↗</span></a>
            
          </td>
          <td class="data-table__hide-mobile data-table__num">
            2022
          </td>
          <td class="data-table__hide-mobile data-table__num">
            3
          </td>
          <td class="data-table__hide-mobile">
            
          </td>
        </tr>
        
        <tr>
          <td>
            <a href="/countries/QAT/" class="data-table__country-cell">
              <img class="data-table__country-flag" src="/assets/images/countries/flags/qat.svg" alt="">
              <span class="data-table__country-full">Qatar</span><span class="data-table__country-iso">QAT</span>
            </a>
          </td>
          <td>
            
          </td>
          <td>
            
          </td>
          <td>
            
          </td>
          <td class="data-table__hide-mobile data-table__num">
            2025
          </td>
          <td class="data-table__hide-mobile data-table__num">
            2
          </td>
          <td class="data-table__hide-mobile">
            
          </td>
        </tr>
        
        <tr>
          <td>
            <a href="/countries/ROU/" class="data-table__country-cell">
              <img class="data-table__country-flag" src="/assets/images/countries/flags/rou.svg" alt="">
              <span class="data-table__country-full">Romania</span><span class="data-table__country-iso">ROU</span>
            </a>
          </td>
          <td>
            
              Cătălin Gherghe
            
          </td>
          <td>
            
              <a href="mailto:catalinliviu.gherghe@gmail.com" class="js-contact-email" data-email-user="catalinliviu.gherghe" data-email-domain="gmail.com" aria-label="Email Cătălin Gherghe" title="Email">
                <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 1024 1024" aria-hidden="true" focusable="false"><path fill="currentColor" d="M928 160H96c-17.7 0-32 14.3-32 32v640c0 17.7 14.3 32 32 32h832c17.7 0 32-14.3 32-32V192c0-17.7-14.3-32-32-32m-40 110.8V792H136V270.8l-27.6-21.5l39.3-50.5l42.8 33.3h643.1l42.8-33.3l39.3 50.5zM833.6 232L512 482L190.4 232l-42.8-33.3l-39.3 50.5l27.6 21.5l341.6 265.6a55.99 55.99 0 0 0 68.7 0L888 270.8l27.6-21.5l-39.3-50.5z"></path></svg>
              </a>
            
          </td>
          <td>
            
              <a href="http://rms.unibuc.ro" target="_blank" rel="noopener" aria-label="Visit national MO website for Romania (opens in new tab)"><span class="data-table__label-full">Visit ↗</span><span class="data-table__label-short">↗</span></a>
            
          </td>
          <td class="data-table__hide-mobile data-table__num">
            1959
          </td>
          <td class="data-table__hide-mobile data-table__num">
            67
          </td>
          <td class="data-table__hide-mobile">
            
              1959, 1960, 1969, 1978, 1999, 2018
            
          </td>
        </tr>
        
        <tr>
          <td>
            <a href="/countries/RUS/" class="data-table__country-cell">
              <img class="data-table__country-flag" src="/assets/images/countries/flags/rus.svg" alt="">
              <span class="data-table__country-full">Russian Federation</span><span class="data-table__country-iso">RUS</span>
            </a>
          </td>
          <td>
            
              Kirill Sukhov
            
          </td>
          <td>
            
              <a href="mailto:imo.russia@ya.ru" class="js-contact-email" data-email-user="imo.russia" data-email-domain="ya.ru" aria-label="Email Kirill Sukhov" title="Email">
                <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 1024 1024" aria-hidden="true" focusable="false"><path fill="currentColor" d="M928 160H96c-17.7 0-32 14.3-32 32v640c0 17.7 14.3 32 32 32h832c17.7 0 32-14.3 32-32V192c0-17.7-14.3-32-32-32m-40 110.8V792H136V270.8l-27.6-21.5l39.3-50.5l42.8 33.3h643.1l42.8-33.3l39.3 50.5zM833.6 232L512 482L190.4 232l-42.8-33.3l-39.3 50.5l27.6 21.5l341.6 265.6a55.99 55.99 0 0 0 68.7 0L888 270.8l27.6-21.5l-39.3-50.5z"></path></svg>
              </a>
            
          </td>
          <td>
            
              <a href="http://math.rosolymp.ru/" target="_blank" rel="noopener" aria-label="Visit national MO website for Russian Federation (opens in new tab)"><span class="data-table__label-full">Visit ↗</span><span class="data-table__label-short">↗</span></a>
            
          </td>
          <td class="data-table__hide-mobile data-table__num">
            1992
          </td>
          <td class="data-table__hide-mobile data-table__num">
            31
          </td>
          <td class="data-table__hide-mobile">
            
              1992, 2020, 2021
            
          </td>
        </tr>
        
        <tr>
          <td>
            <a href="/countries/RWA/" class="data-table__country-cell">
              <img class="data-table__country-flag" src="/assets/images/countries/flags/rwa.svg" alt="">
              <span class="data-table__country-full">Rwanda</span><span class="data-table__country-iso">RWA</span>
            </a>
          </td>
          <td>
            
              Obed Nsanzimfura Korusenge
            
          </td>
          <td>
            
              <a href="mailto:obed.n@rwandaolympiadfoundation.org" class="js-contact-email" data-email-user="obed.n" data-email-domain="rwandaolympiadfoundation.org" aria-label="Email Obed Nsanzimfura Korusenge" title="Email">
                <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 1024 1024" aria-hidden="true" focusable="false"><path fill="currentColor" d="M928 160H96c-17.7 0-32 14.3-32 32v640c0 17.7 14.3 32 32 32h832c17.7 0 32-14.3 32-32V192c0-17.7-14.3-32-32-32m-40 110.8V792H136V270.8l-27.6-21.5l39.3-50.5l42.8 33.3h643.1l42.8-33.3l39.3 50.5zM833.6 232L512 482L190.4 232l-42.8-33.3l-39.3 50.5l27.6 21.5l341.6 265.6a55.99 55.99 0 0 0 68.7 0L888 270.8l27.6-21.5l-39.3-50.5z"></path></svg>
              </a>
            
          </td>
          <td>
            
              <a href="https://rwandaolympiadfoundation.org/" target="_blank" rel="noopener" aria-label="Visit national MO website for Rwanda (opens in new tab)"><span class="data-table__label-full">Visit ↗</span><span class="data-table__label-short">↗</span></a>
            
          </td>
          <td class="data-table__hide-mobile data-table__num">
            2021
          </td>
          <td class="data-table__hide-mobile data-table__num">
            6
          </td>
          <td class="data-table__hide-mobile">
            
          </td>
        </tr>
        
        <tr>
          <td>
            <a href="/countries/SAF/" class="data-table__country-cell">
              <img class="data-table__country-flag" src="/assets/images/countries/flags/saf.svg" alt="">
              <span class="data-table__country-full">South Africa</span><span class="data-table__country-iso">SAF</span>
            </a>
          </td>
          <td>
            
              Liam Baker
            
          </td>
          <td>
            
              <a href="mailto:bakerbakura@gmail.com" class="js-contact-email" data-email-user="bakerbakura" data-email-domain="gmail.com" aria-label="Email Liam Baker" title="Email">
                <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 1024 1024" aria-hidden="true" focusable="false"><path fill="currentColor" d="M928 160H96c-17.7 0-32 14.3-32 32v640c0 17.7 14.3 32 32 32h832c17.7 0 32-14.3 32-32V192c0-17.7-14.3-32-32-32m-40 110.8V792H136V270.8l-27.6-21.5l39.3-50.5l42.8 33.3h643.1l42.8-33.3l39.3 50.5zM833.6 232L512 482L190.4 232l-42.8-33.3l-39.3 50.5l27.6 21.5l341.6 265.6a55.99 55.99 0 0 0 68.7 0L888 270.8l27.6-21.5l-39.3-50.5z"></path></svg>
              </a>
            
          </td>
          <td>
            
              <a href="http://www.samf.ac.za" target="_blank" rel="noopener" aria-label="Visit national MO website for South Africa (opens in new tab)"><span class="data-table__label-full">Visit ↗</span><span class="data-table__label-short">↗</span></a>
            
          </td>
          <td class="data-table__hide-mobile data-table__num">
            1992
          </td>
          <td class="data-table__hide-mobile data-table__num">
            35
          </td>
          <td class="data-table__hide-mobile">
            
              2014
            
          </td>
        </tr>
        
        <tr>
          <td>
            <a href="/countries/SAU/" class="data-table__country-cell">
              <img class="data-table__country-flag" src="/assets/images/countries/flags/sau.svg" alt="">
              <span class="data-table__country-full">Saudi Arabia</span><span class="data-table__country-iso">SAU</span>
            </a>
          </td>
          <td>
            
              Sultan Saud Albarakati
            
          </td>
          <td>
            
              <a href="mailto:sultan.albarakati@kaust.edu.sa" class="js-contact-email" data-email-user="sultan.albarakati" data-email-domain="kaust.edu.sa" aria-label="Email Sultan Saud Albarakati" title="Email">
                <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 1024 1024" aria-hidden="true" focusable="false"><path fill="currentColor" d="M928 160H96c-17.7 0-32 14.3-32 32v640c0 17.7 14.3 32 32 32h832c17.7 0 32-14.3 32-32V192c0-17.7-14.3-32-32-32m-40 110.8V792H136V270.8l-27.6-21.5l39.3-50.5l42.8 33.3h643.1l42.8-33.3l39.3 50.5zM833.6 232L512 482L190.4 232l-42.8-33.3l-39.3 50.5l27.6 21.5l341.6 265.6a55.99 55.99 0 0 0 68.7 0L888 270.8l27.6-21.5l-39.3-50.5z"></path></svg>
              </a>
            
          </td>
          <td>
            
              <a href="https://www.mawhiba.org" target="_blank" rel="noopener" aria-label="Visit national MO website for Saudi Arabia (opens in new tab)"><span class="data-table__label-full">Visit ↗</span><span class="data-table__label-short">↗</span></a>
            
          </td>
          <td class="data-table__hide-mobile data-table__num">
            2004
          </td>
          <td class="data-table__hide-mobile data-table__num">
            22
          </td>
          <td class="data-table__hide-mobile">
            
              2028
            
          </td>
        </tr>
        
        <tr class="data-table__row--inactive">
          <td>
            <a href="/countries/SCG/" class="data-table__country-cell">
              <img class="data-table__country-flag" src="/assets/images/countries/flags/scg.svg" alt="">
              <span class="data-table__country-full">Serbia and Montenegro</span><span class="data-table__country-iso">SCG</span>
            </a>
          </td>
          <td>
            
          </td>
          <td>
            
          </td>
          <td>
            
          </td>
          <td class="data-table__hide-mobile data-table__num">
            2003
          </td>
          <td class="data-table__hide-mobile data-table__num">
            3
          </td>
          <td class="data-table__hide-mobile">
            
          </td>
        </tr>
        
        <tr>
          <td>
            <a href="/countries/SEN/" class="data-table__country-cell">
              <img class="data-table__country-flag" src="/assets/images/countries/flags/sen.svg" alt="">
              <span class="data-table__country-full">Senegal</span><span class="data-table__country-iso">SEN</span>
            </a>
          </td>
          <td>
            
              Samba Dabo
            
          </td>
          <td>
            
              <a href="mailto:sdabo345@gmail.com" class="js-contact-email" data-email-user="sdabo345" data-email-domain="gmail.com" aria-label="Email Samba Dabo" title="Email">
                <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 1024 1024" aria-hidden="true" focusable="false"><path fill="currentColor" d="M928 160H96c-17.7 0-32 14.3-32 32v640c0 17.7 14.3 32 32 32h832c17.7 0 32-14.3 32-32V192c0-17.7-14.3-32-32-32m-40 110.8V792H136V270.8l-27.6-21.5l39.3-50.5l42.8 33.3h643.1l42.8-33.3l39.3 50.5zM833.6 232L512 482L190.4 232l-42.8-33.3l-39.3 50.5l27.6 21.5l341.6 265.6a55.99 55.99 0 0 0 68.7 0L888 270.8l27.6-21.5l-39.3-50.5z"></path></svg>
              </a>
            
          </td>
          <td>
            
          </td>
          <td class="data-table__hide-mobile data-table__num">
            2026
          </td>
          <td class="data-table__hide-mobile data-table__num">
            1
          </td>
          <td class="data-table__hide-mobile">
            
          </td>
        </tr>
        
        <tr>
          <td>
            <a href="/countries/SGP/" class="data-table__country-cell">
              <img class="data-table__country-flag" src="/assets/images/countries/flags/sgp.svg" alt="">
              <span class="data-table__country-full">Singapore</span><span class="data-table__country-iso">SGP</span>
            </a>
          </td>
          <td>
            
              Yong Sheng Soh
            
          </td>
          <td>
            
              <a href="mailto:matsys@nus.edu.sg" class="js-contact-email" data-email-user="matsys" data-email-domain="nus.edu.sg" aria-label="Email Yong Sheng Soh" title="Email">
                <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 1024 1024" aria-hidden="true" focusable="false"><path fill="currentColor" d="M928 160H96c-17.7 0-32 14.3-32 32v640c0 17.7 14.3 32 32 32h832c17.7 0 32-14.3 32-32V192c0-17.7-14.3-32-32-32m-40 110.8V792H136V270.8l-27.6-21.5l39.3-50.5l42.8 33.3h643.1l42.8-33.3l39.3 50.5zM833.6 232L512 482L190.4 232l-42.8-33.3l-39.3 50.5l27.6 21.5l341.6 265.6a55.99 55.99 0 0 0 68.7 0L888 270.8l27.6-21.5l-39.3-50.5z"></path></svg>
              </a>
            
          </td>
          <td>
            
              <a href="http://sms.math.nus.edu.sg/" target="_blank" rel="noopener" aria-label="Visit national MO website for Singapore (opens in new tab)"><span class="data-table__label-full">Visit ↗</span><span class="data-table__label-short">↗</span></a>
            
          </td>
          <td class="data-table__hide-mobile data-table__num">
            1988
          </td>
          <td class="data-table__hide-mobile data-table__num">
            39
          </td>
          <td class="data-table__hide-mobile">
            
          </td>
        </tr>
        
        <tr>
          <td>
            <a href="/countries/SLV/" class="data-table__country-cell">
              <img class="data-table__country-flag" src="/assets/images/countries/flags/slv.svg" alt="">
              <span class="data-table__country-full">El Salvador</span><span class="data-table__country-iso">SLV</span>
            </a>
          </td>
          <td>
            
              Riquelmi Salvador Cardona Fuentes
            
          </td>
          <td>
            
              <a href="mailto:riquelmi.cardona@jovenestalento.edu.sv" class="js-contact-email" data-email-user="riquelmi.cardona" data-email-domain="jovenestalento.edu.sv" aria-label="Email Riquelmi Salvador Cardona Fuentes" title="Email">
                <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 1024 1024" aria-hidden="true" focusable="false"><path fill="currentColor" d="M928 160H96c-17.7 0-32 14.3-32 32v640c0 17.7 14.3 32 32 32h832c17.7 0 32-14.3 32-32V192c0-17.7-14.3-32-32-32m-40 110.8V792H136V270.8l-27.6-21.5l39.3-50.5l42.8 33.3h643.1l42.8-33.3l39.3 50.5zM833.6 232L512 482L190.4 232l-42.8-33.3l-39.3 50.5l27.6 21.5l341.6 265.6a55.99 55.99 0 0 0 68.7 0L888 270.8l27.6-21.5l-39.3-50.5z"></path></svg>
              </a>
            
          </td>
          <td>
            
              <a href="https://www.jovenestalento.edu.sv/" target="_blank" rel="noopener" aria-label="Visit national MO website for El Salvador (opens in new tab)"><span class="data-table__label-full">Visit ↗</span><span class="data-table__label-short">↗</span></a>
            
          </td>
          <td class="data-table__hide-mobile data-table__num">
            2005
          </td>
          <td class="data-table__hide-mobile data-table__num">
            21
          </td>
          <td class="data-table__hide-mobile">
            
          </td>
        </tr>
        
        <tr>
          <td>
            <a href="/countries/SRB/" class="data-table__country-cell">
              <img class="data-table__country-flag" src="/assets/images/countries/flags/srb.svg" alt="">
              <span class="data-table__country-full">Serbia</span><span class="data-table__country-iso">SRB</span>
            </a>
          </td>
          <td>
            
              Miljan Knežević
            
          </td>
          <td>
            
              <a href="mailto:kmiljan@matf.bg.ac.rs" class="js-contact-email" data-email-user="kmiljan" data-email-domain="matf.bg.ac.rs" aria-label="Email Miljan Knežević" title="Email">
                <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 1024 1024" aria-hidden="true" focusable="false"><path fill="currentColor" d="M928 160H96c-17.7 0-32 14.3-32 32v640c0 17.7 14.3 32 32 32h832c17.7 0 32-14.3 32-32V192c0-17.7-14.3-32-32-32m-40 110.8V792H136V270.8l-27.6-21.5l39.3-50.5l42.8 33.3h643.1l42.8-33.3l39.3 50.5zM833.6 232L512 482L190.4 232l-42.8-33.3l-39.3 50.5l27.6 21.5l341.6 265.6a55.99 55.99 0 0 0 68.7 0L888 270.8l27.6-21.5l-39.3-50.5z"></path></svg>
              </a>
            
          </td>
          <td>
            
              <a href="https://dms.rs/" target="_blank" rel="noopener" aria-label="Visit national MO website for Serbia (opens in new tab)"><span class="data-table__label-full">Visit ↗</span><span class="data-table__label-short">↗</span></a>
            
          </td>
          <td class="data-table__hide-mobile data-table__num">
            2006
          </td>
          <td class="data-table__hide-mobile data-table__num">
            21
          </td>
          <td class="data-table__hide-mobile">
            
          </td>
        </tr>
        
        <tr>
          <td>
            <a href="/countries/SUI/" class="data-table__country-cell">
              <img class="data-table__country-flag" src="/assets/images/countries/flags/sui.svg" alt="">
              <span class="data-table__country-full">Switzerland</span><span class="data-table__country-iso">SUI</span>
            </a>
          </td>
          <td>
            
              Swiss Mathematical Olympiad Board
            
          </td>
          <td>
            
              <a href="mailto:info@mathematical.olympiad.ch" class="js-contact-email" data-email-user="info" data-email-domain="mathematical.olympiad.ch" aria-label="Email Swiss Mathematical Olympiad Board" title="Email">
                <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 1024 1024" aria-hidden="true" focusable="false"><path fill="currentColor" d="M928 160H96c-17.7 0-32 14.3-32 32v640c0 17.7 14.3 32 32 32h832c17.7 0 32-14.3 32-32V192c0-17.7-14.3-32-32-32m-40 110.8V792H136V270.8l-27.6-21.5l39.3-50.5l42.8 33.3h643.1l42.8-33.3l39.3 50.5zM833.6 232L512 482L190.4 232l-42.8-33.3l-39.3 50.5l27.6 21.5l341.6 265.6a55.99 55.99 0 0 0 68.7 0L888 270.8l27.6-21.5l-39.3-50.5z"></path></svg>
              </a>
            
          </td>
          <td>
            
              <a href="https://mathematical.olympiad.ch/en/" target="_blank" rel="noopener" aria-label="Visit national MO website for Switzerland (opens in new tab)"><span class="data-table__label-full">Visit ↗</span><span class="data-table__label-short">↗</span></a>
            
          </td>
          <td class="data-table__hide-mobile data-table__num">
            1991
          </td>
          <td class="data-table__hide-mobile data-table__num">
            36
          </td>
          <td class="data-table__hide-mobile">
            
              2030
            
          </td>
        </tr>
        
        <tr>
          <td>
            <a href="/countries/SVK/" class="data-table__country-cell">
              <img class="data-table__country-flag" src="/assets/images/countries/flags/svk.svg" alt="">
              <span class="data-table__country-full">Slovakia</span><span class="data-table__country-iso">SVK</span>
            </a>
          </td>
          <td>
            
              Stanislav Krajči
            
          </td>
          <td>
            
              <a href="mailto:stanislav.krajci@upjs.sk" class="js-contact-email" data-email-user="stanislav.krajci" data-email-domain="upjs.sk" aria-label="Email Stanislav Krajči" title="Email">
                <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 1024 1024" aria-hidden="true" focusable="false"><path fill="currentColor" d="M928 160H96c-17.7 0-32 14.3-32 32v640c0 17.7 14.3 32 32 32h832c17.7 0 32-14.3 32-32V192c0-17.7-14.3-32-32-32m-40 110.8V792H136V270.8l-27.6-21.5l39.3-50.5l42.8 33.3h643.1l42.8-33.3l39.3 50.5zM833.6 232L512 482L190.4 232l-42.8-33.3l-39.3 50.5l27.6 21.5l341.6 265.6a55.99 55.99 0 0 0 68.7 0L888 270.8l27.6-21.5l-39.3-50.5z"></path></svg>
              </a>
            
          </td>
          <td>
            
              <a href="http://skmo.sk" target="_blank" rel="noopener" aria-label="Visit national MO website for Slovakia (opens in new tab)"><span class="data-table__label-full">Visit ↗</span><span class="data-table__label-short">↗</span></a>
            
          </td>
          <td class="data-table__hide-mobile data-table__num">
            1993
          </td>
          <td class="data-table__hide-mobile data-table__num">
            34
          </td>
          <td class="data-table__hide-mobile">
            
          </td>
        </tr>
        
        <tr>
          <td>
            <a href="/countries/SVN/" class="data-table__country-cell">
              <img class="data-table__country-flag" src="/assets/images/countries/flags/svn.svg" alt="">
              <span class="data-table__country-full">Slovenia</span><span class="data-table__country-iso">SVN</span>
            </a>
          </td>
          <td>
            
              Gregor Dolinar
            
          </td>
          <td>
            
              <a href="mailto:gregor.dolinar@fe.uni-lj.si" class="js-contact-email" data-email-user="gregor.dolinar" data-email-domain="fe.uni-lj.si" aria-label="Email Gregor Dolinar" title="Email">
                <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 1024 1024" aria-hidden="true" focusable="false"><path fill="currentColor" d="M928 160H96c-17.7 0-32 14.3-32 32v640c0 17.7 14.3 32 32 32h832c17.7 0 32-14.3 32-32V192c0-17.7-14.3-32-32-32m-40 110.8V792H136V270.8l-27.6-21.5l39.3-50.5l42.8 33.3h643.1l42.8-33.3l39.3 50.5zM833.6 232L512 482L190.4 232l-42.8-33.3l-39.3 50.5l27.6 21.5l341.6 265.6a55.99 55.99 0 0 0 68.7 0L888 270.8l27.6-21.5l-39.3-50.5z"></path></svg>
              </a>
            
          </td>
          <td>
            
              <a href="http://www.dmfa.si/" target="_blank" rel="noopener" aria-label="Visit national MO website for Slovenia (opens in new tab)"><span class="data-table__label-full">Visit ↗</span><span class="data-table__label-short">↗</span></a>
            
          </td>
          <td class="data-table__hide-mobile data-table__num">
            1993
          </td>
          <td class="data-table__hide-mobile data-table__num">
            34
          </td>
          <td class="data-table__hide-mobile">
            
              2006
            
          </td>
        </tr>
        
        <tr>
          <td>
            <a href="/countries/SWE/" class="data-table__country-cell">
              <img class="data-table__country-flag" src="/assets/images/countries/flags/swe.svg" alt="">
              <span class="data-table__country-full">Sweden</span><span class="data-table__country-iso">SWE</span>
            </a>
          </td>
          <td>
            
              Jana Madjarova
            
          </td>
          <td>
            
              <a href="mailto:jana@chalmers.se" class="js-contact-email" data-email-user="jana" data-email-domain="chalmers.se" aria-label="Email Jana Madjarova" title="Email">
                <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 1024 1024" aria-hidden="true" focusable="false"><path fill="currentColor" d="M928 160H96c-17.7 0-32 14.3-32 32v640c0 17.7 14.3 32 32 32h832c17.7 0 32-14.3 32-32V192c0-17.7-14.3-32-32-32m-40 110.8V792H136V270.8l-27.6-21.5l39.3-50.5l42.8 33.3h643.1l42.8-33.3l39.3 50.5zM833.6 232L512 482L190.4 232l-42.8-33.3l-39.3 50.5l27.6 21.5l341.6 265.6a55.99 55.99 0 0 0 68.7 0L888 270.8l27.6-21.5l-39.3-50.5z"></path></svg>
              </a>
            
          </td>
          <td>
            
              <a href="http://www.mattetavling.se" target="_blank" rel="noopener" aria-label="Visit national MO website for Sweden (opens in new tab)"><span class="data-table__label-full">Visit ↗</span><span class="data-table__label-short">↗</span></a>
            
          </td>
          <td class="data-table__hide-mobile data-table__num">
            1967
          </td>
          <td class="data-table__hide-mobile data-table__num">
            59
          </td>
          <td class="data-table__hide-mobile">
            
              1991
            
          </td>
        </tr>
        
        <tr>
          <td>
            <a href="/countries/SYR/" class="data-table__country-cell">
              <img class="data-table__country-flag" src="/assets/images/countries/flags/syr.svg" alt="">
              <span class="data-table__country-full">Syria</span><span class="data-table__country-iso">SYR</span>
            </a>
          </td>
          <td>
            
              Chadi Al-Azmeh
            
          </td>
          <td>
            
              <a href="mailto:dca.olympiad@gmail.com" class="js-contact-email" data-email-user="dca.olympiad" data-email-domain="gmail.com" aria-label="Email Chadi Al-Azmeh" title="Email">
                <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 1024 1024" aria-hidden="true" focusable="false"><path fill="currentColor" d="M928 160H96c-17.7 0-32 14.3-32 32v640c0 17.7 14.3 32 32 32h832c17.7 0 32-14.3 32-32V192c0-17.7-14.3-32-32-32m-40 110.8V792H136V270.8l-27.6-21.5l39.3-50.5l42.8 33.3h643.1l42.8-33.3l39.3 50.5zM833.6 232L512 482L190.4 232l-42.8-33.3l-39.3 50.5l27.6 21.5l341.6 265.6a55.99 55.99 0 0 0 68.7 0L888 270.8l27.6-21.5l-39.3-50.5z"></path></svg>
              </a>
            
          </td>
          <td>
            
              <a href="https://dca-net.org/" target="_blank" rel="noopener" aria-label="Visit national MO website for Syria (opens in new tab)"><span class="data-table__label-full">Visit ↗</span><span class="data-table__label-short">↗</span></a>
            
          </td>
          <td class="data-table__hide-mobile data-table__num">
            2009
          </td>
          <td class="data-table__hide-mobile data-table__num">
            18
          </td>
          <td class="data-table__hide-mobile">
            
          </td>
        </tr>
        
        <tr>
          <td>
            <a href="/countries/THA/" class="data-table__country-cell">
              <img class="data-table__country-flag" src="/assets/images/countries/flags/tha.svg" alt="">
              <span class="data-table__country-full">Thailand</span><span class="data-table__country-iso">THA</span>
            </a>
          </td>
          <td>
            
              Thiradet Jiarasuksakun
            
          </td>
          <td>
            
              <a href="mailto:imo_thai@ipst.ac.th" class="js-contact-email" data-email-user="imo_thai" data-email-domain="ipst.ac.th" aria-label="Email Thiradet Jiarasuksakun" title="Email">
                <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 1024 1024" aria-hidden="true" focusable="false"><path fill="currentColor" d="M928 160H96c-17.7 0-32 14.3-32 32v640c0 17.7 14.3 32 32 32h832c17.7 0 32-14.3 32-32V192c0-17.7-14.3-32-32-32m-40 110.8V792H136V270.8l-27.6-21.5l39.3-50.5l42.8 33.3h643.1l42.8-33.3l39.3 50.5zM833.6 232L512 482L190.4 232l-42.8-33.3l-39.3 50.5l27.6 21.5l341.6 265.6a55.99 55.99 0 0 0 68.7 0L888 270.8l27.6-21.5l-39.3-50.5z"></path></svg>
              </a>
            
          </td>
          <td>
            
          </td>
          <td class="data-table__hide-mobile data-table__num">
            1989
          </td>
          <td class="data-table__hide-mobile data-table__num">
            38
          </td>
          <td class="data-table__hide-mobile">
            
              2015
            
          </td>
        </tr>
        
        <tr>
          <td>
            <a href="/countries/TJK/" class="data-table__country-cell">
              <img class="data-table__country-flag" src="/assets/images/countries/flags/tjk.svg" alt="">
              <span class="data-table__country-full">Tajikistan</span><span class="data-table__country-iso">TJK</span>
            </a>
          </td>
          <td>
            
              Umed Karimov
            
          </td>
          <td>
            
              <a href="mailto:u.h.karimov@gmail.com" class="js-contact-email" data-email-user="u.h.karimov" data-email-domain="gmail.com" aria-label="Email Umed Karimov" title="Email">
                <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 1024 1024" aria-hidden="true" focusable="false"><path fill="currentColor" d="M928 160H96c-17.7 0-32 14.3-32 32v640c0 17.7 14.3 32 32 32h832c17.7 0 32-14.3 32-32V192c0-17.7-14.3-32-32-32m-40 110.8V792H136V270.8l-27.6-21.5l39.3-50.5l42.8 33.3h643.1l42.8-33.3l39.3 50.5zM833.6 232L512 482L190.4 232l-42.8-33.3l-39.3 50.5l27.6 21.5l341.6 265.6a55.99 55.99 0 0 0 68.7 0L888 270.8l27.6-21.5l-39.3-50.5z"></path></svg>
              </a>
            
          </td>
          <td>
            
          </td>
          <td class="data-table__hide-mobile data-table__num">
            2005
          </td>
          <td class="data-table__hide-mobile data-table__num">
            22
          </td>
          <td class="data-table__hide-mobile">
            
          </td>
        </tr>
        
        <tr>
          <td>
            <a href="/countries/TKM/" class="data-table__country-cell">
              <img class="data-table__country-flag" src="/assets/images/countries/flags/tkm.svg" alt="">
              <span class="data-table__country-full">Turkmenistan</span><span class="data-table__country-iso">TKM</span>
            </a>
          </td>
          <td>
            
              Pirmyrat Gurbanov
            
          </td>
          <td>
            
              <a href="mailto:pirgurban@gmail.com" class="js-contact-email" data-email-user="pirgurban" data-email-domain="gmail.com" aria-label="Email Pirmyrat Gurbanov" title="Email">
                <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 1024 1024" aria-hidden="true" focusable="false"><path fill="currentColor" d="M928 160H96c-17.7 0-32 14.3-32 32v640c0 17.7 14.3 32 32 32h832c17.7 0 32-14.3 32-32V192c0-17.7-14.3-32-32-32m-40 110.8V792H136V270.8l-27.6-21.5l39.3-50.5l42.8 33.3h643.1l42.8-33.3l39.3 50.5zM833.6 232L512 482L190.4 232l-42.8-33.3l-39.3 50.5l27.6 21.5l341.6 265.6a55.99 55.99 0 0 0 68.7 0L888 270.8l27.6-21.5l-39.3-50.5z"></path></svg>
              </a>
            
          </td>
          <td>
            
              <a href="https://education.gov.tm/" target="_blank" rel="noopener" aria-label="Visit national MO website for Turkmenistan (opens in new tab)"><span class="data-table__label-full">Visit ↗</span><span class="data-table__label-short">↗</span></a>
            
          </td>
          <td class="data-table__hide-mobile data-table__num">
            1993
          </td>
          <td class="data-table__hide-mobile data-table__num">
            27
          </td>
          <td class="data-table__hide-mobile">
            
          </td>
        </tr>
        
        <tr>
          <td>
            <a href="/countries/TTO/" class="data-table__country-cell">
              <img class="data-table__country-flag" src="/assets/images/countries/flags/tto.svg" alt="">
              <span class="data-table__country-full">Trinidad and Tobago</span><span class="data-table__country-iso">TTO</span>
            </a>
          </td>
          <td>
            
              Indra Haraksingh
            
          </td>
          <td>
            
              <a href="mailto:haraksinghindra@gmail.com" class="js-contact-email" data-email-user="haraksinghindra" data-email-domain="gmail.com" aria-label="Email Indra Haraksingh" title="Email">
                <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 1024 1024" aria-hidden="true" focusable="false"><path fill="currentColor" d="M928 160H96c-17.7 0-32 14.3-32 32v640c0 17.7 14.3 32 32 32h832c17.7 0 32-14.3 32-32V192c0-17.7-14.3-32-32-32m-40 110.8V792H136V270.8l-27.6-21.5l39.3-50.5l42.8 33.3h643.1l42.8-33.3l39.3 50.5zM833.6 232L512 482L190.4 232l-42.8-33.3l-39.3 50.5l27.6 21.5l341.6 265.6a55.99 55.99 0 0 0 68.7 0L888 270.8l27.6-21.5l-39.3-50.5z"></path></svg>
              </a>
            
          </td>
          <td>
            
          </td>
          <td class="data-table__hide-mobile data-table__num">
            1991
          </td>
          <td class="data-table__hide-mobile data-table__num">
            32
          </td>
          <td class="data-table__hide-mobile">
            
          </td>
        </tr>
        
        <tr>
          <td>
            <a href="/countries/TUN/" class="data-table__country-cell">
              <img class="data-table__country-flag" src="/assets/images/countries/flags/tun.svg" alt="">
              <span class="data-table__country-full">Tunisia</span><span class="data-table__country-iso">TUN</span>
            </a>
          </td>
          <td>
            
              Taoufik Charrada
            
          </td>
          <td>
            
              <a href="mailto:tawfik.charrada@gmail.com" class="js-contact-email" data-email-user="tawfik.charrada" data-email-domain="gmail.com" aria-label="Email Taoufik Charrada" title="Email">
                <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 1024 1024" aria-hidden="true" focusable="false"><path fill="currentColor" d="M928 160H96c-17.7 0-32 14.3-32 32v640c0 17.7 14.3 32 32 32h832c17.7 0 32-14.3 32-32V192c0-17.7-14.3-32-32-32m-40 110.8V792H136V270.8l-27.6-21.5l39.3-50.5l42.8 33.3h643.1l42.8-33.3l39.3 50.5zM833.6 232L512 482L190.4 232l-42.8-33.3l-39.3 50.5l27.6 21.5l341.6 265.6a55.99 55.99 0 0 0 68.7 0L888 270.8l27.6-21.5l-39.3-50.5z"></path></svg>
              </a>
            
          </td>
          <td>
            
          </td>
          <td class="data-table__hide-mobile data-table__num">
            1981
          </td>
          <td class="data-table__hide-mobile data-table__num">
            35
          </td>
          <td class="data-table__hide-mobile">
            
          </td>
        </tr>
        
        <tr>
          <td>
            <a href="/countries/TUR/" class="data-table__country-cell">
              <img class="data-table__country-flag" src="/assets/images/countries/flags/tur.svg" alt="">
              <span class="data-table__country-full">Türkiye</span><span class="data-table__country-iso">TUR</span>
            </a>
          </td>
          <td>
            
              Azer Kerimov
            
          </td>
          <td>
            
              <a href="mailto:kerimov@fen.bilkent.edu.tr" class="js-contact-email" data-email-user="kerimov" data-email-domain="fen.bilkent.edu.tr" aria-label="Email Azer Kerimov" title="Email">
                <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 1024 1024" aria-hidden="true" focusable="false"><path fill="currentColor" d="M928 160H96c-17.7 0-32 14.3-32 32v640c0 17.7 14.3 32 32 32h832c17.7 0 32-14.3 32-32V192c0-17.7-14.3-32-32-32m-40 110.8V792H136V270.8l-27.6-21.5l39.3-50.5l42.8 33.3h643.1l42.8-33.3l39.3 50.5zM833.6 232L512 482L190.4 232l-42.8-33.3l-39.3 50.5l27.6 21.5l341.6 265.6a55.99 55.99 0 0 0 68.7 0L888 270.8l27.6-21.5l-39.3-50.5z"></path></svg>
              </a>
            
          </td>
          <td>
            
              <a href="https://bilimolimpiyatlari.tubitak.gov.tr/tr" target="_blank" rel="noopener" aria-label="Visit national MO website for Türkiye (opens in new tab)"><span class="data-table__label-full">Visit ↗</span><span class="data-table__label-short">↗</span></a>
            
          </td>
          <td class="data-table__hide-mobile data-table__num">
            1978
          </td>
          <td class="data-table__hide-mobile data-table__num">
            43
          </td>
          <td class="data-table__hide-mobile">
            
              1993
            
          </td>
        </tr>
        
        <tr>
          <td>
            <a href="/countries/TWN/" class="data-table__country-cell">
              <img class="data-table__country-flag" src="/assets/images/countries/flags/twn.svg" alt="">
              <span class="data-table__country-full">Taiwan</span><span class="data-table__country-iso">TWN</span>
            </a>
          </td>
          <td>
            
              Yen-chi Roger Lin
            
          </td>
          <td>
            
              <a href="mailto:yclinpa@gmail.com" class="js-contact-email" data-email-user="yclinpa" data-email-domain="gmail.com" aria-label="Email Yen-chi Roger Lin" title="Email">
                <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 1024 1024" aria-hidden="true" focusable="false"><path fill="currentColor" d="M928 160H96c-17.7 0-32 14.3-32 32v640c0 17.7 14.3 32 32 32h832c17.7 0 32-14.3 32-32V192c0-17.7-14.3-32-32-32m-40 110.8V792H136V270.8l-27.6-21.5l39.3-50.5l42.8 33.3h643.1l42.8-33.3l39.3 50.5zM833.6 232L512 482L190.4 232l-42.8-33.3l-39.3 50.5l27.6 21.5l341.6 265.6a55.99 55.99 0 0 0 68.7 0L888 270.8l27.6-21.5l-39.3-50.5z"></path></svg>
              </a>
            
          </td>
          <td>
            
              <a href="https://tpmso.org/tmo/" target="_blank" rel="noopener" aria-label="Visit national MO website for Taiwan (opens in new tab)"><span class="data-table__label-full">Visit ↗</span><span class="data-table__label-short">↗</span></a>
            
          </td>
          <td class="data-table__hide-mobile data-table__num">
            1992
          </td>
          <td class="data-table__hide-mobile data-table__num">
            35
          </td>
          <td class="data-table__hide-mobile">
            
              1998
            
          </td>
        </tr>
        
        <tr>
          <td>
            <a href="/countries/TZA/" class="data-table__country-cell">
              <img class="data-table__country-flag" src="/assets/images/countries/flags/tza.svg" alt="">
              <span class="data-table__country-full">Tanzania</span><span class="data-table__country-iso">TZA</span>
            </a>
          </td>
          <td>
            
              Said Sima
            
          </td>
          <td>
            
              <a href="mailto:said.sima@gmail.com" class="js-contact-email" data-email-user="said.sima" data-email-domain="gmail.com" aria-label="Email Said Sima" title="Email">
                <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 1024 1024" aria-hidden="true" focusable="false"><path fill="currentColor" d="M928 160H96c-17.7 0-32 14.3-32 32v640c0 17.7 14.3 32 32 32h832c17.7 0 32-14.3 32-32V192c0-17.7-14.3-32-32-32m-40 110.8V792H136V270.8l-27.6-21.5l39.3-50.5l42.8 33.3h643.1l42.8-33.3l39.3 50.5zM833.6 232L512 482L190.4 232l-42.8-33.3l-39.3 50.5l27.6 21.5l341.6 265.6a55.99 55.99 0 0 0 68.7 0L888 270.8l27.6-21.5l-39.3-50.5z"></path></svg>
              </a>
            
          </td>
          <td>
            
          </td>
          <td class="data-table__hide-mobile data-table__num">
            2014
          </td>
          <td class="data-table__hide-mobile data-table__num">
            9
          </td>
          <td class="data-table__hide-mobile">
            
          </td>
        </tr>
        
        <tr>
          <td>
            <a href="/countries/UAE/" class="data-table__country-cell">
              <img class="data-table__country-flag" src="/assets/images/countries/flags/uae.svg" alt="">
              <span class="data-table__country-full">United Arab Emirates</span><span class="data-table__country-iso">UAE</span>
            </a>
          </td>
          <td>
            
              International Olympiad Foundation
            
          </td>
          <td>
            
              <a href="mailto:info@olympiads.org" class="js-contact-email" data-email-user="info" data-email-domain="olympiads.org" aria-label="Email International Olympiad Foundation" title="Email">
                <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 1024 1024" aria-hidden="true" focusable="false"><path fill="currentColor" d="M928 160H96c-17.7 0-32 14.3-32 32v640c0 17.7 14.3 32 32 32h832c17.7 0 32-14.3 32-32V192c0-17.7-14.3-32-32-32m-40 110.8V792H136V270.8l-27.6-21.5l39.3-50.5l42.8 33.3h643.1l42.8-33.3l39.3 50.5zM833.6 232L512 482L190.4 232l-42.8-33.3l-39.3 50.5l27.6 21.5l341.6 265.6a55.99 55.99 0 0 0 68.7 0L888 270.8l27.6-21.5l-39.3-50.5z"></path></svg>
              </a>
            
          </td>
          <td>
            
              <a href="https://olympiads.org/" target="_blank" rel="noopener" aria-label="Visit national MO website for United Arab Emirates (opens in new tab)"><span class="data-table__label-full">Visit ↗</span><span class="data-table__label-short">↗</span></a>
            
          </td>
          <td class="data-table__hide-mobile data-table__num">
            2008
          </td>
          <td class="data-table__hide-mobile data-table__num">
            9
          </td>
          <td class="data-table__hide-mobile">
            
          </td>
        </tr>
        
        <tr>
          <td>
            <a href="/countries/UGA/" class="data-table__country-cell">
              <img class="data-table__country-flag" src="/assets/images/countries/flags/uga.svg" alt="">
              <span class="data-table__country-full">Uganda</span><span class="data-table__country-iso">UGA</span>
            </a>
          </td>
          <td>
            
              Joseph Ssebuliba
            
          </td>
          <td>
            
              <a href="mailto:ssebulibaa@gmail.com" class="js-contact-email" data-email-user="ssebulibaa" data-email-domain="gmail.com" aria-label="Email Joseph Ssebuliba" title="Email">
                <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 1024 1024" aria-hidden="true" focusable="false"><path fill="currentColor" d="M928 160H96c-17.7 0-32 14.3-32 32v640c0 17.7 14.3 32 32 32h832c17.7 0 32-14.3 32-32V192c0-17.7-14.3-32-32-32m-40 110.8V792H136V270.8l-27.6-21.5l39.3-50.5l42.8 33.3h643.1l42.8-33.3l39.3 50.5zM833.6 232L512 482L190.4 232l-42.8-33.3l-39.3 50.5l27.6 21.5l341.6 265.6a55.99 55.99 0 0 0 68.7 0L888 270.8l27.6-21.5l-39.3-50.5z"></path></svg>
              </a>
            
          </td>
          <td>
            
              <a href="https://ums.ug/" target="_blank" rel="noopener" aria-label="Visit national MO website for Uganda (opens in new tab)"><span class="data-table__label-full">Visit ↗</span><span class="data-table__label-short">↗</span></a>
            
          </td>
          <td class="data-table__hide-mobile data-table__num">
            2012
          </td>
          <td class="data-table__hide-mobile data-table__num">
            15
          </td>
          <td class="data-table__hide-mobile">
            
          </td>
        </tr>
        
        <tr>
          <td>
            <a href="/countries/UKR/" class="data-table__country-cell">
              <img class="data-table__country-flag" src="/assets/images/countries/flags/ukr.svg" alt="">
              <span class="data-table__country-full">Ukraine</span><span class="data-table__country-iso">UKR</span>
            </a>
          </td>
          <td>
            
              Bogdan Rublov
            
          </td>
          <td>
            
              <a href="mailto:rublyovbv@gmail.com" class="js-contact-email" data-email-user="rublyovbv" data-email-domain="gmail.com" aria-label="Email Bogdan Rublov" title="Email">
                <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 1024 1024" aria-hidden="true" focusable="false"><path fill="currentColor" d="M928 160H96c-17.7 0-32 14.3-32 32v640c0 17.7 14.3 32 32 32h832c17.7 0 32-14.3 32-32V192c0-17.7-14.3-32-32-32m-40 110.8V792H136V270.8l-27.6-21.5l39.3-50.5l42.8 33.3h643.1l42.8-33.3l39.3 50.5zM833.6 232L512 482L190.4 232l-42.8-33.3l-39.3 50.5l27.6 21.5l341.6 265.6a55.99 55.99 0 0 0 68.7 0L888 270.8l27.6-21.5l-39.3-50.5z"></path></svg>
              </a>
            
          </td>
          <td>
            
              <a href="http://matholymp.com.ua/" target="_blank" rel="noopener" aria-label="Visit national MO website for Ukraine (opens in new tab)"><span class="data-table__label-full">Visit ↗</span><span class="data-table__label-short">↗</span></a>
            
          </td>
          <td class="data-table__hide-mobile data-table__num">
            1993
          </td>
          <td class="data-table__hide-mobile data-table__num">
            34
          </td>
          <td class="data-table__hide-mobile">
            
          </td>
        </tr>
        
        <tr>
          <td>
            <a href="/countries/UNK/" class="data-table__country-cell">
              <img class="data-table__country-flag" src="/assets/images/countries/flags/unk.svg" alt="">
              <span class="data-table__country-full">United Kingdom</span><span class="data-table__country-iso">UNK</span>
            </a>
          </td>
          <td>
            
              Geoff Smith
            
          </td>
          <td>
            
              <a href="mailto:geoffsmith1729@gmail.com" class="js-contact-email" data-email-user="geoffsmith1729" data-email-domain="gmail.com" aria-label="Email Geoff Smith" title="Email">
                <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 1024 1024" aria-hidden="true" focusable="false"><path fill="currentColor" d="M928 160H96c-17.7 0-32 14.3-32 32v640c0 17.7 14.3 32 32 32h832c17.7 0 32-14.3 32-32V192c0-17.7-14.3-32-32-32m-40 110.8V792H136V270.8l-27.6-21.5l39.3-50.5l42.8 33.3h643.1l42.8-33.3l39.3 50.5zM833.6 232L512 482L190.4 232l-42.8-33.3l-39.3 50.5l27.6 21.5l341.6 265.6a55.99 55.99 0 0 0 68.7 0L888 270.8l27.6-21.5l-39.3-50.5z"></path></svg>
              </a>
            
          </td>
          <td>
            
              <a href="https://bmos.ukmt.org.uk/" target="_blank" rel="noopener" aria-label="Visit national MO website for United Kingdom (opens in new tab)"><span class="data-table__label-full">Visit ↗</span><span class="data-table__label-short">↗</span></a>
            
          </td>
          <td class="data-table__hide-mobile data-table__num">
            1967
          </td>
          <td class="data-table__hide-mobile data-table__num">
            59
          </td>
          <td class="data-table__hide-mobile">
            
              1979, 2002, 2019, 2024
            
          </td>
        </tr>
        
        <tr>
          <td>
            <a href="/countries/URY/" class="data-table__country-cell">
              <img class="data-table__country-flag" src="/assets/images/countries/flags/ury.svg" alt="">
              <span class="data-table__country-full">Uruguay</span><span class="data-table__country-iso">URY</span>
            </a>
          </td>
          <td>
            
              Maximiliano Stock
            
          </td>
          <td>
            
              <a href="mailto:lacompartida@gmail.com" class="js-contact-email" data-email-user="lacompartida" data-email-domain="gmail.com" aria-label="Email Maximiliano Stock" title="Email">
                <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 1024 1024" aria-hidden="true" focusable="false"><path fill="currentColor" d="M928 160H96c-17.7 0-32 14.3-32 32v640c0 17.7 14.3 32 32 32h832c17.7 0 32-14.3 32-32V192c0-17.7-14.3-32-32-32m-40 110.8V792H136V270.8l-27.6-21.5l39.3-50.5l42.8 33.3h643.1l42.8-33.3l39.3 50.5zM833.6 232L512 482L190.4 232l-42.8-33.3l-39.3 50.5l27.6 21.5l341.6 265.6a55.99 55.99 0 0 0 68.7 0L888 270.8l27.6-21.5l-39.3-50.5z"></path></svg>
              </a>
            
          </td>
          <td>
            
              <a href="http://com-partidauruguay.weebly.com/" target="_blank" rel="noopener" aria-label="Visit national MO website for Uruguay (opens in new tab)"><span class="data-table__label-full">Visit ↗</span><span class="data-table__label-short">↗</span></a>
            
          </td>
          <td class="data-table__hide-mobile data-table__num">
            1987
          </td>
          <td class="data-table__hide-mobile data-table__num">
            29
          </td>
          <td class="data-table__hide-mobile">
            
          </td>
        </tr>
        
        <tr>
          <td>
            <a href="/countries/USA/" class="data-table__country-cell">
              <img class="data-table__country-flag" src="/assets/images/countries/flags/usa.svg" alt="">
              <span class="data-table__country-full">United States of America</span><span class="data-table__country-iso">USA</span>
            </a>
          </td>
          <td>
            
              Karen Bliss
            
          </td>
          <td>
            
              <a href="mailto:amchq@maa.org" class="js-contact-email" data-email-user="amchq" data-email-domain="maa.org" aria-label="Email Karen Bliss" title="Email">
                <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 1024 1024" aria-hidden="true" focusable="false"><path fill="currentColor" d="M928 160H96c-17.7 0-32 14.3-32 32v640c0 17.7 14.3 32 32 32h832c17.7 0 32-14.3 32-32V192c0-17.7-14.3-32-32-32m-40 110.8V792H136V270.8l-27.6-21.5l39.3-50.5l42.8 33.3h643.1l42.8-33.3l39.3 50.5zM833.6 232L512 482L190.4 232l-42.8-33.3l-39.3 50.5l27.6 21.5l341.6 265.6a55.99 55.99 0 0 0 68.7 0L888 270.8l27.6-21.5l-39.3-50.5z"></path></svg>
              </a>
            
          </td>
          <td>
            
              <a href="https://maa.org/student-programs/amc/" target="_blank" rel="noopener" aria-label="Visit national MO website for United States of America (opens in new tab)"><span class="data-table__label-full">Visit ↗</span><span class="data-table__label-short">↗</span></a>
            
          </td>
          <td class="data-table__hide-mobile data-table__num">
            1974
          </td>
          <td class="data-table__hide-mobile data-table__num">
            52
          </td>
          <td class="data-table__hide-mobile">
            
              1981, 2001
            
          </td>
        </tr>
        
        <tr class="data-table__row--inactive">
          <td>
            <a href="/countries/USS/" class="data-table__country-cell">
              <img class="data-table__country-flag" src="/assets/images/countries/flags/uss.svg" alt="">
              <span class="data-table__country-full">Union of Soviet Socialist Republics</span><span class="data-table__country-iso">USS</span>
            </a>
          </td>
          <td>
            
          </td>
          <td>
            
          </td>
          <td>
            
          </td>
          <td class="data-table__hide-mobile data-table__num">
            1959
          </td>
          <td class="data-table__hide-mobile data-table__num">
            29
          </td>
          <td class="data-table__hide-mobile">
            
              1964, 1968, 1973
            
          </td>
        </tr>
        
        <tr>
          <td>
            <a href="/countries/UZB/" class="data-table__country-cell">
              <img class="data-table__country-flag" src="/assets/images/countries/flags/uzb.svg" alt="">
              <span class="data-table__country-full">Uzbekistan</span><span class="data-table__country-iso">UZB</span>
            </a>
          </td>
          <td>
            
              Science Olympiad Center
            
          </td>
          <td>
            
              <a href="mailto:info@olympcenter.uz" class="js-contact-email" data-email-user="info" data-email-domain="olympcenter.uz" aria-label="Email Science Olympiad Center" title="Email">
                <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 1024 1024" aria-hidden="true" focusable="false"><path fill="currentColor" d="M928 160H96c-17.7 0-32 14.3-32 32v640c0 17.7 14.3 32 32 32h832c17.7 0 32-14.3 32-32V192c0-17.7-14.3-32-32-32m-40 110.8V792H136V270.8l-27.6-21.5l39.3-50.5l42.8 33.3h643.1l42.8-33.3l39.3 50.5zM833.6 232L512 482L190.4 232l-42.8-33.3l-39.3 50.5l27.6 21.5l341.6 265.6a55.99 55.99 0 0 0 68.7 0L888 270.8l27.6-21.5l-39.3-50.5z"></path></svg>
              </a>
            
          </td>
          <td>
            
              <a href="http://olympiad.uzedu.uz" target="_blank" rel="noopener" aria-label="Visit national MO website for Uzbekistan (opens in new tab)"><span class="data-table__label-full">Visit ↗</span><span class="data-table__label-short">↗</span></a>
            
          </td>
          <td class="data-table__hide-mobile data-table__num">
            1997
          </td>
          <td class="data-table__hide-mobile data-table__num">
            25
          </td>
          <td class="data-table__hide-mobile">
            
          </td>
        </tr>
        
        <tr>
          <td>
            <a href="/countries/VEN/" class="data-table__country-cell">
              <img class="data-table__country-flag" src="/assets/images/countries/flags/ven.svg" alt="">
              <span class="data-table__country-full">Venezuela</span><span class="data-table__country-iso">VEN</span>
            </a>
          </td>
          <td>
            
              Rafael Sánchez
            
          </td>
          <td>
            
              <a href="mailto:lamonedar@gmail.com" class="js-contact-email" data-email-user="lamonedar" data-email-domain="gmail.com" aria-label="Email Rafael Sánchez" title="Email">
                <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 1024 1024" aria-hidden="true" focusable="false"><path fill="currentColor" d="M928 160H96c-17.7 0-32 14.3-32 32v640c0 17.7 14.3 32 32 32h832c17.7 0 32-14.3 32-32V192c0-17.7-14.3-32-32-32m-40 110.8V792H136V270.8l-27.6-21.5l39.3-50.5l42.8 33.3h643.1l42.8-33.3l39.3 50.5zM833.6 232L512 482L190.4 232l-42.8-33.3l-39.3 50.5l27.6 21.5l341.6 265.6a55.99 55.99 0 0 0 68.7 0L888 270.8l27.6-21.5l-39.3-50.5z"></path></svg>
              </a>
            
          </td>
          <td>
            
              <a href="https://www.acmven.org" target="_blank" rel="noopener" aria-label="Visit national MO website for Venezuela (opens in new tab)"><span class="data-table__label-full">Visit ↗</span><span class="data-table__label-short">↗</span></a>
            
          </td>
          <td class="data-table__hide-mobile data-table__num">
            1981
          </td>
          <td class="data-table__hide-mobile data-table__num">
            32
          </td>
          <td class="data-table__hide-mobile">
            
          </td>
        </tr>
        
        <tr>
          <td>
            <a href="/countries/VNM/" class="data-table__country-cell">
              <img class="data-table__country-flag" src="/assets/images/countries/flags/vnm.svg" alt="">
              <span class="data-table__country-full">Vietnam</span><span class="data-table__country-iso">VNM</span>
            </a>
          </td>
          <td>
            
              Gia Vuong Nguyen Chu
            
          </td>
          <td>
            
              <a href="mailto:ncgvuong@math.ac.vn" class="js-contact-email" data-email-user="ncgvuong" data-email-domain="math.ac.vn" aria-label="Email Gia Vuong Nguyen Chu" title="Email">
                <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 1024 1024" aria-hidden="true" focusable="false"><path fill="currentColor" d="M928 160H96c-17.7 0-32 14.3-32 32v640c0 17.7 14.3 32 32 32h832c17.7 0 32-14.3 32-32V192c0-17.7-14.3-32-32-32m-40 110.8V792H136V270.8l-27.6-21.5l39.3-50.5l42.8 33.3h643.1l42.8-33.3l39.3 50.5zM833.6 232L512 482L190.4 232l-42.8-33.3l-39.3 50.5l27.6 21.5l341.6 265.6a55.99 55.99 0 0 0 68.7 0L888 270.8l27.6-21.5l-39.3-50.5z"></path></svg>
              </a>
            
          </td>
          <td>
            
          </td>
          <td class="data-table__hide-mobile data-table__num">
            1974
          </td>
          <td class="data-table__hide-mobile data-table__num">
            50
          </td>
          <td class="data-table__hide-mobile">
            
              2007
            
          </td>
        </tr>
        
        <tr>
          <td>
            <a href="/countries/YEM/" class="data-table__country-cell">
              <img class="data-table__country-flag" src="/assets/images/countries/flags/yem.svg" alt="">
              <span class="data-table__country-full">Yemen</span><span class="data-table__country-iso">YEM</span>
            </a>
          </td>
          <td>
            
              Munaf Abood
            
          </td>
          <td>
            
              <a href="mailto:munafabood@hotmail.com" class="js-contact-email" data-email-user="munafabood" data-email-domain="hotmail.com" aria-label="Email Munaf Abood" title="Email">
                <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 1024 1024" aria-hidden="true" focusable="false"><path fill="currentColor" d="M928 160H96c-17.7 0-32 14.3-32 32v640c0 17.7 14.3 32 32 32h832c17.7 0 32-14.3 32-32V192c0-17.7-14.3-32-32-32m-40 110.8V792H136V270.8l-27.6-21.5l39.3-50.5l42.8 33.3h643.1l42.8-33.3l39.3 50.5zM833.6 232L512 482L190.4 232l-42.8-33.3l-39.3 50.5l27.6 21.5l341.6 265.6a55.99 55.99 0 0 0 68.7 0L888 270.8l27.6-21.5l-39.3-50.5z"></path></svg>
              </a>
            
          </td>
          <td>
            
          </td>
          <td class="data-table__hide-mobile data-table__num">
            
          </td>
          <td class="data-table__hide-mobile data-table__num">
            0
          </td>
          <td class="data-table__hide-mobile">
            
          </td>
        </tr>
        
        <tr class="data-table__row--inactive">
          <td>
            <a href="/countries/YUG/" class="data-table__country-cell">
              <img class="data-table__country-flag" src="/assets/images/countries/flags/yug.svg" alt="">
              <span class="data-table__country-full">Yugoslavia</span><span class="data-table__country-iso">YUG</span>
            </a>
          </td>
          <td>
            
          </td>
          <td>
            
          </td>
          <td>
            
          </td>
          <td class="data-table__hide-mobile data-table__num">
            1963
          </td>
          <td class="data-table__hide-mobile data-table__num">
            37
          </td>
          <td class="data-table__hide-mobile">
            
              1967, 1977
            
          </td>
        </tr>
        
        <tr>
          <td>
            <a href="/countries/ZWE/" class="data-table__country-cell">
              <img class="data-table__country-flag" src="/assets/images/countries/flags/zwe.svg" alt="">
              <span class="data-table__country-full">Zimbabwe</span><span class="data-table__country-iso">ZWE</span>
            </a>
          </td>
          <td>
            
              A Stewart
            
          </td>
          <td>
            
              <a href="mailto:stewarta@maths.uz.ac.zw" class="js-contact-email" data-email-user="stewarta" data-email-domain="maths.uz.ac.zw" aria-label="Email A Stewart" title="Email">
                <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 1024 1024" aria-hidden="true" focusable="false"><path fill="currentColor" d="M928 160H96c-17.7 0-32 14.3-32 32v640c0 17.7 14.3 32 32 32h832c17.7 0 32-14.3 32-32V192c0-17.7-14.3-32-32-32m-40 110.8V792H136V270.8l-27.6-21.5l39.3-50.5l42.8 33.3h643.1l42.8-33.3l39.3 50.5zM833.6 232L512 482L190.4 232l-42.8-33.3l-39.3 50.5l27.6 21.5l341.6 265.6a55.99 55.99 0 0 0 68.7 0L888 270.8l27.6-21.5l-39.3-50.5z"></path></svg>
              </a>
            
          </td>
          <td>
            
          </td>
          <td class="data-table__hide-mobile data-table__num">
            2009
          </td>
          <td class="data-table__hide-mobile data-table__num">
            2
          </td>
          <td class="data-table__hide-mobile">
            
          </td>
        </tr>
        
      </tbody>
"""

soup = BeautifulSoup(html_content, "html.parser")

paises = {}

# Localiza todos os elementos do nome do país
nomes_paises = soup.find_all("span", class_="data-table__country-full")

for span_nome in nomes_paises:
    # Procura o próximo elemento que contenha a classe do código ISO
    span_iso = span_nome.find_next_sibling(
        "span", class_="data-table__country-iso"
    )

    if span_iso:
        nome = span_nome.get_text(strip=True)
        iso = span_iso.get_text(strip=True)
        paises[iso] = nome

print(paises)
# Saída: {'CZS': 'Czechoslovakia'}