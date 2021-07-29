def block_tag(text, _class='success'):
    return f'<div class={_class}">{text}</div>'


if __name__ == '__main__':
    # Testes (assertions)

    assert block_tag('Successfully Added!') == \
        '<div class="success">Successfully Added!</div>'
    assert block_tag('Unable to Delete!', 'error') == \
        '<div class="error">Unable to Delete!</div>'