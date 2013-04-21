require 'kramdown/parser/kramdown'
require 'middleman-core/sitemap'

module MarkdownExtensions
  class Kramdown::Parser::WikiKramdown < Kramdown::Parser::Kramdown
    def initialize(source, options)
      super
      @app = options[:app]
      # Table parser matches [[a|b]
      @block_parsers.delete :table
      @span_parsers.unshift :wiki_link
    end

    Kramdown::Options.define(:app, Object, nil, '') { |o| o }

    def parse_wiki_link
      @src.pos += @src.matched_size

      page, text = link_target_and_text(@src[1], @src[2])

      if page.start_with? 'img'
        img = Element.new :img
        img.attr['src'] = page
        @tree.children << img
        return
      end

      url = @app.page_url page
      if url
        link = Element.new :a
        link.attr['href'] = url + @src[3]
        add_text(text, link)
        @tree.children << link
      else
        add_text(text)
      end
    end

    def link_target_and_text(a, b)
      if b.empty?
        return a, a.gsub('_', ' ')
      else
        return b, a
      end
    end

    define_parser(:wiki_link, /\[\[([^!][^\]|#]*)\|?([^\]|#]*)(#?[^\]#|]*)\]\]/, '\\[\\[[^!]')

    def handle_extension(name, opts, body, type)
      case name
      when 'template'
        template_name = opts.delete('name')
        opts['body'] = body
        @tree.children << Element.new(:raw, @app.partial(template_name, locals: opts))
        true
      else
        super(name, opts, body, type)
      end
    end
  end

  class Kramdown::Converter::Html
    alias_method :old_convert_root, :convert_root

    def convert_root(el, indent)
      result = old_convert_root(el, indent)
      toc_tree = generate_toc_tree(@toc, :ol, {})
      result.prepend convert(toc_tree, 0) unless toc_tree.children.empty?
      result
    end

    def convert_img(el, indent)
      el.attr['src'].prepend '/docs/3.1/'
      "<img#{html_attributes(el.attr)} />"
    end
  end
end
