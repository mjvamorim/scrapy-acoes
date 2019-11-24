# -*- coding: utf-8 -*-
import scrapy

##### scrapy crawl  acoes -o acoes.json ###########e

class AcoesSpider(scrapy.Spider):
    name = 'acoes'
    acoes = []
    start_urls = ['http://www.fundamentus.com.br/detalhes.php']


    def parse(self, response):
        funds = response.xpath('//*[@id="test1"]/tbody/tr')
        for papel in funds:
            url = 'http://www.fundamentus.com.br/'+papel.xpath('.//a/@href').extract_first()
            acao = url[url.find('=')+1:]
            self.log('Acão  %s' % acao)
            self.acoes.append(acao)
            yield scrapy.Request(url=url, callback=self.parse_detail)



    def parse_detail(self, response):
        titulo = response.xpath('//div[@class="atual"]/p/strong/text()').get().strip()
        preco =  response.xpath('//html/body/div[1]/div[2]/table[1]/tr[1]/td[4]/span/text()').get().strip()
        p_l = response.xpath('//html/body/div[1]/div[2]/table[3]/tr[2]/td[4]/span/text()').get().strip()
        n_acoes = response.xpath('//html/body/div[1]/div[2]/table[2]/tr[2]/td[4]/span/text()').get().strip()
        patrimonio = response.xpath('//html/body/div[1]/div[2]/table[4]/tr[4]/td[4]/span/text()').get().strip()
        p_vp = response.xpath('//html/body/div[1]/div[2]/table[3]/tr[3]/td[4]/span/text()').get().strip()
        ebit = response.xpath('//html/body/div[1]/div[2]/table[3]/tr[5]/td[6]/span/text()').get().strip()
        roe =      response.xpath('//html/body/div[1]/div[2]/table[3]/tr[9]/td[6]/span/text()').get().strip()
        roic =     response.xpath('//html/body/div[1]/div[2]/table[3]/tr[8]/td[6]/span/text()').get().strip()
        liquidez = response.xpath('//html/body/div[1]/div[2]/table[3]/tr[10]/td[6]/span/text()').get().strip()
        yield {
            'titulo': titulo,
            'preco' : preco,
            'p_l': p_l,
            'n_acoes' : n_acoes,
            'patrimonio' : patrimonio,
            'p_vp' : p_vp,
            'ebit' : ebit,
            'roe' : roe,
            'roic' : roic,
            'liquidez' : liquidez
        }
       

@gerar csv

      
