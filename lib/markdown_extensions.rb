require 'kramdown/parser/kramdown'

module MarkdownExtensions
  class Kramdown::Parser::WikiKramdown < Kramdown::Parser::Kramdown
    def initialize(source, options)
      super
      # Table parser matches [[a|b]
      @block_parsers.delete :table
      @span_parsers.unshift :wiki_link
    end

    def parse_wiki_link
      @src.pos += @src.matched_size
      link = Element.new :a
      link.attr['href'] = (@src[2] || @src[1]) + @src[3]
      add_text(@src[1], link)
      @tree.children << link
    end

    define_parser(:wiki_link, /\[\[([^|#]*)\|?([^|#]*)(#?[^#|]*)\]\]/, '\\[\\[')
  end
end
